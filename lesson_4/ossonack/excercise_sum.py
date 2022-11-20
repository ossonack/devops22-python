start_int = int(input("Input a start integer: "))
end_int = int(input("Input a ending integer: "))
sum = 0
for i in range(start_int, end_int):
    print(i)
    sum += i
print("Sum of all integers:", sum)