def tokenization(expression):

    # 1. Remove Spaces from expression | expression is a string
    # 2. isDigit() -> tell if we have a digit or not

    tokens = []

    for i in range(0, len(expression)):
        # Cook Your Dish Here
        tokens.append(expression[i])

    return tokens


def simpleEvaluation(expression):

    result = 0.0
    operators = ['^', '/', '*', '-', '+']
    expression = [2, "+", 3, "*", 4, "^", 2, "+", 1]
    for i in range(0, len(operators)):

        j = 0
        k = len(expression)

        while j < k:
            if expression[j] == operators[i]:

                if i is 0:
                    result =  (float(expression[j-1]) ** float(expression[j+1]))
                elif i is 1:
                    result = (float(expression[j - 1]) / float(expression[j + 1]))
                elif i is 2:
                    result = (float(expression[j - 1]) * float(expression[j + 1]))
                elif i is 3:
                    result = (float(expression[j - 1]) - float(expression[j + 1]))
                elif i is 4:
                    result = (float(expression[j - 1]) + float(expression[j + 1]))

                expression[j-1] = result
                expression.pop(j)
                expression.pop(j)
                k = len(expression)
                j = 0

            j = j + 1

    return result


expression1 = "(3 + 66 * 2 ^ 22) * (2 - 1)"
expression2 = "(3.19 + 66 * 2 ^ 22.578) * (2 - 1)"
tokens = tokenization(expression1)
print(tokens)

"""
num = "57"
print(num.isdigit())

num = "8"
fNum = float(num)
print(fNum)
"""

exp = 2.2 + 5 * 7 -3
print(exp)
