# Default parameters:
# Create a program which has a main function and a subfunction called tester.
# The main function prompts user for an input "Write something (quit ends): " and sends this input to the subfunction as a parameter.
# Define the subfunction tester so that it has one parameter called "givenstring", which has the default value "Too short".
# If the user input is less than 10 characters, the program uses the default value and if 10 or more, it prints the usergiven input.
# If the user inputs "quit", the program is terminated.

given_string = True

while given_string:
    given_string = input("Write something (quit ends): ")

    if given_string != "quit" and len(given_string) < 10:
        print("Too short")
    elif given_string != "quit" and len(given_string) >= 10:
        print(given_string)
    elif given_string == "quit":
        given_string = False
