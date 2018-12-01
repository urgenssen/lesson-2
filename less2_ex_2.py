my_list = []
a = 0

while a<5:
    my_list.append(input("Write name: "))
    a+=1  
name = my_list[1]  


def find_person(name):
    value = "Без имени"
    while value != name: 
        value = my_list.pop()
        if value == name:
            return (name + " is found")
            break
        elif my_list == []:
            return (name + " is not found")
            break
    

example = find_person("Ян")
print (example)
