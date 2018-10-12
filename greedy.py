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
    # arrival_time.sort()
    # departure_time.sort()
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

arrive = [1100, 940, 859,950, 900, 1500, 1800]
departure = [1110, 1200, 1300, 1120, 1130, 1900, 2000]
length = len(arrive)

print("Numero minimo de plataformas necessario = ", find_platform_avaliable(arrive, departure, length))
print("horario chegada: ", arrive)
print("horario saida", departure)
