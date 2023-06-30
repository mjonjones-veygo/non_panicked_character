import names
from random import choice

def generate_race(race_options=['Human', 'Elf', 'Dwarf']):
    return choice(race_options)

def generate_class(class_options=['Paladin', 'Wizard', 'Rogue']):
    return choice(class_options)

def generate_background(backgrounds=['Sailor', 'Soldier', 'Acolyte']):
    return choice(backgrounds)

def generate_name(gender='male'):
    return names.get_full_name(gender=gender)

def generate_alignment():
    alignments = [
        'Chaotic Evil',
        'Chaotic Neutral',
        'Chaotic Good',
        'Neutral Evil',
        'Neutral Neutral',
        'Neutral Good',
        'Lawful Evil',
        'Lawful Neutral',
        'Lawful Good',
    ]
    return choice(alignments)
