#Write a program that counts up the number of vowels [a, e, i, o, 
# u] contained in the string.

text=input("enter your string\t ")
x = len(text)
count = 0 
for i in range(x) :
    if(text[i] == 'a' or text[i] == 'i' or text[i] == 'e' or text[i] == 'o' or text[i] == 'o'  ) :
        count +=1 

print("count is : " , count)