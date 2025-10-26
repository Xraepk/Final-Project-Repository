
def main():
    import os
    import json
    import random
    import datetime
    from defaults import DEFAULT_ROOMS, DEFAULT_NPCS, DEFAULT_ATTRIBUTES

    user_file = ""
    return_to_main = True

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

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

    def write_preset(name, rooms=DEFAULT_ROOMS, npcs=DEFAULT_NPCS, attributes=DEFAULT_ATTRIBUTES):
        with open(name, "w") as file:
            json.dump(rooms, file)
            file.write("\n")
            json.dump(npcs, file)
            file.write("\n")
            json.dump(attributes, file)

    def read_preset(name):
        with (open(name) as file):
            room_line = file.readline()
            rooms_info = json.loads(room_line)
            npc_line = file.readline()
            npc_info = json.loads(npc_line)
            attrubute_line = file.readline()
            attribute_info = json.loads(attrubute_line)
            return rooms_info, npc_info, attribute_info

    def preset_manager():
        global user_file
        changing_presets = True
        while changing_presets:
            clear()
            presets = open(user_file, "r").readlines()
            print("Current presets:\n")
            for line in presets:
                print(f"\t{line}")
            print("Enter \"A\" to create a new preset."
                  "\nEnter \"B\" to edit existing preset."
                  "\nEnter \"C\" to delete an existing preset."
                  "\nEnter anything else to return.")
            preset_command = input("\nEnter: ").strip().upper()
            if preset_command == "A":
                creating_preset = True
                while creating_preset:
                    new_preset = input("Enter new preset file name: ")
                    if os.path.exists(new_preset) or os.path.isfile(new_preset):
                        input("File already exists. Enter new file name. (Enter) ")
                    else:
                        with open(user_file, "a") as file:
                            file.write(new_preset)
                            file.write("\n")
                        write_preset(new_preset)
                        creating_preset = False
                        input(f"File {new_preset} created. (Enter) ")
            elif preset_command == "B":
                edit_preset = input("Enter the preset file name you wish to edit: ").strip()
                with open(user_file) as file:
                    is_preset = False
                    for line in file.readlines():
                        if line == f"{edit_preset}\n":
                            is_preset = True
                    if is_preset:
                        editing_preset = True
                        while editing_preset:
                            clear()
                            rooms, npcs, attributes = read_preset(edit_preset)
                            print(f"{edit_preset} information:\n")
                            print("\tRooms:")
                            for key, value in rooms.items():
                                print(f"\t\t{key.replace('\n', ' ')}: {value.replace('\n', ' ')}")
                            print("\n\tNPCs:")
                            for npc in npcs:
                                print(f"\t\t{npc}")
                            print("\n\tAttributes:")
                            for key, value in attributes.items():
                                print(f"\t\t{key}: ", end="")
                                for item in value:
                                    if value.index(item) == len(value) - 1:
                                        print(f"{item}", end="")
                                    else:
                                        print(f"{item}, ", end="")
                                print()
                            edit_command = input("\nKey:"
                                                 "\n\tEnter \"A\" to edit Rooms"
                                                 "\n\tEnter \"B\" to edit NPCs"
                                                 "\n\tEnter \"C\" to edit Attributes"
                                                 "\n\tEnter anything else to exit"
                                                 "\n\nEnter: ").strip().upper()
                            if edit_command == "A":
                                clear()
                                room_dict = dict()
                                print("Enter room names one at a time, then enter its description."
                                      " Enter \"DONE\" to finish.\n")
                                name = ""
                                while name.strip().upper() != "DONE":
                                    name = input("Enter room name: ")
                                    if name.strip().upper() == "DONE":
                                        finalize = input("Rewrite Rooms? (Y/anything else) ").strip().upper()
                                        if finalize == "Y":
                                            write_preset(edit_preset, room_dict, npcs, attributes)
                                            input("File updated. (Enter) ")
                                    else:
                                        description = input(f"Enter {name} description: ")
                                        room_dict[name] = description
                            elif edit_command == "B":
                                clear()
                                npc_list = []
                                print("Enter NPC names one at a time. Enter \"DONE\" to finish.\n")
                                name = ""
                                while name.strip().upper() != "DONE":
                                    name = input("Enter NPC name: ").title()
                                    if name.strip().upper() == "DONE":
                                        finalize = input("Rewrite NPCs? (Y/anything else) ").strip().upper()
                                        if finalize == "Y":
                                            write_preset(edit_preset, rooms, npc_list, attributes)
                                            input("File updated. (Enter) ")
                                    else:
                                        npc_list.append(name)
                            elif edit_command == "C":
                                clear()
                                print("Key:")
                                print("\tEnter \"A\" to edit Hair Lengths"
                                      "\n\tEnter \"B\" to edit Hair Colors"
                                      "\n\tEnter \"C\" to edit Shoe Types"
                                      "\n\tEnter \"D\" to edit Outer Wear"
                                      "\n\tEnter \"E\" to edit Shirt Colors"
                                      "\n\tEnter \"F\" to edit Pants Types"
                                      "\n\tEnter \"G\" to edit Special Wear"
                                      "\n\tEnter \"H\" to edit Special Items"
                                      "\n\tEnter anything else to exit")
                                attribute_command = input("Enter: ").strip().upper()
                                clear()
                                attribute_command_dict = {"A": "Hair Lengths",
                                                          "B": "Hair Colors",
                                                          "C": "Shoe Types",
                                                          "D": "Outer Wear",
                                                          "E": "Shirt Colors",
                                                          "F": "Pants Types",
                                                          "G": "Special Wear",
                                                          "H": "Special Items"}

                                for letter, category in attribute_command_dict.items():
                                    if attribute_command == letter:
                                        edit_attribute = category
                                new_attribute_list = []
                                attribute_name = ""
                                print(f"\nEnter {edit_attribute} names. Enter \"DONE\" to finish.\n")
                                while attribute_name.strip().upper() != "DONE":
                                    attribute_name = input(f"Enter {edit_attribute} name: ")
                                    if attribute_name.strip().upper() != "DONE":
                                        new_attribute_list.append(attribute_name)

                                finalize = input(f"Rewrite {edit_attribute}? (Y/anything else) ").strip().upper()
                                if finalize == "Y":
                                    attributes[edit_attribute] = new_attribute_list
                                    write_preset(edit_preset, rooms, npcs, attributes)
                                    input("File updated. (Enter) ")
                            else:
                                editing_preset = False





                    else:
                        input("Invalid file. (Enter) ")
            elif preset_command == "C":
                delete_file = input("Enter the file you wish to delete or enter \"DONE\" to exit: ")
                file = open(user_file, "r")
                if delete_file.strip().upper() == "DONE":
                    clear()
                else:
                    is_a_preset = False
                    for line in file.readlines():
                        if f"{delete_file}\n" == line:
                            is_a_preset = True
                            file.close()
                            finalize = input(f"Are you sure you want to delete {delete_file}? "
                                             "This cannot be undone. (Y/anything else) ").strip().upper()
                            if finalize == "Y":
                                os.remove(delete_file)
                                file.close()
                                with open(user_file) as read_file:
                                    preset_info = read_file.readlines()
                                open(user_file, "w").close()
                                with open(user_file, "a") as write_file:
                                    for line in preset_info:
                                        if not(f"{delete_file}\n" == line):
                                            write_file.write(line)
                    if is_a_preset == False:
                        input("Invalid preset file. (Enter) ")
            else:
                changing_presets = False
                clear()

    def generate():
        global return_to_main
        return_to_main = True
        global user_file
        generating = True
        while generating:
            clear()
            generate_navigation = input("Enter \"A\" to play Classic"
                                        "\nEnter \"B\" to play a preset"
                                        "\nEnter anything else to return"
                                        "\n\nEnter: ").strip().upper()
            if generate_navigation == "A":
                gen_rooms = DEFAULT_ROOMS
                gen_npcs = DEFAULT_NPCS
                gen_attributes = DEFAULT_ATTRIBUTES
                return_to_main = False
            elif generate_navigation == "B":
                with open(user_file) as file:
                    clear()
                    presets = file.readlines()
                    if len(presets) > 0:
                        print("Current presets:\n")
                        for line in presets:
                            print(f"\t{line}")
                        file_to_load = input("Enter preset file name to load: ")
                        for line in presets:
                            if f"{file_to_load}\n" == line and not(line == ""):
                                gen_rooms, gen_npcs, gen_attributes = read_preset(file_to_load)
                                loaded = True
                                input("File loaded. (Enter) ")
                                return_to_main = False
                            else:
                                input("Invalid preset file. (Enter) ")
                    else:
                        input("You have no presets on this account. (Enter) ")
            else:
                break

            killer = random.choice(gen_npcs)
            npc_dict = {}
            for npc in gen_npcs:
                is_killer = True if npc == killer else False
                hair_length = random.choice(gen_attributes["Hair Lengths"])
                hair_color = random.choice(gen_attributes["Hair Colors"])
                shoe_type = random.choice(gen_attributes["Shoe Types"])
                outer_wear = random.choice(gen_attributes["Outer Wear"])
                shirt_color = random.choice(gen_attributes["Shirt Colors"])
                pants_type = random.choice(gen_attributes["Pants Types"])
                special_wear = random.choice(gen_attributes["Special Wear"])
                special_item = random.choice(gen_attributes["Special Items"])
                npc_dict[npc] = [is_killer, hair_length, hair_color, shoe_type, outer_wear, shirt_color, pants_type, special_wear, special_item]

            game_interface(gen_rooms, npc_dict):

    def game_interface(rooms, npcs):



    sign_in()
    while return_to_main == True:
        main_menu()
        generate()

if __name__ == "__main__":
    main()