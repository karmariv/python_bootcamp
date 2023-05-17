def arithmetic_arranger(problems):
    #Define variables
    import sys 
    import re

    op = '' #operator
    total_items = 0
    line1 = ''
    line2 = ''
    line3 = ''
    #test = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


    #get the size of the array
    total_items = len(problems)

    #Abort if there are more than 5 problems
    if(total_items > 5):
        print("Error: Too many problems")
        return
        #sys.exit()

    for prob in problems:
        divider = ''
        #Check syntax only numbers and operator '+' and '-' are valid 
        # Error: Operator must be '+' or '-'   
        if re.search("[+,-]", prob) == None:
            print("Error with problem ", prob, ": Operator must be '+' or '-'")
            return
            #sys.exit()
    
        elem = prob.split()

        #Error: Numbers must only contain digits.
        if elem[0].isdigit() == False or elem[2].isdigit() == False:
            print("Error with problem ", prob, ": Numbers must only contain digits")
            #sys.exit()
            return
    
        #Error: Numbers cannot be more than four digits
        if len(elem[0]) > 4 or len(elem[2]) > 4:
            print("Error with problem ", prob, ": Numbers cannot be more than four digits")
            #sys.exit()
            return


        #get the length of the greater number in the problem
        elem_length = 0
        for e in elem:
            if len(e) > elem_length:
                elem_length = len(e)

        #get the operator
        op = elem[1]

        #operands
        operand1 = elem[0].rjust(elem_length + 2)
        operand2 = op + ' ' + (elem[2]).rjust(elem_length)
        divider = divider.rjust(elem_length + 2, '-')
    
        #Build string
        line1 = line1 + (operand1).ljust(elem_length + 6)
        line2 = line2 + (operand2).ljust(elem_length + 6)
        line3 = line3 + divider.ljust(elem_length + 6)

    arranged_problems = line1 + '\n' +  line2  + '\n' + line3

    return arranged_problems