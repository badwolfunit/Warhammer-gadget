from pathlib import Path


# Ensure the config directory exists on import so users can drop JSON files there
CONFIG_DIR = Path.home() / ".config" / "warhammer-gadget" / "datasheets"
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
__all__ = ["CONFIG_DIR"]