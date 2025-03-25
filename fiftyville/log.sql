-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema
-- Understanding the whole database, the tables name and information available in the DB.


SELECT COUNT(*) FROM crime_scene_reports;
-- Checking how many entries there are in crime scene reports

SELECT description FROM crime_scene_reports WHERE year = '2023' AND street = 'Humphrey Street';
-- checking for anything abnormal in crime_scene_reports on the day of theft.

-- Found out about bakery from the crime reports scene, let's take a look at those interviews now.
SELECT * FROM interviews WHERE transcript like '%Bakery%';
-- Looking for all the interviews with bakery in their transcript. Can see 3 interview took place on July 28 with Raymond, Eugene, Ruth.

-- Refined my query to eliminate irrelevant interviews on that day.
SELECT * FROM interviews WHERE year = '2023' AND month = '7' AND day = '28' AND transcript LIKE '%bakery%';

/* Leads:
Ruth: thief got into a car, parking lot, security footage, car
Eugene: he recognized, ATM on Leggett Street, withdrew money
Raymond: made a call, <60 seconds, flight out of fiftyville, asked to book ticket.

Now let's take a look at all these leads individually */
-- From Ruth's Interview:
SELECT * FROM bakery_security_logs WHERE year = '2023' AND month = '7' AND day = '28' AND minute BETWEEN '15' AND '25' AND activity = 'exit';

SELECT p.name, bsl.activity, bsl.license_plate, bsl.year, bsl.month, bsl.day, bsl.hour, bsl.minute
FROM bakery_security_logs bsl
JOIN people p ON p.license_plate = bsl.license_plate
WHERE bsl.year = '2023' AND bsl.month = '7'AND bsl.day = '28' AND bsl.hour = 10 AND bsl.minute BETWEEN '15' AND '25';

-- Over to Eugene Interview now:
-- ATM transaction on Leggett Street
SELECT * FROM atm_transactions
WHERE year = '2023' AND month = '07' AND day = '28' AND atm_location = 'Leggett Street';

-- now let's add the name of the account holder using the similar query as above.
SELECT at.*, p.name
FROM atm_transactions at
JOIN bank_accounts b ON at.account_number = b.account_number
JOIN people p ON b.person_id = p.id
WHERE at.atm_location = 'Leggett Street' AND at.year = 2023 AND at.month = '7' AND at.day = '28' AND at.transaction_type = 'withdraw';

-- Over to Raymonth Interview now:
-- Phone Call and Flight Ticket booking
-- Phone Calls made that day less than 60 seconds.
SELECT * FROM phone_calls
WHERE year = '2023' AND month = '7' AND day = '28' AND duration < '60';

-- Now let's add name to these calls.
SELECT p.name, pc.caller, pc.receiver, pc.year, pc.month, pc.day, pc.duration
FROM phone_calls pc
JOIN people p ON pc.caller = p.phone_number
WHERE pc.year = '2023' AND pc.month = '7' AND pc.day = '28' AND pc.duration < 60;

-- exploring airports to check the flights
SELECT * FROM airports WHERE city = 'Fiftyville';
-- the id of fiftyville airport is 8

-- the witness mentioned that they wanted to book the earliest flight out of fiftyville so let's take a look at that now.
SELECT * FROM flights
WHERE origin_airport_id = 8 AND year = '2023' AND month = '7' AND day = '28'
ORDER BY hour;
-- taking note of flight_id 6 as this is the flight thief is on.

-- With the query above, we can see that the destination_airport_id is 5, now let's check which city/airport is id 5
SELECT * FROM airports WHERE id = 5;

-- Airport: Fort Worth International Airport in Dallas, TX. The thief escaped here.

-- Now combining info from all three witnesses and leads
SELECT p.name
FROM bakery_security_logs bsl
JOIN people p ON p.license_plate = bsl.license_plate
JOIN bank_accounts ba on ba.person_id = p.id
JOIN atm_transactions at ON at.account_number = ba.account_number
JOIN phone_calls pc ON pc.caller = p.phone_number
WHERE bsl.year = '2023' AND bsl.month = '7' AND bsl.day = '28' AND bsl.hour = '10' AND bsl.minute BETWEEN 15 AND 25
AND at.atm_location = 'Leggett Street' AND at.year = '2023' AND at.month = '7' AND at.day = '28' AND at.transaction_type = 'withdraw'
AND pc.year = '2023' AND pc.month = '7' AND pc.day = '28' AND pc.duration < 60;

-- Bruce and Diana (either of them) is thief. Now we can check whom of these two was on that flight.
SELECT name FROM people
WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);

SELECT p.name
FROM people p
JOIN passengers ps ON p.passport_number = ps.passport_number
WHERE ps.flight_id = 36
AND p.name IN ('Bruce', 'Diana');


