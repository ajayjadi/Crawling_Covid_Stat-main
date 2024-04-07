import os

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_query(module, query, current_directory):
    """
    Executes the specified make query in the given module directory.

    Args:
        module (str): The directory path of the module.
        query (str): The query to execute.
        current_directory (str): The current directory before executing the query.
    """
    clear_terminal()
    if os.getcwd() != module:
        os.chdir(module)
    os.system(f"make {query}")
    input("\nPress Enter to continue...")
    clear_terminal()
    os.chdir(current_directory)

def main_menu():
    """Displays the main menu."""
    clear_terminal()
    print("Welcome to Execute Queries of Modules 3.1 and 3.2")
    print("1. Execute Module 3.1")
    print("2. Execute Module 3.2")
    print("3. Exit")

def module_31_menu(current_directory):
    """Displays the menu for Module 3.1."""
    clear_terminal()
    print("Module 3.1 (Addressing Queries of Worldometer Covid Statistics)")
    print("1. Execute Query 1")
    print("2. Execute Query 2")
    print("3. Back to Main Menu")
    return current_directory

def module_32_menu(current_directory):
    """Displays the menu for Module 3.2."""
    clear_terminal()
    print("Module 3.2 (Addressing Queries of Wikipedia Covid News)")
    print("1. Execute Query 2.1")
    print("2. Execute Query 2.2")
    print("3. Execute Query 3")
    print("4. Execute Query 4")
    print("5. Execute Query 5")
    print("6. Back to Main Menu")
    return current_directory

# Main program
current_directory = os.getcwd()
while True:
    main_menu()
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        current_directory = module_31_menu(current_directory)
        while True:
            query_choice = input("\nEnter your choice: ")
            if query_choice == '1':
                execute_query("Module3.1", "query1", current_directory)
            elif query_choice == '2':
                execute_query("Module3.1", "query2", current_directory)
            elif query_choice == '3':
                break
            else:
                print("Invalid choice! Please try again.")
        clear_terminal()  # Clear the terminal after returning from executing queries
    
    elif choice == '2':
        current_directory = module_32_menu(current_directory)
        while True:
            query_choice = input("\nEnter your choice: ")
            if query_choice == '1':
                execute_query("Module3.2/2a", "all", current_directory)
            elif query_choice == '2':
                execute_query("Module3.2/2b", "all", current_directory)
            elif query_choice == '3':
                execute_query("Module3.2-345", "query3", current_directory)
            elif query_choice == '4':
                execute_query("Module3.2-345", "query4", current_directory)
            elif query_choice == '5':
                execute_query("Module3.2-345", "query5", current_directory)
            elif query_choice == '6':
                break
            else:
                print("Invalid choice! Please try again.")
        clear_terminal()  # Clear the terminal after returning from executing queries
    
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
