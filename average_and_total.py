

'''this is a programme to calculate the total and average of n numbers'''

len = int(input('for how many no. do u want average?: '))

total = 0

for i in range(0,len):
    sum1 = float(input('enter no: '))
    total = sum1 + total

avg = total/len

print('total is:', total)
print('average is:',avg)



'''sum using List'''

len = int(input('for how many no. do u want average?: '))

num = []

for i in range(0,len):
    element = float(input('enter no: '))
    num.append(element)
                
total = sum(num)

avg = total/len

print('total is:', total)
print('average is:',avg)


