from lib.task_list import TaskList
import sys


def main():
    print("Welcome to the Task Manager Application:")
    print('type "help" for a list of commands\n')

    tl = TaskList()

    while True:
        command = input()
        handle_command(command, tl)


def handle_command(command, tl):
    if command in ["quit", "q", "Q"]:
        sys.exit()
    elif command == "help":
        print("Valid commands include:")
        print("\tquit - exit program")
        print("\tshow - display tasks")
        print(
            "\tshow [complete, incomplete] - display only either complete or incomplete tasks"
        )
        print("\tadd -t <title> -d <description> - add a task")
        print("\tcomplete <id> - mark a task as completed")
    elif command == "show":
        # Assuming you have a function called displayTasks() that prints the tasks
        print(tl)

    elif command == "show complete":
        print(tl.displayFiltered(True))

    elif command == "show incomplete":
        print(tl.displayFiltered(False))

    elif command.startswith("add"):
        parts = command.split()
        if len(parts) < 5 or "-t" not in parts or "-d" not in parts:
            print(
                "Invalid command. Please provide both title and description using -t and -d tags."
            )
        else:
            title_index = parts.index("-t") + 1
            description_index = parts.index("-d") + 1
            if title_index >= len(parts) or description_index >= len(parts):
                print(
                    "Invalid command. Please provide both title and description using -t and -d tags."
                )
            else:
                # Extract title
                title_parts = []
                i = title_index
                while i < len(parts) and parts[i] != "-d":
                    title_parts.append(parts[i])
                    i += 1
                title = " ".join(title_parts)

                # Extract description
                description_parts = []
                i = description_index
                while i < len(parts) and (parts[i] != "-t" or parts[i] != "-t"):
                    description_parts.append(parts[i])
                    i += 1
                description = " ".join(description_parts)

                # Assuming you have a function called addTask() that adds the task
                tl.addTask(title, description)
                print("\nTask added successfully.\n")
    elif command.startswith("complete"):
        # Assuming the user input for marking a task completed is in the format "complete id"
        parts = command.split(maxsplit=1)
        if len(parts) < 2:
            print("Invalid command. Please provide the id of the task.")
        else:
            try:
                int(parts[1])
            except ValueError:
                print("Invalid command. Please provide the id of the task.")

            task_id = int(parts[1])
            # Assuming you have a function called markTaskCompleted() that marks the task as completed
            tl.markTaskCompleted(task_id)
            print("Task marked as completed.")
    else:
        print("Invalid command. Type 'help' for a list of valid commands.")


if __name__ == "__main__":
    main()
