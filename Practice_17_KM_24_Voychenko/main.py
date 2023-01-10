from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factotial import fact
from logarithm.logarithm import log, lg, ln

def main():
    menu ="""
    1) exp2 - x^2
    2) exp3 - x^3
    3) root2 - x^(1/2)
    4) root3 - x^(1/3)
    5) fact - x!
    6) log - log x base a
    7) lg - log x base 10
    8) ln - log x base e
    """
    choose = [exp2, exp3, root2, root3, fact, log, lg, ln]

    print(menu)

    point = int(input('Виберіть номер функції: '))
    x = input('Введіть x: ')
    if point == 6:
        a = input('Введіть базу логорифма: ')

        print(choose[point-1](a, x))
    else:
        print(choose[point-1](x))

if __name__ == "__main__":
    main()