
# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def output_txt():
    with open("data.txt", "r", encoding="utf-8") as file:
        book = file.read().split("\n")
    return book


def write_txt():
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{input('enter txt: ')}")

def find_person(func):
    text=input("enter person: ")
    for i in func:
        if text in i:
            print(i)
    


def change_delete_replace_addfile(arr):
    text=input("enter text: ")
    for i in range(len(arr)):
        if text in arr[i]:
            b = arr[i].replace(text,input("enter replace_text:"))
            arr.pop(i)
            arr.insert(i,b)
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write('\n'.join(arr))
    return arr
    

while True:
    mode = input(   '\n 1. Программа должна выводить данные'
                    '\n 2. Программа должна сохранять данные в текстовом файле'
                    '\n 3. Пользователь может ввести одну из характеристик для поиска'
                    '\n 4. Пользователь также может ввести имя или фамилию'
                    '\n Выберите режим работы справочник: ')
    if mode == "1":
        print(output_txt())
    elif mode=="2":
        write_txt()
    elif mode=="3":
        find_person(output_txt())
    elif mode=="4":
        change_delete_replace_addfile(output_txt())
    elif mode == "0":
        break
    else:
        print("No mode")