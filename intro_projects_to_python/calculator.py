'''
Author: Kevin Ramirez
Date: 2/2/26
Program: Calculator.py
Purpose: create a basic calculator
'''
#creating my own exception handling
class InvalidOperatorError(Exception):
    """ raised when user inputs invalid operatand. """
    pass

#creating function for operations
def operations(variable: float, variable2:float, operator:str ):
    '''
    Docstring for operations
    
    :param variable: Description
    :type variable: float
    :param variable2: Description
    :type variable2: float
    :param operator: Description
    :type operator: str
    '''

    try:
        if operator == '/':
            if variable2 == '0':
               raise ZeroDivisionError
            else:
               return variable / variable2
    except ZeroDivisionError as e:
        Error: str = (f'{e} not allowed.')
        return Error.capitalize()

    if operator == '+':
        return variable + variable2
    elif operator == '-':
        return variable - variable2
    elif operator == '*':
        return variable * variable2
    

#creating variable
variable: float = 0
variable2: float = 0
operation: str

#taking users input and applying exception handling
try:
    variable = float(input('Enter number:'))
except ValueError:
    print('Invalid number.')

try:
    operation = input('Enter operation (+, -, /, *, or =): ')
    if(operation != '+' and operation != '-' and operation != '/' and operation != '*'):
        raise InvalidOperatorError(f'Invalid operator {operation}, enter +, -, /, or *') #practicing using raise
except InvalidOperatorError as e:
    print(f'Error: {e}')

try:
    variable2 = float(input('Enter number:'))
except ValueError:
    print('Invalid number.')

result = operations(variable, variable2, operation)
print(result)

#exiting message
print('Exiting....')