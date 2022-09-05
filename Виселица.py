from tkinter import *
from tkinter import messagebox as mb
import random as r
import os

words = "Ноутбук Бобёр Симсик Лошадь Коалиция Фотосинтез Олиголецитальная Желток Эмбриогенез ЛиттлеБиг БигБон Донбас Луганск Общага Университет Пересдача Комиссия Плотонгенко Ивашко Вершинина Искандер Семихин Семихина Цыганова Елифанов Воробьёва Москва Оогенез Сперматогенез Седло  Уздечка Компиляция Класс Аудитория Массаж Оксимерон ГородППодошвой ФатаМоргана ТамГдеНасНет Реп Пирокинезис Элли Элизиум Поляночь Кадуцей Энигма Автор Абзац Аудитория Балл Беседа Библиотека Вариант Ведомость Век Внимание Вопрос Время Выбор Выпускник Газета Город Государство Грамматика Диалог Диктант Диплом Задание Закон Замена Занятие Информация Лингвистика Книга Конспект Каникулы Кафедра Культура Литература Наука Общество Оценка Ошибка Память Пересказ Пример Ребёнок Дом Еда Радость Любовь Сила Кино Регистрация Восстановление Замечание Погода Мороз Дождь Боль Клавиатура Компьютер Календарь Освещение Коридор Автомобиль Гитара Алкоголь Леопард Антилопа Пальма Великобритания Австралия Италия Мороженое Колесо Карусель Помидор Огурец Перец Дисциплина Торможение Плакат Водоворот Абонемент Аксессуар Альпинист Активация Аналитика Балалайка Баловство Баррикада Баскетбол Волейбол Блондинка Бутерброд Бриллиант Велосипед Восстание Галактика Голодовка Жаворонок Завещание Заработок Инвентарь Интеллект Искусство Контейнер Континент Коробка Медитация Молодость Наручники Население Насекомое Начальник Невидимка Одолжение Репетиция Санаторий Сообщение Спортсмен Стоимость Сценарист Телефон Террорист Удивление Умножение Деление Сложение Вычитание Философия Храбрость Черепаха Шашлык Шахматы Шоколад".lower().split(" ")
translate = {"q":"й", "w":"ц", "e":"у", "r":"к", "t":"е", "y":"н", "u":"г", "i":"ш", "o":"щ", "p":"з", "bracketleft":"х", "bracketright":"ъ", "a":"ф", "s":"ы", "d":"в", "f":"а", "g":"п", "h":"р", "j":"о", "k":"л", "l":"д", "semicolon":"ж", "quoteright":"э", "z":"я", "x":"ч", "c":"с", "v":"м", "b":"и", "n":"т", "m":"ь", "comma":"б", "period":"ю", "quoteleft":"ё"}

word = r.choice(words)
lettering = word
main_text = (" _"*len(word))[1:]
letters = []
attempt = int(12 - len(word)/2)
print(word)

root = Tk()
root.title("Виселица")
root.geometry("500x130")
root.resizable(False, False)
root['bg'] = "gray20"

def updater():
    global word, lettering, main_text, letters, attempt
    word = r.choice(words)
    lettering = word
    main_text = (" _"*len(word))[1:]
    letters = []
    attempt = int(15 - len(word)/2)
    print(word)

    wording['text'] = main_text
    letters_lbl['text'] = letters
    attempts['text'] = "Оставшиеся ошибки: " + str(attempt)
    root.update()

def checker(event):
    global main_text, word, attempt
    if event.keysym not in translate.keys():
        return
    letter = translate[event.keysym]
    if letter in word:
        for i in range(len(word)):
            ind = word.index(letter)
            main_text = main_text[:ind*2] + letter + main_text[ind*2+1:]
            wording['text'] = main_text
            word = word[:ind] + "`" + word[ind+1:]
            if letter not in word:
                break
        if word == "`"*len(word):
            answer = mb.askquestion("Вы выжили!", "Желаете сыграть ещё?")
            if answer == "yes":
                updater()
            else:
                root.destroy()
    else:
        if letter not in letters and letter not in lettering:
            letters.append(letter)
            letters_lbl['text'] = ", ".join(letters)
            attempt -= 1
            attempts['text'] = "Оставшиеся ошибки: " + str(attempt)
            if attempt == 0:
                answer = mb.askquestion("Вы повешаны!", f"Правильным словом было \"{lettering}\"\nЖелаете воскреснуть и сыграть ещё?")
                if answer == "yes":
                    updater()
                else:
                    root.destroy()

    print(word)


wording = Label(root, text = main_text, bg = "gray20", fg = "yellow", font = "Intro 20 bold italic")
letters_lbl = Label(root, text = letters, bg = "gray20", fg = "red", font = "Intro 12 italic")
attempts = Label(root, text = "Оставшиеся ошибки: " + str(attempt), bg = "gray20", fg = "gray80", font = "Intro 15 italic")

wording.pack(pady = 5)
letters_lbl.pack(pady = 5)
attempts.pack()

root.bind("<KeyPress>", checker)

root.mainloop()
