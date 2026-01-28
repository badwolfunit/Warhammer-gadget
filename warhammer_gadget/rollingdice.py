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

import dice


def rollingDicefunct():
    # Asks user for amount of dice to roll and rolls them
    print("Amount of dice to roll?")
    amountOfDice: str = input()
    
    try:
        # Validate input is a positive integer
        num_dice = int(amountOfDice)
        if num_dice <= 0:
            print("Please enter a positive number of dice.")
            return
        
        # Use validated integer value for rolling
        results = dice.roll(str(num_dice) + 'd6')
        # Prints results
        print(results)
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"Error rolling dice: {e}")
