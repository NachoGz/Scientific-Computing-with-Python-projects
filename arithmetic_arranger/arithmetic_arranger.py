

def arithmetic_arranger(problems, results=False):

    # rules
    # max problems is 5
    if len(problems) > 5:
        return "Error: Too many problems."
        

    num1 = []
    num2 = []
    operators = []
    operation = []

    for i in problems:
        x = i.split()
        t1 = x[0]
        op = x[1]
        t2 = x[2]
        num1.append(t1)
        num2.append(t2)
        operators.append(op)
    # max 4 digits
        if len(t1) > 4 or len(t2) > 4:
            return "Error: Numbers cannot be more than four digits."
            
    # only numbers
        elif not t1.isnumeric() or not t2.isnumeric():
            return "Error: Numbers must only contain digits."
            
        # only + or - operators
        elif op == '/' or op == '*':
            return "Error: Operator must be \'+\' or \'-\'."
            
        if op == '+':
            operation.append(str(int(t1) + int(t2)))
        elif op == '-':
            operation.append(str(int(t1) - int(t2)))
        
    first = ''
    second = ''
    result = ''
    lines = ''
    for i in range(len(problems)):

        length = max(len(num1[i]), len(num2[i])) + 2
        top = str(num1[i]).rjust(length)
        bottom = operators[i] + str(num2[i]).rjust(length - 1)
        line = '-'*length
        res = str(operation[i]).rjust(length)

        if problems[i] != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            result += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            result += res
        first.rstrip()
        second.rstrip()
        lines.rstrip()
        
    if results:
        result.rstrip()
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + result
    else:
        arranged_problems = first + '\n' + second + '\n' + lines

    return arranged_problems



print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))

#   123
# +  49
# -----

