print("\t\t\t\t\t\t\t\t\t\tBASIC CALCULATOR")

cont = "y"
while cont == "y" or cont == "Y":
    op = input("Operator\n")
    int1 = int(input("Number 1\n"))
    int2 = int(input("Number 2\n"))

    if op == "*":
        print(int1 * int2,"\n")
    elif op == "%":
        print(int1 % int2,"\n")
    elif op == "/":
        print(int1 / int2,"\n")
    elif op == "+":
        print(int1 + int2,"\n")
    elif op == "-":
        print(int1 - int2,"\n")
    else :
        print("You entered wrong operator\n")

