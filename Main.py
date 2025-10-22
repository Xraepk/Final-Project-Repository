
def main():
    import os
    from defaults import DEFAULT_ROOMS, DEFAULT_NPCS, DEFAULT_ATTRIBUTES

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

    def write_preset(name, rooms=DEFAULT_ROOMS, npcs=DEFAULT_NPCS, attributes=DEFAULT_ATTRIBUTES, type="new"):
        

    def preset_manager():
        global user_file
        changing_presets = True
        while changing_presets:
            clear()
            print("Current presets:")
            for line in presets:
                print(f"\t{line}")
            print("\nEnter \"A\" to create a new preset."
                  "\nEnter \"B\" to edit existing preset."
                  "\nEnter \"C\" to delete an existing preset.")
            preset_command = input("Enter: ")
            if preset_command == "A":
                creating_preset = True
                while creating_preset:
                    new_preset = input("Enter new preset file name: ")
                    if os.path.exists(new_preset) or os.path.isfile(new_preset):
                        print("File already exists. Enter new file name. (Enter) ")
                    else:
                        open(new_preset, "w").close()
                        creating_preset = False
                        input(f"File {new_preset} created. (Enter) ")
            elif preset_command == "B":
                None


    def generate():
        return None

    sign_in()
    main_menu()
    generate()

if __name__ == "__main__":
    main()