from builtins import input, ZeroDivisionError

while True:
    try:
        number = int(input("What is your fav number boss?:\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    finally:
        print("Loop Complete")
