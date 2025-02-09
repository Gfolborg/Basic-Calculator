print("Basic Calculator")
print("----------------")
print("You will enter first number, choose the operator, then enter second number")
print(" ")

user_input = input("Would you like to use the calcultor (Y/N): ")

while user_input.lower() != "y" and user_input.lower() != "n":
    print('Error: Enter "Y" for Yes and "N" for No')
    print(" ")
    user_input = input("Would you like to use the calculator (Y/N): ")
    if user_input.lower() == "n":
        print(" ")
        print("#######################")
        print("#######################")
        print("##                   ##")
        print("## Ending Calculator ##")
        print("##                   ##")
        print("#######################")
        print("#######################")
        exit()
    elif user_input.lower() == "y":
        print(" ")
        break


if user_input.lower() == "y":
    pass
elif user_input.lower() == "n":
    print(" ")
    print("#######################")
    print("#######################")
    print("##                   ##")
    print("## Ending Calculator ##")
    print("##                   ##")
    print("#######################")
    print("#######################")

user_input.lower == "y"
print('''Enter number and math operator as you would a calculator''')
print(" ")
math_input = input()

def calculator(math_input):
    try:
        results = eval(math_input)
        return f"Answer: {results}"
    except (SyntaxError, NameError, TypeError) as e:
        print(f"Error with math input: {e}")
print(calculator(math_input))
print(" ")

ask_to_continue = input("Would you like to continue? (Y/N): ")


    




