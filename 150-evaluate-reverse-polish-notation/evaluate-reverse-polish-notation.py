from collections import deque

# Start parse
# Base case: If you read in two integer then an operator:
#   Perform op
#   Return result as new lefthand
# Recursive case: If you read in two integer then an integer:
#   "Remember" lefthand (=the first integer)
#   Start a new parse w/ lh = second int, rh = third int
#   New lefthand = result of parse, next operator will be at startIdx + (# times compressed) + 2
#
#     3 3 4 + *
# 1 2 + 3 4 + *
#
# 1     3     +   cmpr = 2
# 1 1   2   + +   cmpr = 1
# 1 1 1 1 + + +   cmpr = 0
#
# 111++

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {'+', '-', '*', '/'}

        def operate(operand1: int, operand2: int, operator: chr):
            if operator == '+':
                return operand1 + operand2
            if operator == '-':
                return operand1 - operand2
            if operator == '*':
                return operand1 * operand2
            if operator == '/':
                return int(operand1 / operand2)

        dk = deque()
        for tk in tokens:
            
            if tk in operators:
                result = operate(operand2=dk.pop(), operand1=dk.pop(), operator=tk)
                dk.append(result)
            else:
                dk.append(int(tk))
        
        return dk.pop()

# 10 6 9 3 + -11 * / * 17 + 5 +
# 10 6 9 3 +
# 10 6 12    -11 *
# 10 6 -132        /
# 10 0               *
# 0                    17 +
# 17                        5 +
# 22