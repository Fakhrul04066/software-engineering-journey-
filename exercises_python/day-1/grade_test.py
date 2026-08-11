marks = int(input("Enter the marks = "))

match marks:
    case x if 90 <= x <= 100:
        print("A+")
    case x if 80 <= x < 90:
        print("A")
    case x if 70 <= x < 80:
        print("A-")
    case x if 60 <= x < 70:
        print("B")
    case x if 50 <= x < 60:
        print("C")
    case _:
        print("Fail")