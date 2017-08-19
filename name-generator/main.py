import random

first_names = ['Abrielle', 'Adair', 'Adara', 'Adriel', 'Aiyana', 'Alissa', 'Alixandra', 'Altair', 'Amara', 'Anatola', 'Anya', 'Arcadia', 'Ariadne', 'Arianwen', 'Aurelia', 'Aurelian', 'Aurelius', 'Avalon', 'Acalia', 'Alaire', 'Auristela', 'Bastian', 'Breena', 'Brielle', 'Briallan', 'Briseis', 'Cambria', 'Cara', 'Carys', 'Caspian', 'Cassia', 'Cassiel', 'Cassiopeia', 'Cassius', 'Chaniel', 'Cora', 'Corbin', 'Cyprian', 'Daire', 'Darius', 'Destin', 'Drake', 'Drystan', 'Dagen', 'Devlin', 'Devlyn', 'Eira', 'Eirian', 'Elysia', 'Eoin', 'Evadne', 'Eliron', 'Evanth', 'Fineas', 'Finian', 'Fyodor', 'Gareth', 'Gavriel', 'Griffin', 'Guinevere', 'Gaerwn', 'Ginerva', 'Hadriel', 'Hannelore', 'Hermione', 'Hesperos', 'Iagan', 'Ianthe', 'Ignacia', 'Ignatius', 'Iseult', 'Isolde', 'Jessalyn', 'Kara', 'Kerensa', 'Korbin', 'Kyler', 'Kyra', 'Katriel', 'Kyrielle', 'Leala', 'Leila', 'Lilith',
               'Liora', 'Lucien', 'Lyra', 'Leira', 'Liriene', 'Liron', 'Maia', 'Marius', 'Mathieu', 'Mireille', 'Mireya', 'Maylea', 'Meira', 'Natania', 'Nerys', 'Nuriel', 'Nyssa', 'Neirin', 'Nyfain', 'Oisin', 'Oralie', 'Orion', 'Orpheus', 'Ozara', 'Oleisa', 'Orinthea', 'Peregrine', 'Persephone', 'Perseus', 'Petronela', 'Phelan', 'Pryderi', 'Pyralia', 'Pyralis', 'Qadira', 'Quintessa', 'Quinevere', 'Raisa', 'Remus', 'Rhyan', 'Rhydderch', 'Riona', 'Renfrew', 'Saoirse', 'Sarai', 'Sebastian', 'Seraphim', 'Seraphina', 'Sirius', 'Sorcha', 'Saira', 'Sarielle', 'Serian', 'Séverin', 'Tavish', 'Tearlach', 'Terra', 'Thalia', 'Thaniel', 'Theia', 'Torian', 'Torin', 'Tressa', 'Tristana', 'Uriela', 'Urien', 'Ulyssia', 'Vanora', 'Vespera', 'Vasilis', 'Xanthus', 'Xara', 'Xylia', 'Yadira', 'Yseult', 'Yakira', 'Yeira', 'Yeriel', 'Yestin', 'Zaira', 'Zephyr', 'Zora', 'Zorion', 'Zaniel', 'Zarek']
second_names = ['miller', 'lobb', 'thaker']
titles = ['the great', 'the bold', 'the magnificent', 'the incorigible',
          'the shield', 'the silent blade', 'the arcanist', 'the conjurer', 'the necromancer']

beginnings = ['a', 'be', 'de', 'el', 'fa', 'jo', 'ki',
              'la', 'ma', 'na', 'o', 'pa', 're', 'si', 'ta', 'va']
middles = ['bar', 'chef', 'dell', 'fat', 'gran', 'hal', 'jen', 'ke', 'lim', 'mor',
           'net', 'penn', 'quill', 'rond', 'sark', 'shen', 'tur', 'vash', 'yor', 'zen']
ends = ['a', 'ac', 'ai', 'al', 'am', 'an', 'ar', 'ea', 'el', 'er',
        'ess', 'egg', 'ett', 'ic', 'id', 'il', 'in', 'is', 'or', 'us', 'urd']


def random_name():
    fname = random.choice(first_names)
    lname = random.choice(second_names)
    title = random.choice(titles)
    return '{} {}'.format(fname, title)


# Later add some randomness to only use a beginning and middle or middle and end
def compose_name():
    a = random.choice(beginnings)
    b = random.choice(middles)
    c = random.choice(ends)
    return '{}{}{}'.format(a, b, c)


if __name__ == "__main__":
    for i in range(5):
        print(compose_name())
