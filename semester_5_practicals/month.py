months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
          9: "September", 10: "October",
          11: "November", 12: "December"}

data = str(input("Enter any month number : "))

if data == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print(f"{months[data]} has 31 days..!!")

elif data == 4 or 6 or 9 or 11:
    print(f"{months[data]} has 30 days..!!")

elif data == 2:
    print(f"{months[data]} has 28 days")

else:
    print("Invalid entry...!!")
print(data)