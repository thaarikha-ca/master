num  = [3, 6, 1, 2, 7, 8, 12, 11, 15, 13, 14]
num1 = [3,4,7,10]
num2 = []
num3 = [-1]

print("CASE 1:")
for x in range(len(num)):
   print(num[x])

print("CASE 2:")
for x in range(len(num)-1, -1, -1):
   print(num[x])

print("CASE 3:")
for x in range(len(num) // 2, len(num)):
    print(num[x])

print("CASE 4:")
for x in range(len(num) // 2, -1, -1):
    print(num[x])

print("CASE 5:")
for x in range(0, len(num), 2):
   print(num[x])

print("CASE 6:")
for x in range(1, len(num), 2):
    print(num[x])

##Welcome