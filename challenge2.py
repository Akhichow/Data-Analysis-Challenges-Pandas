print("Enter a number between 1 to 100")
n = int(input())

if (n % 2) != 0:
    print("Weird")
else:
    if n in range(6, 21, 2):
        print("Weird")
    else:
        print("Not Weird")