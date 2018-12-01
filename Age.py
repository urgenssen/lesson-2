age = input("How old are you?  ")
age = int(age)
def age_determination(age):
    if (age<6)&(age>=3):
        conclusion = "You are studying in the kindergarten"
    elif (age>0)&(age<3):
        conclusion = "You are staying at home with your mom"
    elif (age<=0):
        conclusion = "Erroneous value"
    elif (age>=6)&(age<=16):
        conclusion = "You are studying in the school"
    elif (age>16)&(age<=21):
        conclusion = "You are studying in the university"
    elif (age>21)&(age<=80):
        conclusion = "You are working"
    elif (age>80)&(age<=100):
        conclusion = "You are pensioner"
    elif (age>100):
        conclusion = "You are immortal"        
    return conclusion

example = age_determination(age)
print (example)


