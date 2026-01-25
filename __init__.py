#Written by Bawolfunit
# This program is designed to help run warhammer games by using digital features. Will try to build a device built around this program. Datasheets must be provided by user
#Copyright (C) 2026  Luca Smith(Badwolfunit)
#Disclaimer:
#Warhammer is a trademark of Games Workshop Ltd. This project is not affiliated with, endorsed by, or associated with Games Workshop in any way.
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/

from pathlib import Path


# Create a user config directory for datasheets.
# This is intentionally created on import so users have a known location
# to drop their JSON files.
def ensure_config_dir():
    # Create config directory for datasheets
    CONFIG_DIR = Path.home() / ".config" / "warhammer-gadget" / "datasheets"
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    return CONFIG_DIR

# Call the function
ensure_config_dir()
__all__ = ["ensure_config_dir"]