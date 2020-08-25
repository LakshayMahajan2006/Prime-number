# Prime-number

n = int(input("Enter a starting number : "))#it takes starting number
u = int(input("Enter a ending number : "))#it takes endinging number
for num in range(n, u+1):
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                break
        else:
            print(num)
