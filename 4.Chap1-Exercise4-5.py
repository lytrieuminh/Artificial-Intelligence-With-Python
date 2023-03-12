# Supermarket:
# 🛒🛍️ Make simple Supermarket -program:
# ✅ having 10 products with prices in a list as follows:[10,14,22,33,44,13,22,55,66,77].
# ✅ asking product number from 1 to 10 and summing its price to totalsum and printing product number and price for every product as in example.
# ✅ asking products until user gives '0' to quit the program (while-loop).
# ✅ printing  "Total:" and the total sum of prices.
# ✅ asking "Payment:" from user and printing "Change:" and finally  calculating and printing the amount of change (payment - totalsum) to customer.
# 🚨 You must use in this program: while, input

products = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
totalsum = 0

print("Supermarket\n===========")

while True:
    selection = int(input("Please select product (1-10) 0 to Quit: "))

    if selection != 0:
        price = products[selection - 1]
        totalsum += price
        print(f"Product: {selection}    Price: {price}")

    elif selection == 0:
        print(f"Total: {totalsum}")
        print("Payment: ")
        payment = int(input())
        change = payment - totalsum
        print(f"Change: {change}")
        break
