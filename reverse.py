def reverse():
    Number = int(input("Please Enter any Number: "))
    if 0<Number<1000:
        Reverse = 0
        while (Number > 0):
            Reminder = Number % 10
            Reverse = (Reverse * 10) + Reminder
            Number = Number // 10

        print("\n Reverse of entered number is = %d" % Reverse)
    else:
        print("wrong number")
reverse()




