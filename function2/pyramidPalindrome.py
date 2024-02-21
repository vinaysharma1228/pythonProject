def generate_palindrome(string):
    return string + string[-2::-1]


def pyramid_of_palindromes(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        current_row = generate_palindrome('1' * (2 * i - 1))
        print(spaces + current_row)


pyramid_height = 3
pyramid_of_palindromes(pyramid_height)
