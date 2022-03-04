
import sqlite3
from subprocess import CREATE_NEW_CONSOLE

conn = sqlite3.connect('ZombieTracker2.db')
cursor = conn.cursor()



Zombie_name = input("Enter zombies name:\n")
Zombie_age = input("Zombies age:\n")
Zombie_type = input("Zombies type:\n")
Zombie_location = input("Zombies location:\n")
Zombie_specialty = input("Zombies specailty:\n")
Eat_brains = input("Yes or No:\n")




#cursor.execute('''INSERT INTO ZombieTracker (Name, Age, Type, Location, Specialty, Brains) 
#VALUES
#''',(Zombie_name, Zombie_age, Zombie_type, Zombie_location, Zombie_specialty, Eat_brains))

conn.execute("INSERT INTO ZombieTracker(Name, Age, Type, Location, Brains, Specialty)\
    VALUES(Zombie_name, Zombie_age, Zombie_type, Zombie_location, Zombie_specialty, Eat_brains)")

#conn.execute("INSERT INTO zombie (ID, name, age, type, location, brains, specialty)\
    #VALUES(001, 'Ninja', 99, 'Blue Walker', 'Ottawa', FALSE, 'Igloos')")


#### Did it work? Probably not.

conn.commit()








