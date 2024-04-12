# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.



from impl.CRUD.Create import CreateNote as Create
from impl.CRUD.Save import SaveAll as SaveAll
from impl.CRUD.Update import UpdateNote as Update
from impl.CRUD.Delete import DeleteNote as Delete
from impl.CRUD.FileRead import FileRead as ReadFile


# Заметки
class View:

    

    def __init__(self):
        print("\nДобро пожаловать в заметчик!\n")

        flag = True
        notes = dict()
        fileRead = ReadFile()
        notes = fileRead.readFile()

        while (flag == True):

            print("1. Новая заметка\n"
              "2. Удалить заметку\n"
              "3. Изменить заметку\n"
              "4. Показать все заметки\n"
              "5. Сохранить заметки в файл\n"
              "6. Выйти из заметчика\n")
            
            command = input("Введите номер команды: ")
            if command.isdigit():
                command = int(command)
                
                if (command == 1):
                    create = Create()
                    notes = create.addNote(notes)
                elif (command == 2):
                    if len(notes) != 0:
                        delete = Delete()
                        notes = delete.deleteNoteByKey(notes)
                    else:
                        print("\033[31m", "Пока нет ни одной заметки! \n","\033[37m")
                elif (command == 3):
                    if len(notes) != 0:
                        update = Update()
                        notes = update.updateNoteByKey(notes)
                    else:
                        print("\033[31m", "Пока нет ни одной заметки! \n", "\033[37m")
                elif (command == 4):
                    if len(notes) != 0:
                        readAll = ReadFile()
                        readAll.readAllNotes(notes)
                    else:
                        print("\033[31m", "Пока нет ни одной заметки! \n","\033[37m")
                elif (command == 5):
                    if len(notes) != 0:
                        saveAll = SaveAll()
                        saveAll.saveToFile(notes)
                    else:
                        print("\033[31m","Пока нет ни одной заметки! \n","\033[37m")
                elif (command == 6):
                    print("\033[34m", "Всего доброго!", "\033[37m")
                    flag = False
                else:
                    print("\033[31m","Введено недопустимое значение. Повторите попытку.", "\033[37m")
            else:
                print("\033[31m","Введен недопустимый символ. Повторите попытку.", "\033[37m")

