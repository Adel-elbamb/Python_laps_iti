# Fill an array of 5 elements from the user, Sort it in descending 
# and ascending orders then display the output.
# ==========================1===================
def  arr_sort(num) :
    try:
        list_number = []
        for i in range(num) :
            inp = int(input(f"Enter number of {i+1} ,... "))
            list_number .append(inp)
            
        srt = sorted(list_number)
        srt_rev = sorted(list_number ,reverse=True)
        print(srt)
        print(srt_rev)
    except:
        print("error plz enter valid number ")

try:
    x = int(input("enter number of lenght ")) 
    arr_sort(x)
except Exception :
    print("errror enter nubetrr") 
