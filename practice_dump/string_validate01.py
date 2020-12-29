k='qA2'
for test in ('.isalnum()','.isalpha()','.isdigit()','.islower()','.isupper()'):
    print(any([eval("i"+test) for i in k]))
