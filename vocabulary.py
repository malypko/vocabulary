import os

def clear_screen():
    os.system('cls')

while True:
    clear_screen()
    print("Добро пожаловать в словарь")
    print("=== МЕНЮ ===")
    print("1. Открыть весь словарь")
    print("2. Добавить слово в словарь")
    print("3. Закрыть словарь")
    menu = input("# Введите номер меню: ")
    #print(menu)
    if menu == "1":
        print ("\n")
        print("=== СЛОВАРЬ ====")
        with open("vocabulary.txt", "r", encoding="utf-8") as f:
            print(f.read())
        print("*** КОНЕЦ СЛОВАРЯ ***")
        input("Нажмите любую клавишу, чтобы выйти в меню")
    elif menu == "2":
        clear_screen()
        print("*** Добавляем новое слово в словарь ***")
        english_word = input("Введите новое английское слово: ")
        russian_word = input("Введите его перевод на русский: ")
        new_words = english_word + " " + russian_word
        with open("vocabulary.txt", "a", encoding="utf-8") as f:
            print(new_words, file=f)
        #f.close()            
    elif menu == "3":
        print("Спасибо за использование СЛОВАРЯ")
        break
    else:
        clear_screen()
        f.close



