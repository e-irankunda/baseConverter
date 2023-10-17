userNum = int(input('Enter the number to convert: '))
base = int(input('Enter the base: '))
n = userNum

list_digit = []
while n!= 1:
    k = n % base 
    list_digit.append(k)
    n = n // base
list_digit.append(n)
list_digit.reverse()

newNum = ''
for i in list_digit:
    newNum += str(i)
print(f'The (decimal) {userNum} converts into {newNum} in base {base}')
