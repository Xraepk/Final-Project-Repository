

def main():
    import os

    user_file = ""

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def sign_in():
        global user_file
        logging_in = True
        clear()
        while logging_in:
            has_account = input("Do you have an account? (Y/N) ").strip().upper()
            if has_account == "Y":
                user_file = input("Enter account name: ")
                if os.path.exists(user_file) and os.path.isfile(user_file):
                    print("Opening file...")
            elif has_account == "N":
                user_file = input("Enter new file name: ")
                if os.path.exists(user_file) or os.path.isfile(user_file):
                    print("\nFile already exists. Enter new file name.\n")
                else:
                    open(user_file, "w").close()
                    input("File created. (Enter) ")
                    clear()
            else:
                clear()
                print("Invalid input.", end="")



    sign_in()

        

if __name__ == "__main__":
    main()