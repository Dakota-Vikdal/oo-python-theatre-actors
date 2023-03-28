
class Audition:

    all = []

    def __init__(self, location, hired, role_instance, actor_instance):
        self.location = location
        self.hired = hired
        self.role = role_instance
        self.actor = actor_instance
        Audition.all.append(self)

# `Audition#call_back()` will change the the hired attribute to `True`.
    def call_back(self):
        self.hired = True