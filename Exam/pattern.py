def pattern1():
    for i in range(4):
        for j in range(i):
            print(i,end="")
        print()

def pattern2(strings):
    for string in strings:
        print(string)


strings = ['a', 'bb', 'ccc']
pattern1()
pattern2(strings)

