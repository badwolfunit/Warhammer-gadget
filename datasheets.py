import json

from warhammer_gadget.datasheets_data import CONFIG_DIR
"""
The function `load_datasheet` loads a datasheet from a specified folder in JSON format.
    
:param name: The `name` parameter in the `load_datasheet` function is a string that represents the
name of the datasheet you want to load. It is used to construct the path to the datasheet file by
appending ".json" to the name and looking for the file at that path in the `
:type name: str
:return: The `load_datasheet` function returns a dictionary containing the data loaded from the
specified datasheet file in JSON format.
"""

def load_datasheet(name: str) -> dict:
    datasheet_path = CONFIG_DIR / f"{name}.json"
    if not datasheet_path.exists():
        raise FileNotFoundError(f"Datasheet '{name}' not found at {datasheet_path}")
    
    with open(datasheet_path, "r") as f:
        return json.load(f)


__all__ = ["load_datasheet"]
