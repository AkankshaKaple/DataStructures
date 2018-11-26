# Simple Balanced Parentheses : This program checks if the expression is balanced or not


class BalancedParenthesis:

    def balanced_method(f_expression):
        parentheses_stack = []
        flag = 0
        if len(f_expression) > 0:
            for iterating_element in range(0, len(f_expression)):
                if f_expression[iterating_element] == '(':
                    parentheses_stack.append(f_expression[iterating_element])
                    flag = 1
                elif f_expression[iterating_element] == ")":
                    try:
                        parentheses_stack.pop()
                        flag = 1   
                    except:
                        print("( is missing")
                        flag = 0
            if parentheses_stack == []:  # if stack is empty then check if flag is 0 or 1
                if flag == 1:
                    print("Expression is balanced")
                else:
                    print("Expression is unbalanced")
            else:
                print("Expression is unbalanced")
            return
        else:
            print("Invalid input")


    g_expression = list(input("Enter string : "))  # Convert the expression into a
# list of characters
    balanced_method(g_expression)