"""Warhammer datasheets in JSON format."""

import json
from pathlib import Path


def load_datasheet(name: str) -> dict:
    """Load a datasheet from the datasheets_data folder."""
    datasheet_path = Path(__file__).parent / f"{name}.json"
    if not datasheet_path.exists():
        raise FileNotFoundError(f"Datasheet '{name}' not found at {datasheet_path}")
    
    with open(datasheet_path, "r") as f:
        return json.load(f)


__all__ = ["load_datasheet"]
