import csv

def selection_sort(list_number):
    size_list = len(list_number)
    for i in range(0,size_list):
        current = list_number[i]
        min_value =  min(list_number[i:])
        min_value_index = list_number.index(min(list_number[i:]))
        if current != min_value :
            list_number[i], list_number[min_value_index] = list_number[min_value_index] , list_number[i]
    return list_number

def find_platform_avaliable(arrival_time, departure_time, amount_bus_arrived):

    selection_sort(arrival_time)
    selection_sort(departure_time)

    i = 1
    j = 0
    result = 1
    number_plataform_needed = 1

    while (i < amount_bus_arrived and j < amount_bus_arrived):

        if (arrival_time[i] < departure_time[j]):
            number_plataform_needed+=1
            i+=1

            if (number_plataform_needed > result):
                result = number_plataform_needed

        else:
            number_plataform_needed-=1
            j+=1

    return result

def convert_list_to_int(time_list):
    list_coverted = list(map(int, time_list))
    return list_coverted

dados = {}
with open("bus_schedule.csv") as arquivocsv:
    ler = csv.DictReader(arquivocsv, delimiter=",")
    for linha in ler:
        for chave, valor in linha.items():
            if chave not in dados:
                 dados[chave] = []
            dados[chave].append(valor)

arrive = convert_list_to_int(dados['hora_chegada'])
departure = convert_list_to_int(dados['hora_partida'])

length = len(dados['hora_chegada'])

print("Numero minimo de plataformas necessario = ", find_platform_avaliable(arrive, departure, length))
