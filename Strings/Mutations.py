def mutate_string(string, position, character):
    return ''.join(list(string)[0:position]+list(character)+list(string)[position+1:])

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
