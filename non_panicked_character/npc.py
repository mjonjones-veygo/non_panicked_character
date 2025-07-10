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

def generate_backstory(backstories=None):
    if backstories is None:
        backstories = [
            'Once served as a royal guard but was framed for treason and fled into exile',
            'Grew up as an orphan on the streets, learning to survive through wit and cunning',
            'Was raised by monks in a secluded monastery before venturing into the world',
            'Lost their family in a dragon attack and now seeks revenge against all dragonkind',
            'Former merchant who lost everything in a bad deal and turned to adventuring',
            'Discovered they have mysterious magical powers that they struggle to control',
            'Was cursed by a witch and seeks a way to break the enchantment',
            'Comes from a long line of heroes but feels the weight of living up to their legacy',
            'Fled their homeland after accidentally causing a great catastrophe',
            'Was once a noble but gave up their title to pursue a life of adventure',
            'Saved a village from bandits and discovered their calling as a protector',
            'Haunted by visions of the future that they cannot understand or control',
            'Seeks to restore their family honor after a great scandal',
            'Was betrayed by their closest friend and now has trust issues',
            'Raised by a different race and struggles with their identity',
            'Lost their memory and adventures seeking clues about their past',
            'Made a pact with a powerful entity that they now regret',
            'Witnessed a terrible injustice that sparked their desire for justice',
            'Comes from a family of criminals but chose a different path',
            'Was shipwrecked on a mysterious island and barely escaped with their life'
        ]
    return choice(backstories)
