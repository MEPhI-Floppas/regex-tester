import exrex
import re


# def main():
#     i = 0
#     for test in exrex.generate(r'(a|b*)(ab)*|([ab])*b', 10):
#         if re.match(r'^a(b*a+b)*b*|b(b*a+b)*b*|$', test) is None:
#             print(test)
#             print('Not matched')
#         i += 1
#     print(i)


def main():
    i = 0
    for test in exrex.generate(r'a(b*a+b)*b*|b(b*a+b)*b*|', 5):
        if re.match(r'^(a|b*)(ab)*|([ab])*b$', test) is None:
            print(test)
            print('Not matched')
        i += 1
    print(i)


if __name__ == '__main__':
    main()
