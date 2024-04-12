import json


class SaveAll:

    def __init__(self) -> None:
        pass

    def saveToFile(self, notes) :
        with open('data.json', 'w') as file:
            
            json.dump(notes, file)
            print("\033[32m","\nСохранение успешно!\n", "\033[37m")