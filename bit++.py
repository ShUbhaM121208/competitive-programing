def bit_language(n, statements):
    x = 0
    for statement in statements:
        if '++' in statement:
            x += 1
        elif '--' in statement:
            x -= 1
    return x

# Input Reading
n = int(input())  # Number of statements
statements = [input().strip() for _ in range(n)]

# Output the final value of x
print(bit_language(n, statements))
