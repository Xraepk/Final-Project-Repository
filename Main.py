

def main():
    import os

    user_file = ""

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def read_file(name):
        with open(name) as file:
            return file.readlines()

    def sign_in():
        global user_file
        logging_in = True
        while logging_in:
            clear()
            has_account = input("Do you have an account? (Y/N) ").strip().upper()
            if has_account == "Y":
                user_file = input("Enter account name: ")
                if os.path.exists(user_file) and os.path.isfile(user_file):
                    input("File loaded. (Enter) ")
                    logging_in = False
                else:
                    input("Invalid file. (Enter) ")
            elif has_account == "N":
                user_file = input("Enter new file name: ")
                if os.path.exists(user_file) or os.path.isfile(user_file):
                    input("File already exists. Enter new file name. (Enter) ")
                else:
                    open(user_file, "w").close()
                    input("File created. (Enter) ")
                    clear()
            else:
                input("Invalid input. (Enter) ")

    def main_menu():
        clear()
        begin = False
        while begin == False:
            command = input("Enter \"A\" to begin generation.\nEnter \"B\" to create/edit presets.\n\nEnter: ").strip()
            if command.upper() == "A":
                begin = True
            elif command.upper() == "B":
                preset_manager()

    def preset_manager():
        clear()
        presets = read_file("user_file")
        print("Current presets:")
        for line in presets():
            print(f"\t{line}")
        print("\nEnter \"A\" to create a new preset.\nEnter \"B\" to edit existing preset.")


    def generate():
        return None

    sign_in()
    main_menu()
    generate()

if __name__ == "__main__":
    main()