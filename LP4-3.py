eggs = int(input("Enter number of eggs:"))
dozens = eggs / 12
price = 0
if 0 < dozens <= 3:
    price = 0.50
elif 4 < eggs <= 5:
    price = 0.45
elif 6 < eggs <= 10:
    price = 0.40
elif eggs >= 11:
    price = 0.35
else:
    print("The number of copies is invalid")
    quit()
total = dozens * price
print("Number of dozens: ",str(round(dozens, 2)))
print("Price per dozen: ", str(round(price, 2)))
print("Total cost is: ", str(round(total, 2)))

