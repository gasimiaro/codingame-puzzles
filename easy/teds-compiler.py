#https://www.codingame.com/ide/puzzle/teds-compiler

def longest_valid_prefix(expression):
    stack = []
    max_length = 0
    current_length = 0

    for char in expression:
        if char == '<':
            stack.append(char)
            current_length += 1
        elif char == '>':
            if stack and stack[-1] == '<':
                stack.pop()
                current_length += 1
                if not stack:
                    max_length = current_length
            else:
                break

    return max_length

# Read input
expression = input().strip()

# Calculate and print the length of the longest valid prefix
result = longest_valid_prefix(expression)
print(result)