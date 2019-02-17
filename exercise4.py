def main():
    firstnum = str(input("Εισάγετε τον πρώτο αριθμό(zero-nine): ")).lower()
    praxi = str(input("Εισάγετε την επιθυμητή πράξη(plus, minus, times, divided): ")).lower()
    secondnum = str(input("Εισάγετε τον δεύτερο αριθμό(zero-nine): ")).lower()
    number1 = fnum(firstnum, turn = 1)
    number2 = fnum(secondnum, turn = 2)
    fcalc(praxi, number1, number2)
def fnum(x, turn):
    if x == "one":
        retnum = fone()
    elif x == "two":
        retnum = ftwo()
    elif x == "three":
        retnum = fthree()
    elif x == "four":
        retnum = ffour()
    elif x == "five":
        retnum = ffive()
    elif x == "six":
        retnum = fsix()
    elif x == "seven":
        retnum = fseven()
    elif x == "eight":
        retnum = feight()
    elif x == "nine":
        retnum = fnine()
    elif x == "zero":
        retnum = fzero()
    return retnum
def fone():
    num = 1
    return num
def ftwo():
    num = 2
    return num
def fthree():
    num = 3
    return num
def ffour():
    num = 4
    return num
def ffive():
    num = 5
    return num
def fsix():
    num = 6
    return num
def fseven():
    num = 7
    return num
def feight():
    num = 8
    return num
def fnine():
    num = 9
    return num
def fzero():
    num = 0
    return num
def fcalc(praxis, num1, num2):
    if praxis == "times":
        result = num1*num2
        print ("\nΤο αποτέλεσμα της πράξης είναι: ", result)
    elif praxis == "plus":
        result = num1+num2
        print ("\nΤο αποτέλεσμα της πράξης είναι: ", result)
    elif praxis == "minus":
        result = num1-num2
        print ("\nΤο αποτέλεσμα της πράξης είναι: ", result)
    elif praxis == "divided":
        try:
            result = num1//num2
            print ("\nΤο αποτέλεσμα της πράξης είναι: ", result)
        except ZeroDivisionError:
            print ("\nΔέν είναι δυνατή η διαίρεση με το 0.")
main()
