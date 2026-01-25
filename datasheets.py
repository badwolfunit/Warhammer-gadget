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

import json
import os
from pathlib import Path

def datasheets():
    # Lists available datasheets and allows user to select one to load
    print(f"Here are the available datasheets:")
    datasheets_dir = Path.home() / ".config" / "warhammer-gadget" / "datasheets"
    datasheet_files = [f for f in os.listdir(datasheets_dir) if f.endswith('.json')]
    print(datasheet_files)
    # Get user input for which datasheet to load
    chooseDatasheet: str = input("Enter the name of the datasheet you want to load (without .json extension): ")
    # Create full path to datasheet
    datasheetPath = datasheets_dir / f"{chooseDatasheet}.json"
    if datasheetPath.exists():
        # Loads selected datasheet
        with open(datasheetPath) as f:
            datasheet = json.load(f)
            # Confirm successful load
        print(f"Datasheet '{chooseDatasheet}' loaded successfully.")
        # Print datasheet content
        print(json.dumps(datasheet, indent=4))
    else:
        # Handle case where datasheet does not exist
        print(f"Datasheet '{chooseDatasheet}' not found.")