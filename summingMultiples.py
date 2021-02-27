add = 0
num = 20
'''
for i in range(20, 51):
    if (i % 3) == 0:
        add += i
print(add)
'''

while num < 51:
    if (num % 3) == 0:
        add += num
    num += 1
print(add)
