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
# along with this program.  If not, see <https://www.gnu.org/licenses/

import os
from pathlib import Path


# Create a user config directory for datasheets.
# This is intentionally created on import so users have a known location
# to drop their JSON files.
def get_config_dir():
    """Get the path to the config directory for datasheets.
    
    Returns:
        Path: The path to the config directory
    """
    if os.name == "nt":
        # Set config directory path for datasheets (Windows)
        appdata = os.getenv("APPDATA")
        if appdata is not None:
            base_dir = Path(appdata)
        else:
            # Fallback to the standard roaming AppData location under the user's home directory
            base_dir = Path.home() / "AppData" / "Roaming"
        CONFIG_DIR = base_dir / "WarhammerGadget" / "Datasheets"
    elif os.name == "posix":
        # Set config directory path for datasheets (macOS and Linux)
        CONFIG_DIR = Path.home() / ".config" / "warhammer-gadget" / "datasheets"
    else:
        raise RuntimeError(f"Unsupported operating system: {os.name}")
    return CONFIG_DIR

def ensure_config_dir():
    """Create a user config directory for datasheets if it doesn't exist.
    
    Returns:
        Path: The path to the config directory
    """
    config_dir = get_config_dir()
    # Create the config directory if it doesn't exist
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir

# Call the function to create the directory on import
ensure_config_dir()
__all__ = ["get_config_dir", "ensure_config_dir"]
