print("Basic Calculator")
print("----------------")
print("You will enter first number, choose the operator, then enter second number")
print(" ")

user_input = input("Would you like to use the calcultor (Y/N): ")

# if user_input.lower() == "n":
#     print("#####################")
#     print("#                   #")
#     print("# Ending Calculator #")
#     print("#                   #")
#     print("#####################")

while user_input.lower() != "y" or user_input.lower() != "n":
    print('Error: Enter "Y" for Yes and "N" for No')
    print(" ")
    user_input = input("Would you like to use the calculator (Y/N): ")
    if user_input.lower() == "n":
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

number_1 = input("Choose first number: ")
# operator = input("Choose operator: ")
# number_2 = input("Choose second number: ")
# proceed = input("Would you like to try again? ")
# result = 0




