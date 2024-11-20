my_list = [ 42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    # создаем цикл если индекс меньше моего листа
    print(my_list[index])
    #то выводиться мой лист
    index += 1
    #прибавляем к индексу 1
    if my_list[index] > 0:
    # если больше 0 то выводим число
        print(my_list[index])
    elif my_list[index] == 0:
    #если равно нулю то начинаем цикл сначала
        continue
    elif my_list[index] < 0 :
    #если число в моем листе меньше нуля то останавливаем цикл
        break





