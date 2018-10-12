import math
coins = [1, 5, 10, 25, 50]
bank_note = [1, 2, 5, 10, 20, 50, 100]

def calc_change_real(integer):
    answer_int = list()
    for money in reversed(bank_note):
        while integer >= money:
            integer -= money
            answer_int.append(money)

    return answer_int

def calc_change_coin(decimal):
    answer_dec = list()
    for coin in reversed(coins):
        while decimal >= coin:
            decimal -= coin
            answer_dec.append(coin)

    return answer_dec

def main():
    money_value = float(input("Insira um numero: "))
    split_integer_decimal = math.modf(money_value)
    decimal = round(split_integer_decimal[0], 2)*100

    integer = math.floor(money_value)
    decimal_to_int = math.floor(decimal)

    # print("Inteiro", integer)
    # print("decimal", decimal_to_int)

    solution_integer = calc_change_real(integer)
    solution_decimal = calc_change_coin(decimal_to_int)

    print("\n")
    i = 0
    for element in solution_integer:
        print((str(element) + 'R'), end=' ')
        i+=1
    print("\nTotal de Notas:", i)
    print("\n")

    j = 0
    for element in solution_decimal:
        print((str(element) + 'C'), end=' ')
        j+=1
    print("\nTotal de Moedas:", j)
    print("\n")

if __name__ == '__main__':
    main()
