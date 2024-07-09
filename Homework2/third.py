def check_brackets(expression):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return "Несиметрично"

    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3 );",
    "( 11 }"
]

for expr in expressions:
    result = check_brackets(expr)
    print(f"{expr}: {result}")