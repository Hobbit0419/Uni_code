"""
Solutions to module 2 - A calculator
Student: Anton Lindbro
Mail: anton.lindbro.8243@student.uu.se
Reviewed by: Roman 
Reviewed date: 23/9
"""
import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


#Defining functions for log and factorial that checks for evaluation errors
def log(n):
    if n < 0:
        raise EvaluationError("Function log can't evaluate arguments less than 0")
    else:
        return math.log(n)

def fac(n):
    if (n).is_integer() == False:
        raise EvaluationError("Function fac can only evaluate whole numbers")
    else:
        n = int(n)
        return math.factorial(n)
    
def avg(n):
    return sum(n)/len(n)
    


def statement(wtok, variables):
    result = assignment(wtok, variables)
    if not wtok.is_at_end(): #Checks that the rest of the code took us to the end of the line
        raise SyntaxError('Expected end of line')
    return result


def assignment(wtok, variables):
    result = expression(wtok, variables)
    
    while wtok.get_current() == '=': #Checks if we are doing an assignment
        wtok.next()
        varname = wtok.get_current()
        
        if wtok.is_name():
            wtok.next()
            variables[varname] = result #saves or updates the variable

        else:
            raise SyntaxError('Expected varname after "="')
    
    return result


def expression(wtok, variables):
    
    result = term(wtok, variables)
    
    while wtok.get_current() in ('+','-'):#Checks for addition and subtraction 
        
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)#does the addition
        
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)#Does the subtraction
        
    return result


def term(wtok, variables):
    
    result = factor(wtok, variables)
    while wtok.get_current() in ('*','/'):#Multiplication and division is taken care of here
        
        if wtok.get_current() == '*': 
            wtok.next()
            result = result * factor(wtok, variables)
            
        elif wtok.get_current() == '/':
            wtok.next()
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError('Can not divide by zero')
        
    return result

def factor(wtok, variables):
    #Two dictionaries for the functions the calculator can do.
    function_1 = {'sin' : math.sin, 'cos' : math.cos, 'fac' : fac, 'log' : log, 'exp' : math.exp}
    function_N = {'max' : max, 'sum' : sum, 'avg' : avg}
    
    if wtok.get_current() == '(':#Checks for parenthesis and sends the rest of the expression back to assignment
        wtok.next()
        result = assignment(wtok, variables)
    
        wtok.next()
            
    elif wtok.is_number():#If we have a number it gets returned as a float
        result = float(wtok.get_current())
        wtok.next()
        
    elif wtok.is_name():#If we have a name it could be a variable or a function
        
        if wtok.get_current() in variables:# If it is a variable we return the variable
            
            result = float(variables[wtok.get_current()])
            wtok.next()
            
        elif wtok.get_current() in function_1:#If it is a function with one argument we execute that function
            
            func = wtok.get_current()
            wtok.next()
            
            if wtok.get_current() != '(':
                raise SyntaxError('Expected "("')    
            wtok.next()
            
            result = function_1[func](assignment(wtok, variables))
            wtok.next()
            
        elif wtok.get_current() in function_N:#If it is a function with more than one argument we execute that
            
            func = wtok.get_current()
            wtok.next()
            
            result = function_N[func](arglist(wtok, variables))#Using arglist to get the a list of arguments
            
        else:
            raise EvaluationError('Undefined name')
        
    elif wtok.get_current() == '-':#This takes care of negative numbers
        wtok.next()
        return -factor(wtok, variables)    
        
    else:
        raise SyntaxError("Expected number, variable or '('")  
    return result

def arglist(wtok, variables):#Loops through the tokens inside the parenthesis of a function and returns a list of the arguments
    if wtok.get_current() != '(':
        raise SyntaxError('Expected "("')
    wtok.next()
    
    args = []
    
    while True:
        arg = assignment(wtok, variables)
        args.append(arg)
        
        if wtok.get_current() == ')':
            wtok.next()
            break
        if wtok.get_current() != ',':
            raise SyntaxError('Expected "," or ")"')
        wtok.next()
    return args

def print_variables(variables):#Just a helper function to print the variables in a nice way
    for key in variables:
        print(key + ' = '  + str(variables[key]))


def main():
    print("Numerical calculator")
    
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print_variables(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
                
            except EvaluationError as ee:#Evaluation Error except modeled after the syntax error except
                print("*** Evaluation error: ", ee)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")


if __name__ == "__main__":
    main()
