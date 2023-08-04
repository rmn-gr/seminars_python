import re


def apply_operator(a, operator, b):
    a, b = float(a), float(b)
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b


def search_indexes(r_pattern, expression: str):
    operator = re.search(r_pattern, expression).group(0)
    operator_index = expression.index(operator)
    if len(operator) == 2:
        operator_index += 1

    l_i = operator_index - 1
    while (expression[l_i].isdigit() or expression[l_i] == '.') and l_i != 0 and expression[l_i] != '-':
        l_i -= 1
        if not expression[l_i].isdigit() and expression[l_i] != '-' and expression[l_i] != '.':
            l_i += 1
            break

    r_i = operator_index + 1
    if expression[r_i] == '-': r_i += 1
    while (expression[r_i].isdigit() or expression[r_i] == '.') and r_i < len(expression) - 1:
        r_i += 1

    return l_i, r_i


def resolve_expression(expression: str):

    if not re.search(r'\+|\d-|\*|/|\)\+|\)-|\)\*|\)/', expression):
        return expression

    if len(re.split(r'\+|\d-|\*|/', expression)) == 2:
        operator = re.search(r'\+|\d-|\*|/', expression).group()
        operator_index = expression.index(operator)
        if len(operator) == 2:
            operator_index += 1
            operator = operator[1]
        left_num = expression[:operator_index]
        right_num = expression[operator_index+1:]
        result = str(apply_operator(left_num, operator, right_num))
        return result

    while expression.__contains__('('):
        count = 1
        l_i = expression.index('(')
        r_i = l_i + 1
        while count != 0:
            if expression[r_i] == ')':
                count -= 1
            elif expression[r_i] == '(':
                count += 1
            if count == 0:
                break
            r_i += 1
        if r_i + 1 == len(expression) - 1:
            expression = expression[:l_i] + resolve_expression(expression[l_i+1:r_i])
        else:
            expression = expression[:l_i] + resolve_expression(expression[l_i+1:r_i]) + expression[r_i+1:]

    while re.search(r'\*|/', expression):
        l_i, r_i = search_indexes(r'\*|/', expression)
        if r_i == len(expression)-1:
            expression = expression[:l_i] + resolve_expression(expression[l_i:])
        else:
            expression = expression[:l_i] + resolve_expression(expression[l_i:r_i]) + expression[r_i:]

    while re.search(r'\+|\d-', expression):
        expression = expression.replace('+-', '-').replace('--', '+')
        l_i, r_i = search_indexes(r'\+|\d-', expression)
        if r_i == len(expression) - 1:
            expression = expression[:l_i] + resolve_expression(expression[l_i:])
        else:
            expression = expression[:l_i] + resolve_expression(expression[l_i:r_i]) + expression[r_i:]

    return expression


exp = "-40/-2/((-20+18)*(8/-4)-2)"
print(resolve_expression(exp.replace(' ', '')))


