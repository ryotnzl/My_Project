#
# Break test
# Ryo
#

sum = 0

while True:
    # 1. Input
    x1 = input("Enter x1: ")
    x2 = input("Enter x2: ")
    op = input("Enter operator: ")
    
    # 2. Process
    if op == "+":
        ans = int(x1) + int(x2)
        print("Answer: "+ str(ans))
    elif op == "-":
        ans = int(x1) - int(x2)
        print("Answer: "+ str(ans))
    else:
        print("Invalid")
        continue

    choice = input("Continue? (Yes/No)")
    if choice == "No":
        break