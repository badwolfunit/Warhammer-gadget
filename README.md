# Warhammer Gadget

A compact digital toolbox designed to enhance your Warhammer gaming experience. This application provides utilities for managing datasheets, rolling dice, and more through a text-based user interface (TUI).

## Features

- **Datasheet Management**: Load and view unit datasheets in JSON format
- **Dice Rolling**: Quick and easy dice rolling functionality
- **TUI Interface**: Clean terminal-based interface for PC

## Future Goals

The vision is to build a physical device around the size of a paperback book (or smaller) that can:
- Display datasheets (respecting copyright laws)
- Include a built-in tape measure
- Feature a small detachable laser pointer for line-of-sight checks
- Use a simple directional button interface (left, right, up, down, and OK)

Hardware concepts include using a Raspberry Pi with integrated measurement tools.

## Installation

### Using pip

```bash
pip install warhammer-gadget
```

### From Source

```bash
git clone https://github.com/badwolfunit/Warhammer-gadget.git
cd Warhammer-gadget
pip install -e .
```

## Usage

Run the application:

```bash
warhammer-gadget
```

### Adding Datasheets

Datasheets are stored as JSON files in `~/.config/warhammer-gadget/datasheets/`. 

A template datasheet is available in `warhammer_gadget/datasheet_template/template_datasheet.json` to help you create your own.

**Note**: Users must provide their own datasheets. This software does not include any copyrighted content.

## Development

This is an early-stage project, primarily designed for Warhammer 40K. Currently implemented as a Python TUI application for PC, with plans to expand to embedded hardware in the future.

# Legal stuff
## Disclaimer

Warhammer is a trademark of Games Workshop Ltd.
This project is not affiliated with, endorsed by, or associated with Games Workshop in any way.
## License
This code is licensed under the GNU General Public License v3.0.
Copyright © 2026 Luca Smith (Badwolfunit).
