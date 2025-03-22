def arr(lenght , start ) :
    list_number = []
    for i in range (1,lenght+1) :
        start +=1
        list_number.append(start)
    print(f"list is : {list_number}")


lenght = int(input("Enter the lenght of arr:"))
start = int(input("Enter the start of arr: "))

arr(lenght,start)
