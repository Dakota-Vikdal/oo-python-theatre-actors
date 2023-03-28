from .audition import Audition

class Role:

    all = []

    def __init__(self, character_name):
        self.name = character_name
        Role.all.append(self)



# `Role#auditions` returns all of the auditions associated with this role.
    @property
    def auditions_role(self):
        return [a for a in Audition.all if a.role == self]

#  Role#actors` returns a list of names from the actors associated with 
#  this role.
    @property
    def actors(self):
        return [n.actor for n in Audition.all if n.role == self]

#  `Role#locations` returns a list of locations from the auditions associated
#   with this role.
    @property
    def locations(self):
        return [a.location for a in Audition.all if a.role == self]

#  `Role.silver_screen` returns a unique list of strings for all the character names who have been hired.

    # @classmethod
    # def silver_screen(cls):
        # return list({c.name for c in Role.all if c.hired == True})

    @classmethod
    def silver_screen(cls):
        hhhired = list({c.name for c in cls.all})
        for character in Audition.all:
            if character.hired == True:
                hired = character.role.name
                return hhhired
        else: 
            print("Uh oh!")


