import os
import json
import random
from defaults import DEFAULT_ROOMS, DEFAULT_NPCS, DEFAULT_ATTRIBUTES

# Universal file directory. Does not change after sign-in
user_file = ""

def clear():
    """Clears the screen. Purely for aesthetics and readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def sign_in():
    """Summons account preset information for the app and allows for the creation of new accounts."""
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
            user_file = input("Enter new file name or enter \"0\" to return: ")
            if user_file == "0":
                pass
            elif os.path.exists(user_file) or os.path.isfile(user_file):
                input("File already exists. Enter new file name. (Enter) ")
            else:
                open(user_file, "w").close()
                input("File created. (Enter) ")
                clear()
        else:
            input("Invalid input. (Enter) ")

def main_menu():
    """Essentially maneuvers between the other functions,
    differing in editing, generation, and perhaps tutorial"""
    begin = False
    while begin == False:
        clear()
        command = input("Enter \"A\" to begin generation."
                        "\nEnter \"B\" to create/edit presets."
                        "\nEnter \"C\" to enter the tutorial"
                        "\n\nEnter: ").strip().upper()
        if command == "A":
            begin = True
        elif command == "B":
            preset_manager()
        elif command == "C":
            tutorial()

def write_preset(name, rooms=DEFAULT_ROOMS, npcs=DEFAULT_NPCS, attributes=DEFAULT_ATTRIBUTES):
    """Writes/Re-Writes presets for preset creation and preset edits."""
    with open(name, "w") as file:
        json.dump(rooms, file)
        file.write("\n")
        json.dump(npcs, file)
        file.write("\n")
        json.dump(attributes, file)

def read_preset(name):
    """Returns the given preset's rooms dict, NPC list, and attribute dict."""
    with (open(name) as file):
        room_line = file.readline()
        rooms_info = json.loads(room_line)
        npc_line = file.readline()
        npc_info = json.loads(npc_line)
        attribute_line = file.readline()
        attribute_info = json.loads(attribute_line)
        return rooms_info, npc_info, attribute_info

def preset_manager():
    """Controls preset changes including creating new preset files,
    deleting preset files, and editing presets."""
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
                            print("Enter room names one at a time, then enter its description. "
                                  "(!NAME CANNOT START WITH A DIGIT!)"
                                  " \nEnter \"DONE\" to finish.\n")
                            name = ""
                            while name.strip().upper() != "DONE":
                                name = input("Enter room name: ")
                                if name.strip().upper() == "DONE":
                                    finalize = input("Rewrite Rooms? (Y/anything else) ").strip().upper()
                                    if finalize == "Y":
                                        write_preset(edit_preset, room_dict, npcs, attributes)
                                        input("File updated. (Enter) ")
                                elif name.strip().upper()[:1].isdigit():
                                    print("Invalid room name.")
                                else:
                                    description = input(f"Enter {name} description: ")
                                    room_dict[name] = description
                        elif edit_command == "B":
                            clear()
                            npc_list = []
                            print("Enter NPC names one at a time. (!NAME CANNOT START WITH A DIGIT!) "
                                  "\nEnter \"DONE\" to finish.\n")
                            name = ""
                            while name.strip().upper() != "DONE":
                                name = input("Enter NPC name: ").title()
                                if name.strip().upper() == "DONE":
                                    finalize = input("Rewrite NPCs? (Y/anything else) ").strip().upper()
                                    if finalize == "Y":
                                        write_preset(edit_preset, rooms, npc_list, attributes)
                                        input("File updated. (Enter) ")
                                elif name.strip().upper()[:1].isdigit():
                                    print("Invalid NPC name.")
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
                            print(f"\nEnter {edit_attribute} names. (!NAME CANNOT START WITH A DIGIT!)"
                                  f"\nEnter \"DONE\" to finish.\n")
                            while attribute_name.strip().upper() != "DONE":
                                attribute_name = input(f"Enter {edit_attribute} name: ")
                                if attribute_name.strip().upper()[:1].isdigit():
                                    print("Invalid attribute name.")
                                elif attribute_name.strip().upper() != "DONE":
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
                                    if not (f"{delete_file}\n" == line):
                                        write_file.write(line)
                if is_a_preset == False:
                    input("Invalid preset file. (Enter) ")
        else:
            changing_presets = False
            clear()

def tutorial():
    """Function for teaching users how to Dungeon Master"""

    tutorial_active = True
    while tutorial_active:
        clear()
        tutorial_nav = input("Welcome to Nocturne of the Lamb!"
                            "\n\nNever played before? We've got you covered!"
                            "\nWhat would you like to learn?"
                             "\n\n1) What is the game about?"
                             "\n2) How do you play?"
                             "\n3) How do you Dungeon Master?"
                             "\n4) What does the app do for me?"
                             "\n5) How do I make a new preset?"
                             "\n6) Return to main menu"
                            "\n\nEnter: ")
        if tutorial_nav == "1":
            clear()
            input("So what is Nocturne of the Lamb really about?"
                  "\n\nWanna know a secret?"
                  "\nIT'S ABOUT WHATEVER YOU WANT!"
                  "\nThis game does have some defaults to get you started,"
                  "\nHOWEVER,"
                  "\nThis game is completely customizable and the story is whatever you decide!"
                  "\n\n(Enter) ")
        elif tutorial_nav == "2":
            clear()
            input("So how are you supposed to play Nocturne of the Lamb?"
                  "\n\nFor the player, all you need to play is something to take notes on!"
                  "\nThis game is all about gathering clues, making deductions, and surviving."
                  "\nAt the beginning of every round, your Dungeon Master will tell you:"
                  "\n\nA) What time it is (A.K.A. the name of the round) and"
                  "\nB) What happens immediately (eg screaming, lights go out)"
                  "\n\nThe Dungeon Master will inform you when it is your turn."
                  "\nAt this point you will simply begin by declaring to which room you would like to go."
                  "\nAfter your character is \"in the room\", "
                  "your Dungeon Master will describe to you what your character finds."
                  "\n\nAfter this, while you are in the room, you have the following actions:"
                  "\n\nA) Speaking to characters"
                  "\nB) Searching the room for clues"
                  "\nC) Inspecting a body"
                  "\n\nOccasionally if the killer is in \"HOSTILE\" state,"
                  "\nYou have the additional action to hide from the killer."
                  "\nIf you fail to hide (Determined by this app or a D20) then you die."
                  "\n\nYou lose the game if every player dies or if all NPC's die before you discover the killer."
                  "\nYou win by discovering the killer, surviving, and proving it using substantial evidence."
                  "\nWhat is \"substantial evidence\" is determined by your Dungeon Master."
                  "\nAny gameplay change to this style will be explained before hand by your DM"
                  "\n\n(Enter) ")
        elif tutorial_nav == "3":
                clear()
                input("So how do you Dungeon Master for Nocturne of the Lamb?"
                      "\n\nFirst of all you are going to want a few things."
                      "\n\nA) Something to take notes (Optional - The interface has a notepad)"
                      "\nB) This app"
                      "\nC) A drawn map of your area (Optional - only for visualization)"
                      "\nD) A D6 (Suggested) and D20 (Optional)"
                      "\n\nYou will start your game by going to generate and either choosing a preset name or Classic."
                      "\nOnce the preset loads you will have the option to choose who you want the killer to be."
                      "\nFeel free to just enter random for your first time!"
                      "\n\nNow the game is fully set up. Tell everyone what room they all begin in."
                      "\nThis doesn't matter much but it's useful for the first murder "
                      "if you want them to know the direction of a scream."
                      "\n\nAfter this you start the first round by declaring what time it is and what happens."
                      "\nExample: \"It is now 12:00. You hear a blood-curdling scream ring out from the east.\""
                      "\nNext, you go around the table running each player through their turn."
                      "\nFirst, ask them to pick a location they would like to inspect."
                      "\nOnce their character is there, describe the room to them and who is there."
                      "\nThen, as they meet people inform them about character attributes that are clearly visible"
                      "\nIf they inspect something, to see if they find a clue you ust first "
                      "decide if there is a clue to find"
                      "\nIf there is, use the built check feature in the interface. "
                      "(Enter \"key\" to see commands in the interface)"
                      "\nTo do a check, first have you player roll a D6 and then input the number for the check."
                      "\nThe game will tell you if the chack fails or not. "
                      "\nCheck can also be used when trying to hide from a hostile killer"
                      "\n\nIf the check is successful, use the clue feature of the interface."
                      "\nThis will tell you what piece of information about the killer to give to your player."
                      "\n\nThose are the basics! Because this game is customizable, feel free to break rules!"
                      "\nExperiment! Write your own story! Add fake clues! Good luck!"
                      "\nMake sure to look through the key page of the interface."
                      "\nThere are all sorts of commands to make your life easier!"
                      "\n(Enter) ")
        elif tutorial_nav == "4":
            clear()
            input("So what does this app do for me as a Dungeon Master?"
                  "\n\nWell, first of all we have the interface. The interface has randomization capabilities."
                  "\nIt also keeps track of all player information at all times so you don't have to worry!"
                  "\nWith commands from the interface you can do the following:"
                  "\n\nA) Summon a list of room names"
                  "\nB) Summon a list of NPC names"
                  "\nC) Perform a D6 roll based check"
                  "\nD) Continue to the next round"
                  "\nE) End the game"
                  "\nF) Write and look at notes from you digital notepad"
                  "\nG) Summon information from a specific room"
                  "\nH) Summon information from a specific NPC"
                  "\n\nAll of the interface commands are designed to make your gameplay smoother, "
                  "so make sure to try them!"
                  "\n\nThis app also allows you to store presets so you can play your own maps and NPC sets!"
                  "\n(Enter) ")
        elif tutorial_nav == "5":
            clear()
            input("So how do you make a new preset?"
                  "\n\nThe system is fairly self explanatory so once you go to presets just follow the instructions!"
                  "\nMake a new preset with default variables, then swap out the defaults with whatever you like!"
                  "\nYou can also delete any presets you don't want on your system."
                  "\n(Enter) ")
        elif tutorial_nav == "6":
            tutorial_active = False

def generate():
    """Generates character attributes into a dictionary and passes
    all preset/default information into the game_interface function"""
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
                        if f"{file_to_load}\n" == line and not (line == ""):
                            gen_rooms, gen_npcs, gen_attributes = read_preset(file_to_load)
                            loaded = True
                            input("File loaded. (Enter) ")
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
            npc_dict[npc] = [is_killer, hair_length, hair_color, shoe_type, outer_wear, shirt_color, pants_type,
                             special_wear, special_item]

        game_interface(gen_rooms, npc_dict, killer)

def game_interface(rooms, npcs, killer):
    """This is the actual function that helps run the game.
    The interface has several commands that allows the DM to
    acquire information more easily. It also shuffles NPC locations,
    chooses whether an NPC dies, and if so which one (can be overwritten),
    and keeps track of the turn, which is based on half hour increments."""
    hour = 11
    minute = 3
    game_active = True
    note_pad = []
    while game_active:
        if len(npcs) > 1:
            # Adds 30 minutes to game time
            if hour == 12 and minute == 3:
                hour = 1
            elif minute == 3:
                hour += 1
            if minute == 3:
                minute = 0
            else:
                minute = 3
            round_active = True

            npc_locations = {}
            for room in rooms:
                npc_locations[room] = ""
            for npc in npcs:
                room = random.choice(list(rooms))
                npc_locations[room] = npc_locations[room] + f" {npc},"

            # These assignments are essentially fail-safes in case the algorithm happens to be loop-holed
            hostile = False
            death_message = "No Death"
            killed = None
            kill_room = None
            killer_room = None

            if input("Choose NPC to kill? (Y/anything else)").strip().upper() == "Y":
                picking_murder = True
                while picking_murder:
                    clear()
                    for npc in npcs:
                        print(npc)
                    kill_choice = input("\nEnter NPC name or \"NONE\" for no murder: ")
                    if kill_choice.strip().upper() == "NONE":

                        picking_murder = False
                        hostile = True
                    elif kill_choice in npcs:
                        killed = kill_choice
                        for room in npc_locations:
                            if killed in npc_locations[room]:
                                kill_room = room
                        death_message = f"{killed} was murdered in {kill_room}"
                        picking_murder = False
                    else:
                        input("Invalid NPC. (Enter) ")

            elif random.randint(1, 100) <= 75:
                killed = random.choice(list(npcs.keys()))
                while killed == killer:
                    killed = random.choice(list(npcs.keys()))
                for room in npc_locations:
                    if killed in npc_locations[room]:
                        kill_room = room
                death_message = f"{killed} was murdered in {kill_room}"
            else:
                hostile = True
            for room in npc_locations:
                if killer in npc_locations[room]:
                    killer_room = room

            while round_active:
                clear()

                print(f"{killer} (Killer) is in {killer_room}")
                print(f"\nThe time is {hour}:{minute}0\n")
                print(death_message)
                print("\nEnter \"KEY\" for interface interaction menu")
                interface = input("\nEnter: ").strip()
                clear()
                if interface.upper() == "KEY":
                    print("Interface commands:"
                          "\n\n\tEnter \"1\" for room names"
                          "\n\tEnter \"2\" for NPC names"
                          "\n\tEnter \"3\" for a roll based check"
                          "\n\tEnter \"4\" for clue generation"
                          "\n\tEnter \"5\" to end round"
                          "\n\tEnter \"6\" to end game"
                          "\n\tEnter \"7\" to make a new note"
                          "\n\tEnter \"8\" to see your notes"
                          "\n\tEnter room name for room information"
                          "\n\tEnter character name for character information")
                    input("\n(Enter) ")
                elif interface.upper() == "1":
                    for room in rooms:
                        print(room)
                    input("\n(Enter) ")
                elif interface.upper() == "2":
                    for npc in npcs:
                        print(npc)
                    input("\n(Enter) ")
                elif interface.upper() == "3":
                    hiding_num = input("Enter D6 roll. Enter anything else to return. : ")
                    is_num = True
                    for character in hiding_num:
                        if not (character in ("1", "2", "3", "4", "5", "6")):
                            is_num = False
                    if hiding_num.strip() == "":
                        is_num = False
                    if is_num == True:
                        if not (random.randint(1, int(hiding_num)) == 1):
                            print("Success")
                        else:
                            print("Failure")
                    else:
                        print("Invalid Number")
                    input("\n(Enter) ")
                elif interface.upper() == "4":
                    clue_num = random.randint(1, 8)
                    clue = npcs[killer][clue_num]
                    clue_type = None
                    if clue_num == 1:
                        clue_type = "Hair Length"
                    elif clue_num == 2:
                        clue_type = "Hair Color"
                    elif clue_num == 3:
                        clue_type = "Shoe Type"
                    elif clue_num == 4:
                        clue_type = "Outer Wear"
                    elif clue_num == 5:
                        clue_type = "Shirt Color"
                    elif clue_num == 6:
                        clue_type = "Pants Type"
                    elif clue_num == 7:
                        clue_type = "Special Wear"
                    elif clue_num == 8:
                        clue_type = "Special Item"
                    input(f"Clue: {clue_type} - {clue}")
                elif interface.upper() == "5":
                    round_active = False
                    continue
                elif interface.upper() == "6":
                    round_active = False
                    game_active = False
                elif interface.upper() == "7":
                    new_note = input("Enter note: ")
                    note_pad.append(f"\t- {new_note}")
                elif interface.upper() == "8":
                    print("Notes:\n")
                    for note in note_pad:
                        print(note)
                    input("\n(Enter) ")
                elif interface in rooms.keys():
                    print(f"{interface} information:")
                    print(f"\n\tDescription: {rooms[interface].replace("\n", " ")}")
                    print(f"\n\tCharacters in {interface}:{npc_locations[interface][:-1]}")
                    if hostile and interface == killer_room:
                        print(f"\n\tHOSTILE AREA : {killer.upper()}")
                    elif interface == kill_room:
                        print(f"\n\t{killed} is Dead.")
                    input("\n(Enter) ")
                elif interface in npcs.keys():
                    current_room = "I should be assigned. Problemo."
                    for room in npc_locations:
                        if interface in npc_locations[room]:
                            current_room = room
                    print(f"\n{interface} information:\n"
                          f"\n\tHair Length: {npcs[interface][1]}"
                          f"\n\tHair Color: {npcs[interface][2]}"
                          f"\n\tShoe Type: {npcs[interface][3]}"
                          f"\n\tOuter Wear: {npcs[interface][4]}"
                          f"\n\tShirt Color: {npcs[interface][5]}"
                          f"\n\tPants Type: {npcs[interface][6]}"
                          f"\n\tSpecial Wear: {npcs[interface][7]}"
                          f"\n\tSpecial item: {npcs[interface][8]}"
                          f"\n\n\tCurrent Whereabouts: {current_room}")
                    input("\n(Enter) ")

            if killed:
                npcs.pop(killed)
        else:
            input("All NPCs are dead. (Enter) ")
            game_active = False

def main():



    # This is where I run the initial functions. After sign_in, main_menu rotates with generate until game end.
    sign_in()
    while True:
        main_menu()
        generate()


if __name__ == "__main__":
    main()