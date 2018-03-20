from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.
class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database
        
db.connect()
db.create_tables([Person, Pet])
db.close()
from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
#uncle_bob.save() # bob is now stored in the database
# Returns: 1
grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
#herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

#grandma.name = 'Grandma L.'
#grandma.save()  # Update grandma's name in the database.
# Returns: 1

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
#herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
#herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
#herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

#herb_mittens.delete_instance() # he had a great life
# Returns: 1

#herb_fido.owner = uncle_bob
#herb_fido.save()
#bob_fido = herb_fido # rename our variable for clarity

grandma = Person.select().where(Person.name == 'Grandma L.').get()
grandma_ = Person.get(Person.name == 'Grandma L.')

for person in Person.select():
    print(person.name, person.pets.count(), 'pets')
