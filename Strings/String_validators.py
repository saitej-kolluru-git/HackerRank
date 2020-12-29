if __name__ == '__main__':
    k = input()
    for test in ('.isalnum()','.isalpha()','.isdigit()','.islower()','.isupper()'):
        print(any([eval("i"+test) for i in k]))
