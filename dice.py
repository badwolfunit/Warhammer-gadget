import dice


def dice(a):
    print ("amount of dice")
    amountOfDice: str = input()
    results = dice.roll(amountOfDice + 'd6')
    print (results)
