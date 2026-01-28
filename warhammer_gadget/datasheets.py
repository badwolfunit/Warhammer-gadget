# Written by Badwolfunit
# This program is designed to help run warhammer games by using digital features. Will try to build a device built around this program. Datasheets must be provided by user
# Copyright (C) 2026  Luca Smith(Badwolfunit)
# Disclaimer:
# Warhammer is a trademark of Games Workshop Ltd. This project is not affiliated with, endorsed by, or associated with Games Workshop in any way.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
import os
from pathlib import Path
from texttable import Texttable


def datasheetsfunct():
    # Lists available datasheets and allows user to select one to load
    print("Here are the available datasheets:")
    datasheets_dir = Path.home() / ".config" / "warhammer-gadget" / "datasheets"
    
    # Check if directory exists
    if not datasheets_dir.exists():
        print("No datasheets directory found. Please add datasheets to ~/.config/warhammer-gadget/datasheets/")
        return
    
    datasheet_files = [f for f in os.listdir(datasheets_dir) if f.endswith('.json')]
    
    if not datasheet_files:
        print("No datasheets found. Please add JSON files to ~/.config/warhammer-gadget/datasheets/")
        return
        
    print(datasheet_files)
    # Get user input for which datasheet to load
    chooseDatasheet: str = input("Enter the name of the datasheet you want to load (without .json extension): ")
    # Create full path to datasheet
    datasheetPath = datasheets_dir / f"{chooseDatasheet}.json"
    
    if datasheetPath.exists():
        try:
            # Loads selected datasheet
            with open(datasheetPath) as f:
                datasheet = json.load(f)
            # Confirm successful load
            print(f"Datasheet '{chooseDatasheet}' loaded successfully.")
            # Print datasheet content
            print(json.dumps(datasheet, indent=4))
            """
            # Display base stats
            print("Datasheet Name:", datasheet["unit_name"])
            print("Base Stats:")
            # The code snippet you provided is setting up a table using the `Texttable` library to
            # display the base stats of a datasheet. Here's a breakdown of what each line is doing:
            base_stats = Texttable()
            # `base_stats = Texttable()` is initializing an instance of the `Texttable` class, which
            # is used to create and format text-based tables. This line of code creates a new table
            # object named `base_stats` that will be used to display the base stats of a datasheet in
            # a structured and visually appealing way.
            base_stats.set_deco(Texttable.HEADER)
            base_stats.set_cols_dtype(['t', 'a'])
            base_stats.set_cols_align(["l", "r"])
            base_stats.add_rows([["Name", "Value"],
                                ["Movement", datasheet["stats"]["movement"]],
                                ["Toughness", datasheet["stats"]["toughness"]],
                                ["Wounds", datasheet["stats"]["wounds"]],
                                ["Leadership", datasheet["stats"]["leadership"]],
                                ["Save", datasheet["stats"]["save"]],
                                ["Objective Control", datasheet["stats"]["objective_control"]]])
            print(base_stats.draw())
            
            # Display ranged weapons
            print("Weapons:")
            # Check if there are ranged weapons
            if "ranged" in datasheet["weapons"]:
                print("Ranged Weapons:")
                # Loop through each ranged weapon
                for i in range(1, 20):  # Assuming a maximum of 19 ranged weapons
                    key = f"ranged_{i}"
                    # If the weapon exists, display its stats
                    if key in datasheet["weapons"]["ranged"]:
                        # Get weapon data
                        weapon = datasheet["weapons"]["ranged"][key]
                        # Set up table for ranged weapon
                        ranged = Texttable()
                        ranged.set_deco(Texttable.HEADER)
                        ranged.set_cols_dtype(['t', 'a'])
                        ranged.set_cols_align(["l", "r"])
                        ranged.add_rows([["Name", "Value"],
                                         ["Name", weapon["name"]],
                                         ["Range", weapon["range"]],
                                         ["Attacks", weapon["attacks"]],
                                         ["Ballistic Skill", datasheet["stats"]["ballistic_skill"]],
                                         ["Strength", datasheet["stats"]["strength"]],
                                         ["Type", weapon["type"]],
                                         ["AP", weapon["ap"]],
                                         ["Damage", weapon["damage"]]])
                        print(ranged.draw())
            else:
                print("No Ranged Weapons found.")
            
            # Display melee weapons
            print("Weapons:")
            # Check if there are melee weapons
            if "melee" in datasheet["weapons"]:
                print("Melee Weapons:")
                # Loop through each melee weapon
                for i in range(1, 20):  # Assuming a maximum of 19 melee weapons
                    key = f"melee_{i}"
                    # If the weapon exists, display its stats
                    if key in datasheet["weapons"]["melee"]:
                        # Get weapon data
                        weapon = datasheet["weapons"]["melee"][key]
                        # Set up table for melee weapon
                        melee = Texttable()
                        melee.set_deco(Texttable.HEADER)
                        melee.set_cols_dtype(['t', 'a'])
                        melee.set_cols_align(["l", "r"])
                        melee.add_rows([["Name", "Value"],
                                        ["Name", weapon["name"]],
                                        ["Attacks", weapon["attacks"]],
                                        ["Ballistic Skill", datasheet["stats"]["ballistic_skill"]],
                                        ["Strength", datasheet["stats"]["strength"]],
                                        ["Type", weapon["type"]],
                                        ["AP", weapon["ap"]],
                                        ["Damage", weapon["damage"]]])
                        print(melee.draw())
            else:
                print("No Melee Weapons found.")
            
            # Display abilities
            print("Abilities:")
            # Display core and faction abilities
            print ("Core Abilities:", datasheet["abilities"]["core"]["name"])
            print("Faction Ability:", datasheet["abilities"]["faction"]["name"])
            # Display datasheet ability
            if "datasheet" in datasheet["abilities"]:
                print("Datasheet ability:")
                # Loop through each datasheet ablility
                for i in range(1, 20):  # Assuming a maximum of 19 datasheet abilities
                    key = f"datasheet_ablility_{i}"
                    # If the weapon exists, display its stats
                    if key in datasheet["abilities"]["datasheet"]:
                        # Get datasheet ability data
                        ability = datasheet["abilities"]["datasheet"][key]
                        # Set up table for datasheet ability
                        datasheet_ability = Texttable()
                        datasheet_ability.set_deco(Texttable.HEADER)
                        datasheet_ability.set_cols_dtype(['t', 'a'])
                        datasheet_ability.set_cols_align(["l", "r"])
                        datasheet_ability.add_rows([["Name", "Value"],
                                        ["Name", ability["name"]],
                                        ["Description", ability["description"]]])
                        print(datasheet_ability.draw())
            else:
                print("No Datasheet Abilities found.")
            # Display wargear abilities
            if "wargear" in datasheet["abilities"]:
                print("Wargear:")
                for i in range(1, 20):  # Assuming a maximum of 19 wargear abilities
                    key = f"wargear_{i}"
                    # If the weapon exists, display its stats
                    if key in datasheet["wargear"]:
                        # Get wargear data
                        wargear_item = datasheet["wargear"][key]
                        # Set up table for wargear ability
                        wargear = Texttable()
                        wargear.set_deco(Texttable.HEADER)
                        wargear.set_cols_dtype(['t', 'a'])
                        wargear.set_cols_align(["l", "r"])
                        wargear.add_rows([["Name", "Value"],
                                        ["Description", wargear_item["description"]]])
                        print(wargear.draw())
            else:
                print("No Wargear Abilities found.")
            
            # Display wargear options
            if "wargear_options" in datasheet:
                print("Wargear Options:")
                print(*datasheet["wargear_options"], sep =',/n')
            else:
                print("No Wargear Options found.")
            
            # Display unit composition
            print("Unit Composition:")
            print(*datasheet["unit_composition"], sep =',/n')
            
            # Display keywords
            print("Keywords:")
            print(*datasheet["keywords"]["keywords"], sep =',/n')
            print("Faction Keywords:")
            print(datasheet["keywords"]["faction_keywords"])
            
            # Display lore
            print("Lore:")
            print(datasheet["lore"])
            """
        except json.JSONDecodeError:
            print(f"Error: '{chooseDatasheet}.json' is not a valid JSON file.")
        except Exception as e:
            print(f"Error loading datasheet: {e}")
    else:
        # Handle case where datasheet does not exist
        print(f"Datasheet '{chooseDatasheet}' not found. Check spelling and existance.")
        datasheetsfunct()

