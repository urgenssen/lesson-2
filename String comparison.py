
def input_text():
    string_1 = input()
    string_2 = input()
    if (type(string_1) is str) & (type(string_2) is str):
        if string_1 == string_2:
            conclusion = 1
        elif (string_1 != string_2) & (len(string_1)>len(string_2)) & (string_2 == "learn"):
            conclusion = 4   # дополнительное условие (см. ниже)
        elif (string_1 != string_2) & (len(string_1)>len(string_2)):
            conclusion = 2
        elif (string_1 != string_2) & (string_2 == "learn"):
            conclusion = 3
        else:
            return None # если сторая строка длинее первой
    else:
        conclusion = 0
    return conclusion

for example in range(4):  # проверка для нескольких значений
    example = input_text()
    print(example)
    
# input() всегда преобразует данные в строковый тип, так что conclusion = 0 никогда не произойдёт
# Есть 2 условия, которые могут быть выплненны одновременно:
# Строки не равны друг другу, первая строка длиннее второй, а вторая строка может быть "learn", какое значение примет функция?
