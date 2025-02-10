while True:
    user_input = input("Would you like to enter an equation? (Y/N) ")
    print(" ")
    if user_input.lower() != "y" and user_input.lower() != "n":
        print("Enter Y for Yes and N for No")
        print(" ")
    elif user_input.lower() == "y":
        try:
            math_input = input("Enter equation: ")
            print(" ")
            results = eval(math_input)
            print(f"Your answer: {results}")
            print(" ")
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as e:
            print(f"Error with math input: {e}")
            print(" ")
    else:
        print(" ")
        print("#######################")
        print("#######################")
        print("##                   ##")
        print("## Ending Calculator ##")
        print("##                   ##")
        print("#######################")
        print("#######################")
        exit()