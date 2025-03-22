
def  mult() :
    try:
            inp = int(input("Enter the number:"))
            list_number = []
            for i in range (1,inp+1) :
                row = []
                for x in range (1,i+1) :
                    cal = i*x
                    row.append(cal)
                list_number.append(row)
                
            print(list_number)
    except:
         print("error please enter number ")
   
mult()
        
 



