userNum = int(input('Enter the number to convert: '))
base = int(input('Enter the base: '))
n = userNum

num_letter = {'10':'A','11':'B',
                  '12':'C','13':'D',
                  '14':'E','15':'F',
                  '16':'G','17':'H',
                  '18':'I','19':'J',
                  '20':'K','21':'L',
                  '22': 'M', '23':'N',
                  '24':'O','25':'P',
                  '26':'Q','27':'R',
                  '28':'S', '29':'T',
                  '30':'U','31':'V',
                  '32':'W','33':'X',
                  '34':'Y','35':'Z' 
                 }

list_digit = []
if b <= 9:
    while n != 1:
        k = n % base
        list_digit.append(k)
        n = n // base
    list_digit.append(n)
    
else:
    k = n % base
    if str(k) in num_letter:
        list_digit.append(num_letter[str(k)])
        n = n // base  
    else:
        print('Unexpected Error') 
list_digit.reverse()

newNum = ''
for i in list_digit:
    newNum += str(i)

print(f'The (decimal) {userNum} converts into {newNum} in base {base}')
