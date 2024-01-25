num = int(input("enter number between 1 to 20: "))
print(" ")
if num > 0 and num < 21:
    while num <= 20:
        print(f"Multiplication table for {num}")
        print(" ")

        for i in range(1,11):
            print(f"{num} * {i} = {num * i}")
            
        num += 1
    print(" ")

else:
    print("Please enter a valid number between 1 to 20: ")