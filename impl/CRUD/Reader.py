import json

class Reader:
    def __init__(self) -> None:
        pass

    def readFile(self) -> dict:
        notes = {}
        try:
            with open('data.json') as json_file:
                notes = json.load(json_file)
        except FileNotFoundError:
            print("\033[33m", "Внимание: Будет создан новый файл\n","\033[37m")
        return notes

    def readAllNotes(self, notes: dict) -> None:

        keys = list(notes.keys())

        for k in keys:
            print("\nЗаметка №" + k)
            for n in notes[k]:
                print('Title: ' + n['Title'])
                print('Body: ' + n['Body'])
                print('Time: ' + n['Time'] + "\n")
    
    def readNote(self, notes: dict) -> None:
        keys = list(notes.keys())
        id = input("Введите идентификатор заметки: ")
        if id in keys:
            print("\nЗаметка №" + id)
            for n in notes[id]:
                print('Title: ' + n['Title'])
                print('Body: ' + n['Body'])
                print('Time: ' + n['Time'] + "\n")
        else:
            print("\033[31m", "Введен несуществующий идентификатор! ", "\033[37m")
