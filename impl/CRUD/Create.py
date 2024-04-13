from impl.Note import NewNote as Note

class CreateNote:
    
    def __init__(self) -> None:
        pass
    
    def addNote(self, notes: dict) -> dict:
        
        note = Note()
        note.setNoteParam()
        if note.getId() in list(notes.keys()):
            print("\033[31m","\nЗаметка с таким идентификатором уже существует!\n", "\033[37m")
            flag = True
            while flag == True:
                
                move = input("Выберите действие\n"
                        "1. Перезаписать заметку\n"
                         "2. Изменить идентификатор\n"
                         "3. Не создавать заметки\n")
                if move.isdigit():
                    move = int(move)
                    
                    if move == 1:
                        del notes[note.getId()]
                        notes[note.getId()] = []
                        notes[note.getId()].append({
                        'Title': note.getTitle(),
                        'Body': note.getBody(),
                        'Time': note.getTime(),
                        })
                        print("\033[32m","\nЗаметка успешно перезаписана!\n", "\033[37m")
                        flag = False
                    elif move == 2:
                        note.setId()
                        while (note.getId() in list(notes.keys())) == True:
                            print("\033[31m","\nЗаметка с таким идентификатором тоже существует!\n", "\033[37m")
                            note.setId()

                        notes[note.getId()] = []
                        notes[note.getId()].append({
                            'Title': note.getTitle(),
                            'Body': note.getBody(),
                            'Time': note.getTime(),
                            })
                        print("\033[32m","\nЗаметка успешно создана!\n", "\033[37m")
                        flag = False
                    elif move == 3:
                        print("\n")
                        flag = False
                    else:
                        print("\033[31m", "\nВведена невалидная команда!\n", "\033[37m")
                else:
                    print("\033[31m", "\nВведен недопустимый символ!\n", "\033[37m")
        else:
            notes[note.getId()] = []
            notes[note.getId()].append({
                        'Title': note.getTitle(),
                        'Body': note.getBody(),
                        'Time': note.getTime(),
                        })
            print("\033[32m","\nЗаметка успешно создана!\n", "\033[37m")
        return notes