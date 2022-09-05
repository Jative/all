import requests
from bs4 import BeautifulSoup

parsed = "-"*60+"\n\n"

def parser():
    global parsed
    iteration = 0
    i = 0
    while True:
        i += 1
        print(f"Страница {i}...")
        url = f"https://kwork.ru/projects?c=41&page={i}"

        q = requests.get(url)
        result = q.content
        soup = BeautifulSoup(result, "lxml")
        tasks = soup.find_all(class_="d-flex relative")
        if tasks == []:
            return
        for task in tasks:
            try:
                title_class_name = "wants-card__header-title first-letter breakwords pr250"
                task_name = task.find(class_=title_class_name).text
            except:
                title_class_name = "wants-card__header-title first-letter breakwords pr200"
                task_name = task.find(class_=title_class_name).text
            finally:
                parsed += task_name + "\n\n"
                try:
                    task_description = task.find(class_="breakwords first-letter js-want-block-toggle js-want-block-toggle-full hidden").text[:-7]
                    parsed += task_description + "\n\n"
                except:
                    pass
                href = str(task.find(class_=title_class_name)).split("><")[1][8:-(5+len(task_name))]
                want_price = task.find(class_="wants-card__header-price wants-card__price m-hidden").text

                #print(task_name+"\n", task_description+"\n\n")
                #print(want_price)
                parsed += want_price + "\n"
                try:
                    max_price = task.find(class_="wants-card__description-higher-price").text
                    #print(max_price)
                    parsed += max_price + "\n\n"
                except:
                    parsed += "\n"

                #print(href)
                parsed += href + "\n\n" + "-"*60 + "\n\n"
            iteration += 1
            print(f"Обработан {iteration} проект")

def main():
    parser()
    with open("kwork_parsed.txt", "w", encoding="utf-8") as file:
        file.write(parsed)
        file.close()
    print("Завершено успешно!")
    input()

if __name__ == "__main__":
    main()