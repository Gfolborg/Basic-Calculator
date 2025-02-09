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

print('''Enter number and math operator as you would a calculator''')

math_input = input()

def calculator(math_input):
    try:
        results = eval(math_input)
        return results
    except (SyntaxError, NameError, TypeError) as e:
        print(f"Error with math input: {e}")

print(calculator(math_input))

# operator = input("Choose operator: ")
# number_2 = input("Choose second number: ")
# proceed = input("Would you like to try again? ")
# result = 0




