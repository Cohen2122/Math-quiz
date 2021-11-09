import random
def main():

    ops = ["+", "-", "/", "*"]
    score = 0

    print("Maths quiz")
    
    print()

    print("Enter number range: ")
    x = intinput("Lowest number: ")
    y = intinput("highest number: ")

    print()

    a = intinput("How many questions do you want to answer? ")

        
    for times in range(a):
        
        num1 = random.randint(x, y)
        num2 = random.randint(x, y)
        op = ops[random.randint(0, 3)]
    #    print(op)

        if op == "/":
            check = div(num1, num2)
        if op == "*":
            check = mul(num1, num2)
        if op == "+":
            check = add(num1, num2)
        if op == "-":
            check = sub(num1, num2)
            
        if check == True:
            score += 1
    print()
    print("You got " + str(score) + "/" + str(a) + " !")
    print()
    while True:
        print("Would you like to save your score? Y/N")
        b = input()
        if b == "Y":
            print("What is your name?")
            name = input()
            file = open("results.txt", "a")
            file.write(name + ": " + str(score) + "/" + str(a) + "\n")
            file.close()
            break
        if b == "N":
            break
    



def div(num1, num2):

    if num2 == 0:
        num2 = 1
    
    a = num1
    num1 = num1 * num2
    
    print("What is " + str(num1) + " / " + str(num2) + " = ", end="")
    ans = intinput("")
    if ans == a:
        return True
    else:
        return False

def mul(a, b):

    c = a * b

    print("What is " + str(a) + " * " + str(b) + " = ", end="")
    ans = intinput("")
    if ans == c:
        return True
    else:
        return False
def add(a, b):
    
    c = a + b

    print("What is " + str(a) + " + " + str(b) + " = ", end="")
    ans = intinput("")
    if ans == c:
        return True
    else:
        return False

def sub(a, b):

    if a > b:
        c = a - b
        print("What is " + str(a) + " - " + str(b) + " = ", end="")
    elif b > a:
        print("What is " + str(b) + " - " + str(a) + " = ", end="")
        c = b - a
    else:
        print("What is " + str(a) + " - " + str(b) + " = ", end="")
        c = 0

    ans = intinput("")
    if ans == c:
        return True
    else:
        return False

def intinput(prompt):
    while True:
        a = input(prompt)
        if a.isdigit() == True:
            a = int(a)
            return a
        


if "__main__" == __name__:
    main()
