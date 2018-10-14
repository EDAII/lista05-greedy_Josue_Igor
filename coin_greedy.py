import math
coins = list()
bank_note = list()


def register_coins():
    print("Digita as moedas do seu sistema monetario")
    coin = 300
    while coin!=0:
        coin = int(input())
        if isinstance(coin,int) and coin !=0:
            coins.append(coin)
        else:
            break
def register_notes():
    print("Digita as notas do seu sistema monetario")
    note = 300
    while note!=0:
        note = int(input())
        if isinstance(note,int) and note!=0:
            bank_note.append(note)
        else:
            break
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
    register_coins()
    register_notes()
    money_value = float(input("Insira o valor em reais: "))
    split_integer_decimal = math.modf(money_value)
    decimal = round(split_integer_decimal[0], 2)*100

    integer = math.floor(money_value)
    decimal_to_int = math.floor(decimal)


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
