# Write a program that prints the number of times the string 'iti' 
# occurs in anystring.
# ====================solution========
text = input("Enter the text : ")
search = input("Enter your Search :")
count = 0 ;
x = 0
for i in range(len(text)) :
    # print(x)
    x = text.find(search,x)
    if x == -1 :
        break 
    count +=1 
    x +=1 
print("count is :",count)