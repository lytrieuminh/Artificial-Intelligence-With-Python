#Using the list:
#Create a small grocery shopping list with the list datastructure:
#Create a program that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit.

#If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list.
#If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.")
#and prompts the user for the removed item ("Which item is deleted?: ").

#If the user selects 0, the first item is removed.
#When the user quits, the final list is printed for the user "The following items remain in the list:" followed by the remaining items one per line.

#If the user selects anything outside the options, including when deleting items, the program responds "Incorrect selection.".

mylist = []
promptForNumbers = True

while True:
  if promptForNumbers:
    n = int(
      input("Would you like to\n(1) Add or\n(2) Remove items or\n(3) Quit?: "))

  if n == 1:
    a = input("What will be added?: ")
    mylist.append(a)
  elif n == 2:
    count = len(mylist)
    print("There are ", count, " items in the list.")
    b = int(input("Which item is deleted?: "))
    if b < count:
      mylist.pop(b)
    else:
      print("Incorrect selection.")

  elif n == 3:
    x = ", ".join(str(i) for i in mylist)
    print("The following items remain in the list:\n", x)
    break
  else:
    print("Incorrect selection.")
    promptForNumbers = True

