import random
for i in range(4):

    lives = 10
    word = ("cat", "dog","hamster","blue")
    choice = random.randint(0, len(word) - 1)
    new_word = word[choice]

    long = len(new_word)

    what = long * "_"
    print("Загадоннае слово:", what)

    while (lives > 0) and ("_" in what):
        iput = input("Введите букву: ")
        if (iput in new_word) and (iput != ""):
             location = new_word.find(iput)
             what = what[:location] + iput + what[location + 1:]
             print(what)
        else:
            lives-=1
            print("Давай заново, осталось", lives ,"жизней")

    if lives == 0:
        print("В следующий раз!")
    else:
        print("Ты смог, поздравляю!")
