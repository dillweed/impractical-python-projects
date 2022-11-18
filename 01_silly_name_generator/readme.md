# Pseudocode for Silly Name Generator

## Objective

User should run the program from the command line to generate a first last name combination randomly selected from saved lists. The generated full name will display as stdout.

## Steps

1. Import sys and random
1. Load a tuple of first names.
1. Load a tuple of last names.
1. Use random choice to pick an item from each.
1. Print first last with a space inbetween using red font with `print(something, file=sys.stderr)`.
1. Ask user to play again or quit.
1. Repeat if "y" is entered.
1. Quit using sys.exit("Goodbye message").
