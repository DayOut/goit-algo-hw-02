from collections import deque

def check_palindrome(s):
    sanitized = ''.join(symbol.lower() for symbol in s if symbol.isalnum())
    queue = deque(sanitized)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

test_strings = [
    "A man a plan a canal Panama",
    "No lemon, no melon",
    "Hello World",
    "Was it a car or a cat I saw",
    "Madam In Eden I'm Adam"
]

for s in test_strings:
    result = check_palindrome(s)
    print(f'"{s}" is a palindrome: {result}')