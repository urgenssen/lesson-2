my_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name = "Empty"
while name!="Валера":
    name = my_list.pop()
    if name == "Валера":
        print (name + " нашелся")
        break


