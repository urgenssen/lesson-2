
def get_answer():
    while True:
        get_answer_1 = (input("Ask your question: ")).lower()
        if get_answer_1 == "bye":
            print ("Bye")
            break
        else:
            print("What is {}".format(get_answer_1))


def ask_user():
    while True:
        ask_user_1 = (input("How do you do? ")).lower()
        if ask_user_1 == "good":
            print ("bye")
            break
        else:
            get_answer()
            break

example = ask_user()

