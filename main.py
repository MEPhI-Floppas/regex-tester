import exrex
import re

a = r'^(ab*)(ab*)*|([ba])*b$'
b = r'^a([ab])*|b|b([ab]*b)$'


def main():
    i = 0
    for test in exrex.generate(b, 6):
        if re.match(a, test) is None:
            print(test)
            print('Not matched')
        i += 1
        if i == 1000000:
            break
    print(i)


# def main():
#     i = 0
#     for test in exrex.generate(r'b[a|b]*b|b|a(a|b[a|b]*)', 10):
#         if re.match(r'^(ab*)(ab*)*|([b|a])*b$', test) is None:
#             print(test)
#             print('Not matched')
#         i += 1
#     print(i)

h
if __name__ == '__main__':
    main()
