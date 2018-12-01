school_1 = [{'school_class': '5a', 'scores': [5,5,5,3,3,4]}, {'school_class': '5b', 'scores': [1,1,1]},
{'school_class': '5v', 'scores': [5,4,5,5,5]}, {'school_class': '5g', 'scores': [3,2,2,4]}]
a = 0
b = 0
c = 0
for number_dic in school_1:
    scores = number_dic.get("scores")
    a = a + len(scores)
    for value in scores:
        b = b + value
print ("Средняя оценка по школе: " + str(round(float(b/a),1)))

for number_dic_1 in school_1:
    scores_1 = number_dic_1.get("scores")
    d = len(scores_1)
    c = 0
    for value_1 in scores_1:
        c = c + value_1
    print ("Средняя оценка класса " + number_dic_1.get("school_class")+ " : " + str(round(float(c/d),1)))

        
