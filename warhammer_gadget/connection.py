# Written by Bawolfunit
# This program is designed to help run warhammer games by using digital features. Will try to build a device built around this program. Datasheets must be provided by user
# Copyright (C) 2026  Luca Smith(Badwolfunit)
# Disclaimer:
# Warhammer is a trademark of Games Workshop Ltd. This project is not affiliated with, endorsed by, or associated with Games Workshop in any way. It is a fan-made, non-profit project.
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

from .datasheets import datasheetsfunct
from .rollingdice import rollingDicefunct
from .rollingdice import rollingDiceAPI

def connection():
    # Display the datasheet to user
    datasheet = datasheetsfunct()
    print("Enter weapon to attack with:")
    weapon = input("Weapon: ")
    # Find the weapon
    for i in range(1, 20):
        if datasheet is None:
            print("Aborting process.")
            return
        weaponcheck = datasheet[weapon]
        # Check if the weapon is a ranged weapon
        ranged_key = f"ranged_{i}"
        melee_key = f"melee_{i}"
        if weapon == weaponcheck["ranged"][ranged_key]["name"]:
            print(f"Weapon found: {weaponcheck['ranged'][ranged_key]['name']}")
            # Rolling balistic skill check
            try:
                print("Rolling dice for ballistic skill...")
                balisticsCheck = rollingDiceAPI(weaponcheck["ranged"][ranged_key]["attacks"])
                # Checks for sucess
                hits = 0
                if balisticsCheck is None:
                    return
                for i in balisticsCheck:
                    if i >= weaponcheck["ranged"][ranged_key]["hit"]:
                        hits += 1
                print(f"Number of hits: {hits}")
                print("Enter the target units toughness:")
                targetToughness = int(input("Toughness: "))
                # Rolling wound check
                print("Rolling dice for wound check...")
                woundCheck = rollingDiceAPI(hits)
                # Checks for sucess
                if woundCheck is None:
                    return
                wounds = 0
                # Compare toughness and strength and determine wounds
                if targetToughness >= 2*weaponcheck["ranged"][ranged_key]["strength"]:
                    for i in woundCheck:
                        if i >= 6:
                            wounds += 1
                elif targetToughness > weaponcheck["ranged"][ranged_key]["strength"]:
                    for i in woundCheck:
                        if i >= 5:
                            wounds += 1
                elif targetToughness == weaponcheck["ranged"][ranged_key]["strength"]:
                    for i in woundCheck:
                        if i >= 4:
                            wounds += 1
                elif targetToughness < weaponcheck["ranged"][ranged_key]["strength"]:
                    for i in woundCheck:
                        if i >= 3:
                            wounds += 1
                elif 2*targetToughness <= weaponcheck["ranged"][ranged_key]["strength"]/2:
                    for i in woundCheck:
                        if i >= 2:
                            wounds += 1
                print(f"Number sucessful wounds: {wounds}")
                print("The weapon has an armour piercing value of: " + str(weaponcheck["ranged"][ranged_key]["ap"]))
                print("Please allow your opponent to roll for saves. If they have an invulnerable save, they may use that instead of their normal save.")
                unsaved = input("How many wounds were unsaved?")
                damage = int(unsaved)*weaponcheck["ranged"][ranged_key]["damage"]
                print(f"Total damage dealt: {damage}")
            except Exception as e:
                print(f"Error rolling dice: {e}")
        elif weapon == weaponcheck["melee"][melee_key]["name"]:
            print(f"Weapon found: {weaponcheck['melee'][melee_key]['name']}")
            # Rolling weapon skill check
            try:
                print("Rolling dice for attacks...")
                attacksCheck = rollingDiceAPI(weaponcheck["melee"][melee_key]["attacks"])
                # Checks for sucess
                hits = 0
                if attacksCheck is None:
                    return
                for i in attacksCheck:
                    if i >= weaponcheck["melee"][melee_key]["weapon_skill"]:
                        hits += 1
                print(f"Number of hits: {hits}")
                print("Enter the target units toughness:")
                targetToughness = int(input("Toughness: "))
                # Rolling wound check
                print("Rolling dice for wound check...")
                woundCheck = rollingDiceAPI(hits)
                # Checks for sucess
                if woundCheck is None:
                    return
                wounds = 0
                # Compare toughness and strength and determine wounds
                if targetToughness >= 2*weaponcheck["melee"][melee_key]["strength"]:
                    for i in woundCheck:
                        if i >= 6:
                            wounds += 1
                elif targetToughness > weaponcheck["melee"][melee_key]["strength"]:
                    for i in woundCheck:
                        if i >= 5:
                            wounds += 1
                elif targetToughness == weaponcheck["melee"][melee_key]["strength"]:
                    for i in woundCheck:
                        if i >= 4:
                            wounds += 1
                elif targetToughness < weaponcheck["melee"][melee_key]["strength"]:
                    for i in woundCheck:
                        if i >= 3:
                            wounds += 1
                elif 2*targetToughness <= weaponcheck["melee"][melee_key]["strength"]/2:
                    for i in woundCheck:
                        if i >= 2:
                            wounds += 1
                print(f"Number sucessful wounds: {wounds}")
                print("The weapon has an armour piercing value of: " + str(weaponcheck["melee"][melee_key]["ap"]))
                print("Please allow your opponent to roll for saves. If they have an invulnerable save, they may use that instead of their normal save.")
                unsaved = input("How many wounds were unsaved?")
                damage = int(unsaved)*weaponcheck["melee"][melee_key]["damage"]
                print(f"Total damage dealt: {damage}")
            except Exception as e:
                print(f"Error rolling dice: {e}")
        


