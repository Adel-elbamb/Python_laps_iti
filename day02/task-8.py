def numbers():
    nums = []  

    while True:
        x = input("Enter a number (or 'done' to finish): ")  

        if x.lower() == "done":  
            break  

        try:
            num = float(x)  
            nums.append(num)  
        except ValueError:
            print("Error: Please enter a valid number.")  
            continue  

    if nums:  
        total = sum(nums)  
        count = len(nums)  
        avg = total / count  
        print(f"Count: {count}, Sum: {total}, Average: {avg:.2f}")  
    else:
        print("No numbers were entered.")

numbers()
