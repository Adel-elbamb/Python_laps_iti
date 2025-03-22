# ● Write a function that takes a string and prints the 
# longest alphabetical ordered substring occurred For example, if 
# the string is 'abdulrahman' then the output is: Longest substring in 
# alphabetical order is: abdu
def text(s):
    longest = current = s[0]  
    for i in range(len(s) - 1):  
        if s[i] <= s[i + 1]:  
            current += s[i + 1]  
        else:
            if len(current) > len(longest):  
                longest = current  
            current = s[i + 1]  

    if len(current) > len(longest):  
        longest = current  

    print(f"Longest : {longest}")

inp = input("Enter a string: ").strip()  

if inp.isdigit():  
    print("Error: Please enter a valid string, not a number.")
else:
 text(inp)  
 text(inp)   
