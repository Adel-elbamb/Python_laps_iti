text = input("Enter your String :   ")
new_text = "" 

for i in range(len(text)):
    if text[i] not in "aeiou":  
        new_text += text[i]  
print(new_text)
