#● Writea program that prints the locations of "i" character in any 
# string you added
text = input("Enter your text : ")
count =0 
x = []
for i in  range(len(text)) :
    count = text.find("a" , count )
    if count == -1 :
        break
    x.append(count)
    count +=1
print(x)