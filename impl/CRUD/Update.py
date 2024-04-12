import datetime
from impl.Note import NewNote as Note

class UpdateNote:
    
    def __init__(self) -> None:
        pass
    
    def updateNoteByKey(self, notes: dict) -> dict:
        noteKey = input("Введите идентификатор заметки для её изменения: ")
        try:
            Title = notes[noteKey][0]["Title"]
            Body = notes[noteKey][0]["Body"]

            inputTitle = input("Введите новый заголовок: ")
            inputBody = input("Введите новое тело заметки: ")

            if inputTitle != "":
                Title = inputTitle
            
            if inputBody != "":
                Body = inputBody
            
            if inputTitle != "" or inputBody != "":
                notes[noteKey] = []
                notes[noteKey].append({
                    'Title' : Title,
                    'Body' : Body,
                    'Time': datetime.datetime.now().strftime("%c")
                })
                print("\032[31m","\nЗаметка успешно изменена!\n", "\033[37m")
                
        except KeyError:
            print("\033[31m", "Ошибка: Введен несуществующий идентификатор! \n", "\033[37m")
        
        return notes

        