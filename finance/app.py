import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    # Get user's cash
    user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    if not user or "cash" not in user[0]:
        return apology("User data not found", 500)
    cash = user[0]["cash"]

    # Compute portfolio by grouping transactions.
    # (Assumes you have a 'transactions' table with columns: user_id, symbol, shares, price, etc.)
    portfolio = db.execute(
        "SELECT symbol, SUM(shares) as quantity FROM transactions WHERE user_id = ? GROUP BY symbol HAVING quantity > 0",
        user_id
    )

    prices = []         # To store current prices for each asset
    total_stock_value = 0  # Total value of stocks

    # For each asset in portfolio, look up the current price and compute value.
    for asset in portfolio:
        stock = lookup(asset["symbol"])
        if not stock:
            price = 0
        else:
            price = stock["price"]
        prices.append(price)
        total_stock_value += price * asset["quantity"]

    # Calculate overall balance: cash + total stock value
    total_bal = cash + total_stock_value

    return render_template("index.html", cash=cash, port=portfolio, prices=prices, total_bal=total_bal)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        if not shares.isdigit() or int(shares) <= 0:
            return apology("Invalid number of shares")
        shares = int(shares)
        stock = lookup(symbol)
        if not stock:
            return apology("Invalid stock symbol")
        cost = shares * stock["price"]
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        if cash < cost:
            return apology("Not enough cash")
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", cost, user_id)
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", user_id, symbol, shares, stock["price"])
        flash("Bought successfully!")
        return redirect("/")
    return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])
    return render_template("history.html", transactions=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return apology("must provide username and password", 403)
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid username and/or password", 403)
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        if not stock:
            return apology("Invalid stock symbol")
        return render_template("quoted.html", stock=stock)
    return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not username or not password or password != confirmation:
            return apology("Invalid input")
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            return apology("Username already exists")
        hash_password = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_password)
        flash("Registered successfully!")
        return redirect("/login")
    return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares_str = request.form.get("shares")

        # Ensure a valid positive integer was provided for shares
        if not shares_str or not shares_str.isdigit() or int(shares_str) <= 0:
            return apology("Invalid number of shares")
        shares = int(shares_str)

        # Validate the stock symbol
        stock = lookup(symbol)
        if not stock:
            return apology("Invalid stock symbol")

        # Check if the user owns enough shares by summing from transactions
        owned = db.execute(
            "SELECT SUM(shares) AS quantity FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol",
            user_id, symbol
        )
        if not owned or owned[0]["quantity"] < shares:
            return apology("Not enough shares")

        # Calculate total value from sale
        total_value = shares * stock["price"]

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_value, user_id)

        # Record the sale as a negative transaction
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   user_id, symbol, -shares, stock["price"])

        

        flash("Sold successfully!")
        return redirect("/")

    else:
        # For GET: build a list of symbols the user owns (with positive shares)
        symbols = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            user_id
        )
        return render_template("sell.html", symbols=symbols)
