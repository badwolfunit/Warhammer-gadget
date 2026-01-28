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
import texttable

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
        except json.JSONDecodeError:
            print(f"Error: '{chooseDatasheet}.json' is not a valid JSON file.")
        except Exception as e:
            print(f"Error loading datasheet: {e}")
    else:
        # Handle case where datasheet does not exist
        print(f"Datasheet '{chooseDatasheet}' not found. Check spelling and existance.")
        datasheets()
        
