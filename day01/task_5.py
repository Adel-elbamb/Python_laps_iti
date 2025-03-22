# num = int(input("enter your number "))

# for i in range (num) :
#     for x in range(i+1) :
#         print("*" , end="")
#     print()
# ==============================
# rows = 5
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * i)

# ==============================
num = int(input("Enter your number: "))

for i in range(num):
    
    for j in range(num - i - 1):
        print(" ", end="")
 
    for x in range(i + 1):
        print("*", end="")
    print()  


