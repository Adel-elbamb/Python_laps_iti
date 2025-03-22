def div(number) :
         if(number % 3 == 0 and number % 5 == 0 )  :
                    print("fizzbuzz")
         elif (number % 5 == 0) :
                print("buzz")
         elif(number % 3 == 0 ) :
                print("fizz")
         else :
            print("Number not accupet divide in 3 or 5 or both")
  

try : 
   num = int(input("Enter number :"))
   div(num)
except:
       print("not valid input")
