

def main():
    import os

    intro_active = True

    #Functions
    def clear_screen():
        print("cat")
        if os.name == 'nt': 
            os.system('cls')
        else:  
            os.system('clear')


    while intro_active == True:
        #Pre-defined variables
        is_new_user = None
        user_file_name = ""
        
        #Asks the user whether or not they already have an "acount"
        has_acount_input = input("\nDo you have a \"Nocturne of the Lamb\" acount? (yes/no)\n\n")
        has_acount_input = has_acount_input.strip().lower()

        #Checks for input validity
        while is_new_user == None:
            if has_acount_input == "yes":
                is_new_user = True 
            elif has_acount_input == "no":
                is_new_user = False
            else:
                print("\nAnswer must be either \"yes\" or \"no\".")
                has_acount_input = input()
            print()
        
        #Finds previous file by input or creates a new one
        if is_new_user == True:
            user_file_name = input("Enter acount name or type \"return\" to return.\n\n")

            if user_file_name.strip().lower() == "return":
                continue
            elif os.path.exists(user_file_name) and os.path.isfile(user_file_name):
                current_file = open(user_file_name, "r+")
                print(f"\nHello {current_file.readline()}! Welome to Nocturne of the Lamb.")
                intro_active = False
            else:
                print("\n\nFile does not exist.\n\n...re-directing...\n\n")
                input("Press Enter/Return to continue.\n\n")
                clear_screen()
                

        else:
            user_file_name = input("Enter the name of your new Nocturne file.\n\n")
            
            if os.path.exists(user_file_name) or os.path.isfile(user_file_name):
                print("\nThis system cannot re-write a pre-existing file.\n\n...re-directing...\n\n")
                input("Press Enter/Return to continue.\n\n")
                clear_screen()
                
            
            else:
                current_file = open(user_file_name, "w")
                current_file.write(input("\nPlease enter your preffered name.\n\n"))
                current_file.close()
                clear_screen()
            


        

if __name__ == "__main__":
    main()