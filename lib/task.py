class Task:
    label = ""
    description = ""
    complete = False

    def __init__(self, label="", description=""):
        self.label = label
        self.description = description

    def markComplete(self):
        self.complete = True

    def __str__(self) -> str:
        completed = "Completed" if self.complete else "Not Complete"
        string = ""
        string += f"{self.label}: {completed}\n"
        string += "-------------------------------\n"
        string += self.description

        return string
