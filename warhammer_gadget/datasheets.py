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
from texttable import Texttable
from . import get_config_dir


def datasheetsfunct():
    # Lists available datasheets and allows user to select one to load
    print("Here are the available datasheets:")
    datasheets_dir = get_config_dir()
    
    # Check if directory exists
    if not datasheets_dir.exists():
        print(f"No datasheets directory found. Please add datasheets to {datasheets_dir}")
        return
    
    datasheet_files = [f for f in os.listdir(datasheets_dir) if f.endswith('.json')]
    
    if not datasheet_files:
        print(f"No datasheets found. Please add JSON files to {datasheets_dir}")
        return
        
    print(datasheet_files)
    # Get user input for which datasheet to load
    chooseDatasheet: str = input("Enter the name of the datasheet you want to load (without .json extension). For raw JSON suffix the filename with \" RAW\". Note the space in front of RAW:")
    # Prepare the string for later steps
    checkDatasheet = chooseDatasheet.split()
    # Handle empty or whitespace-only input safely
    if not checkDatasheet:
        print("No datasheet name entered. Please enter a valid datasheet name.")
        datasheetsfunct()
        return
    # Create full path to datasheet
    datasheetPath = datasheets_dir / f"{checkDatasheet[0]}.json"
    
    if datasheetPath.exists():
        
        try:
            # Loads selected datasheet
            with open(datasheetPath) as f:
                datasheet = json.load(f)
            # Confirm successful load
            print(f"Datasheet '{chooseDatasheet}' loaded successfully.")
            # Print raw datasheet content
            if len(checkDatasheet) > 1 and checkDatasheet[1].upper() == "RAW":
                print(json.dumps(datasheet, indent=4))
            else:
                # Print formated datasheet content
                # Display base stats
                print(f"\nDatasheet Name: {datasheet['unit_name']}")
                print(f"\nBase Stats:")
                # Loads base stats into a table
                base_stats = Texttable()
                base_stats.set_deco(Texttable.HEADER)
                base_stats.set_cols_dtype(['t', 'a'])
                base_stats.set_cols_align(["l", "r"])
                # Table generation if the unit has an invulnerable save
                if datasheet["stats"]["invulnerable_save"] is not None:
                    base_stats.add_rows([["Name", "Value"],
                                         ["Movement", str(datasheet["stats"]["movement"])+'"'],
                                         ["Toughness", datasheet["stats"]["toughness"]],
                                         ["Wounds", datasheet["stats"]["wounds"]],
                                         ["Leadership", str(datasheet["stats"]["leadership"])+"+"],
                                         ["Save", str(datasheet["stats"]["save"])+"+"],
                                         ["Objective Control", datasheet["stats"]["objective_control"]],
                                         ["Invulnerable Save", str(datasheet["stats"]["invulnerable_save"])+"+"]])
                # Table generation if the unit doesn't have an invulnerable save
                else:
                    base_stats.add_rows([["Name", "Value"],
                                         ["Movement", str(datasheet["stats"]["movement"])+'"'],
                                         ["Toughness", datasheet["stats"]["toughness"]],
                                         ["Wounds", datasheet["stats"]["wounds"]],
                                         ["Leadership", str(datasheet["stats"]["leadership"])+"+"],
                                         ["Save", str(datasheet["stats"]["save"])+"+"],
                                         ["Objective Control", datasheet["stats"]["objective_control"]],
                                         ["Invulnerable Save", datasheet["stats"]["invulnerable_save"]]])
                print(base_stats.draw())
            
                # Display ranged weapons
                print(f"\nWeapons:")
                # Check if there are ranged weapons
                if "ranged" in datasheet["weapons"]:
                    print(f"Ranged Weapons:")
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
                            if weapon["ballistic_skill"] is not None:
                                ranged.add_rows([["Name", "Value"],
                                                 ["Name", weapon["name"]],
                                                 ["Range", str(weapon["range"])+'"'],
                                                 ["Attacks", weapon["attacks"]],
                                                 ["Ballistic Skill", str(weapon["ballistic_skill"]) + "+"],
                                                 ["Strength", weapon["strength"]],
                                                 ["Type", ", ".join(weapon["type"])],
                                                 ["AP", "-"+str(weapon["ap"])],
                                                 ["Damage", weapon["damage"]]])
                            else:
                                ranged.add_rows([["Name", "Value"],
                                                 ["Name", weapon["name"]],
                                                 ["Range", str(weapon["range"])+'"'],
                                                 ["Attacks", weapon["attacks"]],
                                                 ["Ballistic Skill", "N/A"],
                                                 ["Strength", weapon["strength"]],
                                                 ["Type", ", ".join(weapon["type"])],
                                                 ["AP", "-"+str(weapon["ap"])],
                                                 ["Damage", weapon["damage"]]])
                            print(ranged.draw())
                else:
                    print("No Ranged Weapons found.")
            
                # Display melee weapons
                # Check if there are melee weapons
                if "melee" in datasheet["weapons"]:
                    print(f"\nMelee Weapons:")
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
                                            ["Weapon Skill", str(weapon["weapon_skill"]) + "+"],
                                            ["Strength", weapon["strength"]],
                                            ["Type", ", ".join(weapon["type"])],
                                            ["AP", "-"+str(weapon["ap"])],
                                            ["Damage", weapon["damage"]]])
                            print(melee.draw())
                else:
                    print("No Melee Weapons found.")
            
                # Display abilities
                print(f"\nAbilities:")
                # Display core abilities
                if "core" in datasheet["abilities"]:
                    print(f"Core Abilities:")
                    print(*datasheet['abilities']['core'], sep=', ')
                else:
                    print("No Core Abilities found.")
                # Display faction ability
                if "faction" in datasheet["abilities"]:
                    print(f"\nFaction Ability: {datasheet['abilities']['faction']['name']}")
                else:
                    print("No Faction Ability found.")
                # Display datasheet ability
                if "datasheet" in datasheet["abilities"]:
                    print(f"\nDatasheet ability:")
                    # Loop through each datasheet ability
                    for i in range(1, 20):  # Assuming a maximum of 19 datasheet abilities
                        key = f"datasheet_ability_{i}"
                        # If the ability exists, display its details
                        if key in datasheet["abilities"]["datasheet"]:
                            # Get datasheet ability data
                            ability = datasheet["abilities"]["datasheet"][key]
                            # Set up table for datasheet ability
                            datasheet_ability = Texttable()
                            datasheet_ability.set_deco(Texttable.HEADER)
                            datasheet_ability.set_cols_dtype(['t', 'a'])
                            datasheet_ability.set_cols_align(["l", "r"])
                            datasheet_ability.add_rows([["Name",          "Description"],
                                                        [ability["name"], ability["description"]]])
                            print(datasheet_ability.draw())
                else:
                    print("No Datasheet Abilities found.")
                # Display wargear abilities
                if "wargear" in datasheet["abilities"]:
                    print(f"\nWargear:")
                    for i in range(1, 20):  # Assuming a maximum of 19 wargear abilities
                        key = f"wargear_{i}"
                        # If the wargear ability exists, display its stats
                        if key in datasheet["abilities"]["wargear"]:
                            # Get wargear data
                            wargear_item = datasheet["abilities"]["wargear"][key]
                            # Set up table for wargear ability
                            wargear = Texttable()
                            wargear.set_deco(Texttable.HEADER)
                            wargear.set_cols_dtype(['t', 'a'])
                            wargear.set_cols_align(["l", "r"])
                            wargear.add_rows([["Name",               "Description"],
                                              [wargear_item["name"], wargear_item["description"]]])
                            print(wargear.draw())
                else:
                    print("No Wargear Abilities found.")
            
                # Display wargear options
                if "wargear_options" in datasheet:
                    print(f"\nWargear Options:")
                    print(*datasheet["wargear_options"], sep =',\n')
                else:
                    print("No Wargear Options found.")
            
                # Display unit composition
                print(f"\nUnit Composition:")
                print(*datasheet["unit_composition"], sep =',\n')
            
                # Display transport rules if they exist
                if "transport" in datasheet:
                    print(f"\nTransport Rules:")
                    print(*datasheet["transport"], sep =',\n')
                
                # Display damaged characteristics if they exist
                if "damaged" in datasheet:
                    print(f"\nDamaged Characteristics:")
                    print(f"Damaged Range: {datasheet['damaged']['damaged_range']}")
                    print(f"Damaged Rule: {datasheet['damaged']['damaged_rule']}")

                # Display leader rules if they exist
                if "leader" in datasheet:
                    print(f"\nLeader:")
                    print(datasheet["leader"]["leader"])
                # Display keywords
                print(f"\nKeywords:")
                print(*datasheet["keywords"]["keywords"], sep =',\n')
                print("Faction Keywords:")
                print(datasheet["keywords"]["faction_keywords"])
            
                # Display lore
                if "lore" in datasheet:
                    print(f"\nLore:")
                    print(datasheet["lore"])
                else:
                    print("No Lore found.")
        
                return datasheet
            # Error handling
        except json.JSONDecodeError:
            print(f"Error: '{chooseDatasheet}.json' is not a valid JSON file.")
            return None
        except Exception as e:
            print(f"Error loading datasheet: {e}")
            return None
        
        
    
    else:
        # Handle case where datasheet does not exist
        print(f"Datasheet '{chooseDatasheet}' not found. Check spelling and existence.")
        datasheetsfunct()
    
    

