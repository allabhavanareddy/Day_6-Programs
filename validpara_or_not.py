def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')' and stack:
            stack.pop()
        else:
            return False
    return not stack

def generate_correct_parentheses(s):
    def backtrack(current, remaining):
        if not remaining:
            if is_valid_parentheses(current):
                balanced_parentheses.append(current)
            return

        backtrack(current + '(', remaining - 1)
        backtrack(current + ')', remaining - 1)

    balanced_parentheses = []
    n = len(s)
    backtrack('', n)
    return balanced_parentheses

# Input the string with parentheses
input_string = input("Enter a string with parentheses: ")

if is_valid_parentheses(input_string):
    result = generate_correct_parentheses(input_string)
    if result:
        print("True")
        #print("Corrected Balanced Parentheses:")
        #for parentheses in result:
            #print(parentheses)
    #else:
        #print("False")
else:
    print("The given parentheses are not valid.")
