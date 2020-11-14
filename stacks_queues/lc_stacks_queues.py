import string

def calculate(s: str) -> int:
    expression = '(' + s.replace(' ', '') + ')'

    stack = []

    curr_val = 0
    curr_multiplier = 1

    for ch in reversed(expression):
        if ch == ')':
            if curr_val:
                stack.append(curr_val)
                curr_val, curr_multiplier = 0, 1
            stack.append(ch)
        elif ch == '(':
            if curr_val:
                stack.append(curr_val)
                curr_val, curr_multiplier = 0, 1
            # time to evaluate
            res = 0
            while stack:
                curr = stack.pop()
                if curr == ')':
                    break
                elif curr in ('-', '+'):
                    if curr == '+':
                        res = res + stack.pop()
                    else:
                        res = res - stack.pop()
                else:
                    res = curr

            stack.append(res)

        elif ch in string.digits:
            digit = string.digits.index(ch)
            val = digit * curr_multiplier
            curr_multiplier = curr_multiplier * 10
            curr_val += val
        else:
            # this is an operand
            if curr_val:
                stack.append(curr_val)
                curr_val, curr_multiplier = 0, 1
            stack.append(ch)

    return stack[0]

if __name__ == "__main__":
    # val = calculate('7 - 8 + 9 + 2 + 11')
    val = calculate("(7)-(0)+(4)")
    print(val)