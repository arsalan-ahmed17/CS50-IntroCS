import cs50

while True:
    try:
        height = cs50.get_int("Height of the pyramid? ")
        if 1 <= height <= 8:
            break
    except ValueError:
        pass

for i in range(1, height + 1):
    spaces = " " * (height - i)
    hashes = "#" * i
    print(spaces + hashes + " " + hashes)

for i in range (height - 1, 0, -1):
    spaces = " " * (height - i)
    hashes = "#" * i
    print(spaces + hashes + " " + hashes)
