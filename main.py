from dice.py import rollingDice# pyright: ignore[reportMissingImports]
from datasheets.py import datasheets# pyright: ignore[reportMissingImports]

def main():
    print ("select Function")
    print ("(D)ice or data(S)heets")
    diceOrDataSheet: str = input()
    
    if diceOrDataSheet in ("D", "d"):
        print ("amount of dice")
        amountOfDice = input()
        dice()
    elif diceOrDataSheet in ("S", "s"):
        datasheets()
