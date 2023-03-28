from .audition import Audition

class Actor:
    def __init__(self, name):
        self.name = name

# `Actor#auditions` returns a list of auditions this actor attended.
    @property
    def auditions(self):
        return [a for a in Audition.all if a.actor == self]


# `Actor#roles` returns a list of roles the actor auditioned for.
    @property
    def role_method(self):
        return [a.role for a in self.auditions]

# `Actor#characters` returns a list of strings with all the 
#  different character names this actor auditioned for.
    @property
    def characters(self):
        character_names = []
        for character in Audition.all:
            if character.actor == self:
                character_names.append(character.role)
        return character_names



#  Actor#paychecks` returns a list of strings with all the 
#  different character names that this actor has been **hired** for.

#  make sure to create a list and append the character names onto that list
    @property
    def paycheck(self):
        hired_list = []
        for a in self.auditions:
            if a.hired == True:
                hired_list.append(a.role)
        return hired_list



