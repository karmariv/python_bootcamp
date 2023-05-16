#def arithmetic_arranger(problems):
#Define variables
import sys 

op = '' #operator
problems = 0
line1 = ''
line2 = ''
line3 = ''
test = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


#get the size of the array dddsfdfsdfsd
problems = len(test)

#Abort if there are more than 5 problems
if(problems > 5):
    print("Error: Too many problems")
    #return
    sys.exit()

for prob in test:
    elem = prob.split()

    #get the length of the greater number in the problem
    elem_length = 0
    for e in elem:
        if len(e) > elem_length:
            elem_length = len(e)

    #get the operator
    op = elem[1]

    #add element to each line
    elem_1 = elem[0]
    elem_2 = elem[2]

    if len(elem_1) < elem_length:
        elem_1 = elem_1.rjust(elem_length + 2)

    
    if len(elem_2) == elem_length:
        elem_2 = (op + ' ' + elem_2).rjust(elem_length) 

    #Build string
    line1 = line1 + elem_1 + '    '
    line2 = line2 + elem_2 + '    '
    line3 = line3 + line3.rjust(elem_length, '-') + '    '

print(line1)
print(line2)
print(line3)




   # return arranged_problems