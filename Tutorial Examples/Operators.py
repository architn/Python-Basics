# Operators in Python

def OperatorExamples():
    # checkIfTrue = (1 > 2) and (2 > 3)
    checkIfTrue = (1 < 2) or (2 < 3)
    print(checkIfTrue)


# OperatorExamples()

# Conditional Operators in Python

def ConditionalOperatorsExamples():
    if 1 == 2:
        print("1 is Equal to 2")
    elif 1 == 3:
        print("Second")
    elif 1 == 4:
        print("Third")
    elif 1 == 5:
        print("Last")
    else:
        print("Default")


# ConditionalOperatorsExamples()

# For Loops in Python

def ForLoopExamples():
    seq = [1, 2, 3, 4, 5, 6]
    # For Loop
    for num in seq:
        print(num)

    for num in range(0, len(seq)-1):
        print(num)

    # List Comprehension Example
    x = [1, 2, 3, 4]
    out = []
    for num in x:
        out.append(num**2)

    print(out)


# ForLoopExamples()

# While Loop in Python

def WhileLoopExample(i):
    """"
    THIS IS A FUNCTION TO DEMONSTRATE WHILE LOOPS IN PYTHON
    """
    while i < 5:
        print("i is: {}".format(i))
        i = i + 1


# WhileLoopExample(1)


# List Comprehensions in Python

def ListComprehensionExample():
    x = [1, 2, 3, 4, 5]
    out = [num ** 2 for num in x]
    print(out)


# ListComprehensionExample()

# Lambda and Map Functions in Python

def times2(var):
    return var*2


def MapExample():
    seq = [1, 2, 3, 4, 5, 6]
    map_variable = list(map(times2, seq))
    # Implemented via Lambda Expressions
    map_variable_1 = list(map(lambda var:  var * 3, seq))
    print(map_variable)
    print(map_variable_1)


# MapExample()

# Filter function in Python

def FilterExample():
    seq = [1, 2, 3, 4, 5]
    list_variable = list(filter(lambda num: num % 2 == 0, seq))
    print(list_variable)


# FilterExample()
