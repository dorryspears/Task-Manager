from .task import Task


class TaskList:
    id = 0

    def __init__(self):
        self.id = 0
        self.tasks = {}

    def addTask(self, label="", description=""):
        self.tasks[self.id] = Task(description, label)
        self.id += 1

    def addTaskT(self, task: Task):
        self.tasks[self.id] = task
        self.id += 1

    def length(self):
        return len(self.tasks)

    # DO NOT TOUCH UNTIL LESSON TWO
    # def markTaskCompleted(self, id):
    #     pass

    # DO NOT TOUCH UNTIL LESSON THREE
    # def displayFiltered(self, isComplete) -> str:
    #     string = ""
    #     return string

    def __str__(self):
        string = "\n"
        string += "Tasks:\n"
        string += "===============================\n\n"

        for t in self.tasks:
            string += "{} - {}".format(t, self.tasks[t])
            string += "\n\n"

        return string
