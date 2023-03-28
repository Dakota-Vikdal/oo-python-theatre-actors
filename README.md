# Actor's Theater Work

  
***

Actor --------< Auditions >---------- Role


## Introduction

The Flatiron Theater Company is holding auditions!

An Actor may `Audition` for many `Roles`, while a `Role` may have many `Auditions` for it & many `Actors` through Auditions!

&nbsp;

# Actor ----< Audition >---- Role

&nbsp;

## Getting started


- `Auditions` should have a location (string), hired (boolean), **belong to** a role, and **belong to** an actor.
- `Roles` should only have a character_name (string), **have many** auditions, and **have many** actors **through** auditions.
- `Actors` should only have name ( string ), **have many** auditions, and **have many** roles **through** auditions. 

## Relationship

- What relationships will this need (i.e. one-to-one, one-to-many, and
  many-to-many)?

## A note about notation

- When you see a `"#"` the functionality is related to the instance, a `"."` the class.

## Testing

- You can now view all of your Python files for your models in the lib folder. They will be automagically available for you so long as you use the `python debug.py` instruction to test your code.

- Through this `debug.py` file, we've provided to you a console that you can use to test your code. To enter a console session, run `python debug.py` from the command line. You'll be able to test out the functionality that you write there.

---

## Audition

-DONE! `Audition#role` returns an instance of role associated with this audition.
-DONE!`Audition#actor` returns an instance of actor associated with this audition.
-DONE! `Audition#call_back()` will change the the hired attribute to `True`.

## Actor

-DONE! `Actor#auditions` returns a list of auditions this actor attended.
-DONE! `Actor#roles` returns a list of roles the actor auditioned for.
- `Actor#characters` returns a list of strings with all the 
different character names this actor auditioned for.
- `Actor#paychecks` returns a list of strings with all the 
different character names that this actor has been **hired** for.


## Roles

-DONE! `Role#auditions` returns all of the auditions associated with this role.
-DONE! `Role#actors` returns a list of names from the actors associated with this role.
-DONE! `Role#locations` returns a list of locations from the auditions associated
  with this role.
-DONE! `Role.silver_screen` returns a unique list of strings for all the character names who have been hired.
