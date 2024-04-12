#Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки.
import datetime

class NewNote:
    Map = {
        "id": "Введите идентификатор заметки: ",
        "title": "Введите заголовок заметки: ",
        "body": "Введите текст заметки: ",
    }

    def __init__(self) -> None:
        self.noteTitle = ""
        self.noteBody = ""
        self.date = datetime.datetime.now().strftime("%c")
        self.noteId = ""

    def setNoteParam(self):
        self.setId()
        self.setTitle()
        self.setBody()
        self.date = datetime.datetime.now().strftime("%c")

    def setId(self) -> None:
        self.noteId = self.Input(self.Map["id"])

    def setTitle(self) -> None:
        self.noteTitle = self.Input(self.Map["title"])
    
    def setBody(self) -> None:
        self.noteBody = self.Input(self.Map["body"])

    def Input(self, message: str = "") -> str:
        userStr = input(message)
        return userStr
    
    def getTitle(self) -> str:
        return self.noteTitle
    
    def getBody(self) -> str:
        return self.noteBody
    
    def getId(self) -> str:
        return self.noteId
    
    def getTime(self) -> str:
        return self.date
    