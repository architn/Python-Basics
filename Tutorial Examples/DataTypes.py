# Arithmetic operations in Python

def ArithmeticSample():
    value_1 = 2 ** 4
    value = 2 + 3 * 5 + 5
    print(value_1)


# ArithmeticSample()

# Strings in Python

def StringExamples():
    value = "I cannot go outside"
    num = 12
    name = 'Sam'
    value_1 = "My number is {} and my name is {}" .format(num, name)
    value_2 = "My number is {one} and my name is {two}".format(one=num, two=name)
    s = "Hello I Am Archit"
    # Indexing in Python starts with 0
    firstNumber = s[0]
    slicing = s[2:]
    slicing_1 = s[:3]
    slicing_2 = s[0:4]
    print(slicing_2)


# StringExamples()

# Lists in Python

def ListExamples():
    my_Integers = [1, 2, 3, 4]
    my_StringList = ["Apple", "Orange", "Banana"]
    print(my_Integers)
    print(my_StringList)


# ListExamples()

# Dictionary in Python

def DictionaryExamples():
    dictionary_var = {'Apple': 'OSX', 'Microsoft': 'Windows 10'}
    dictionary_list = {"Apple": ["MacBook Air", "MacBook Pro"], "Microsoft": ["HP", "Dell"]}
    dictionary_nested = {"k1": {"innerkey": [1, 2, 3]}}
    # print(dictionary_list['Microsoft'][1])
    print(dictionary_nested["k1"]["innerkey"][2])


# DictionaryExamples()

# Tuples in Python: Immutable (cannot change sequence of objects in Tuple)

def TupleExamples():
    tuple_list = (0, 1, 2, 3)
    print(tuple_list)


# TupleExamples()

# Sets in Python: A representation of unique elements

def SetExample():
    set_list = {1, 1, 1, 2, 2, 3, 3, 5, 5, 6, 6}
    print(set_list)


# SetExample()

# String functions in Python

def BuiltInStringFunctionExample():
    exampleString = "My name is Sam"
    upperCaseString = exampleString.capitalize()
    print(upperCaseString)
    splitString = exampleString.split()
    print(splitString)
    tweet = "Go Sports! #Sports"
    hashtag = tweet.split("#")[1]
    print(hashtag)


# BuiltInStringFunctionExample()


# Tuple Unpacking in Python

def TupleUnpackingExample():
    x = [(1, 2), (3, 4), (5, 6)]
    for a, b in x:
        print(a)


TupleUnpackingExample()
