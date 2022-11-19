"""
This is my version of the Silly Name Generator practice project from Impractical \
Python Projects. If run directly, it will print a random silly name \
and then prompt to be run again or exit. 
 
Functions:
    main() -> None
    make_a_name() -> string
    prompt() -> bool
"""

import sys
import random

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
         "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
         'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
         'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
         'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
         'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
         'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
         'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
         'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
         'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
         'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
         "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
         'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
         'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
         "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')


def main() -> None:
    """ Print a generated name and then prompt to repeat or exit. """
    while True:
        print(f"\n{make_a_name()}\n", file=sys.stderr)
        if prompt():
            continue
        else:
            sys.exit("\nK Bye\n")


def make_a_name() -> str:
    """Returns a random silly name as a string."""
    name = f"{random.choice(first)} {random.choice(last)}"
    return name


def prompt() -> bool:
    """Asks for 'y' or 'n' input to try again or exit."""
    while True:
        response = input("Try again? 'y' or 'n': ").lower()
        if response in ['y', 'n']:
            break

    return True if response == 'y' else False


if __name__ == "__main__":
    main()
