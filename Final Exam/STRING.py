def count_characters(s):
    return len(s)

def reverse_string(s):
    return s[::-1]

def find_repeated_characters(s):
    repeated = {}
    for char in s:
        if s.count(char) > 1:
            repeated[char] = s.count(char)
    return repeated

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def find_case_and_spaces(s):
    result = {'uppercase': 0, 'lowercase': 0, 'spaces': 0}
    for char in s:
        if char.isupper():
            result['uppercase'] += 1
        elif char.islower():
            result['lowercase'] += 1
        elif char.isspace():
            result['spaces'] += 1
    return result

def main():
    while True:
        print("\nMenu:")
        print("1. Count Characters")
        print("2. Reverse String")
        print("3. Find Repeated Characters")
        print("4. Count Vowels")
        print("5. Find Capitals, Smalls, and Spaces")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting...")
            break

        s = input("Enter a string: ")

        if choice == '1':
            print("Character Count:", count_characters(s))
        elif choice == '2':
            print("Reversed String:", reverse_string(s))
        elif choice == '3':
            repeated_chars = find_repeated_characters(s)
            print("Repeated Characters:", repeated_chars if repeated_chars else "No repeated characters.")
        elif choice == '4':
            print("Vowel Count:", count_vowels(s))
        elif choice == '5':
            case_spaces = find_case_and_spaces(s)
            print(f"Uppercase: {case_spaces['uppercase']}, Lowercase: {case_spaces['lowercase']}, Spaces: {case_spaces['spaces']}")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
def count_characters(s):
    return len(s)

