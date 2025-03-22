def reverse_string(user_input):
    try:
        return user_input[::-1]  
    except Exception:
        print("Error: Please enter a valid string.")
        return None

def text(t):
    return "".join(sorted(list(t), reverse=True))

inp = input("Enter a string: ").strip()  

if inp.isdigit():  
    print("Error: Please enter a valid string, not a number.")
else:
    print("Descending:", reverse_string(inp))
    print(" Descending :", text(inp))
