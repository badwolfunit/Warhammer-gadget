# Written by Bawolfunit
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

from .rollingdice import rollingDicefunct
from .datasheets import datasheets


def licenseInfo():
    """Prints license and copyright information to the user."""
    print("Warhammer-gadget  Copyright (C) 2026  Luca Smith(Badwolfunit). This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions.")


def main():
    """Main entry point for the Warhammer Gadget application.
    
    Prompts the user to select between dice rolling or datasheet viewing functionality.
    """
    # Asks user what function they want to use
    print("Select Function")
    print("(D)ice or data(S)heets")
    # Get user input
    diceOrDataSheet: str = input()
    
    # Activated function based on user input
    if diceOrDataSheet in ("D", "d"):
        # Activate dice rolling function
        rollingDicefunct()
        
    elif diceOrDataSheet in ("S", "s"):
        # Activate datasheet function
        datasheets()
    else:
        # Invalid input handler
        print("Invalid input, please try again")
        main()


if __name__ == "__main__":
    licenseInfo()
    main()