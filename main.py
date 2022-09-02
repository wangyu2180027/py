import package1.calc as calc
from package1.calc import add as a, minus
from package1.calc2 import add
from package1.calc2 import minus as b

def main():
    result = a(1, 2) #calc.py add
    result2 = calc.minus(5,3) #calc.py minus
    print(result)
    print(result2)

    result3 = add(5,1) #calc2.py add
    print(result3)

    result4 = b(8,4) #calc2.py minus
    print(result4)

if __name__ == '__main__':
    main()