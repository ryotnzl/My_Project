#
# While test
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
    elif op == "-":
        ans = int(x1) - int(x2)
    
    # 3. Output
    print("Answer: "+ str(ans))
