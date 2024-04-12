class DeleteNote:

    def __init__(self) -> None:
        pass
         
    def deleteNoteByKey(self, notes: dict) -> dict:
        try:
            del notes[input("Введите идентификатор заметки для её удаления: ")]
            print("\033[32m","\nЗаметка успешно удалена!\n", "\033[37m")
        except KeyError:
            print("\033[31m", "Введен несуществующий идентификатор! ", "\033[37m")

        return notes