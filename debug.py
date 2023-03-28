import ipdb
from lib import *

# Test your code below...
angelina = Actor("Angelina Jolie")
brad = Actor("Brad Pitt")
boomboom = Actor("Boomboom")

role1 = Role("Peter Pan")
role2 = Role("Captain Hook")
role3 = Role("Peter Pan")

a1 = Audition("San Fran", False, role2, angelina)
a2 = Audition("AK", False, role1, brad)
a3 = Audition("BOOMBOOM", True, role3, angelina)
a4 = Audition("YEA!", False, role1, boomboom)



# the below line allows us to stop & try stuff!
ipdb.set_trace()