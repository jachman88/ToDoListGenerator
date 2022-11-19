# This is a basic command line To-Do list app

# Banner
print("*" * 10)
print("To Do List")
print("*" * 10)

# Add feature here that prompts user to either create a new list or open an existing list.

my_list = []

while True:
    user_action = input('Type add, show, edit, delete or exit: ')
    user_action = user_action.strip()  # incase any spaces get added at the end
    match user_action:
        case 'add':
            list_item = input("What would you like to do? ")
            my_list.append(list_item)
        case 'show' | 'display':
            for task_number, item in enumerate(my_list):
                task_number = task_number + 1
                row = f"{task_number}. {item.capitalize()}"
                print(row)
        case 'edit' | 'modify':
            task_number = int(input("Which task would you like to edit? "))
            task_number = task_number - 1
            my_list[task_number] = input("What would you like to do now? ")
        case 'delete' | 'remove':
            list_item = int(input("Which task would you like to delete? "))
            list_item = list_item - 1
            my_list.pop(list_item)
        case 'exit':
            print("Good Bye!") # Change messaging here once writing to file feature has been added.
            break

# Add feature to write the list to a file.
