from peewee import *

db = SqliteDatabase('mydb.db')

class City(Model):
	name = CharField()
	count_institution = IntegerField()
	is_relative = BooleanField()

	class Meta:
		database = db


class Institution(Model):
	name = CharField()
	owner = CharField()
	count_units = IntegerField()
	is_relative = BooleanField()

	class Meta:
		database = db
		table_name = 'ins'# This model uses the "people.db" database.

class Units(Model):
	owner = CharField()
	brand = CharField()
	type = CharField()
	s_number = CharField()
	r_number = CharField()
	count_hosts = IntegerField()
	is_relative = BooleanField()

	class Meta:
		database = db # this model uses the "people.db" database

class Hosts(Model):
	owner = CharField()
	number = CharField()
	name = CharField()
	mark = CharField()
	icon = CharField()
	period = CharField()
	mark_of_steel = CharField()
	
	class Meta:
		database = db
		
class Conclusions(Model):
	owner = CharField()
	number = CharField()
	type = CharField()
	name = CharField()
	reason = CharField()
	recommendatiton = CharField()
	photo = CharField()
	date_z = CharField()
	date_v = CharField()
	date_d = CharField()
	text = CharField()
	
	class Meta:
		database = db

class Users(Model):
	name = CharField()
	password = CharField()

	class Meta:
		database = db # this model uses the "people.db" database

db.connect()

#db.create_tables([Institution])
#db.create_tables([Units])
#db.create_tables([Users])
#db.create_tables([City])
#db.create_tables([Hosts])

#host = Hosts.create(owner='andrey', number='DZ-4443', name='gegeshe4ka', mark='sony', icon='/jpg.png', period='10', mark_of_steel='585')
#host = Hosts.create(owner='january', number='DZ-4443', name='gegeshe4ka', mark='sony', icon='/jpg.png', period='10', mark_of_steel='585')
#unit = Units.create(owner='ТЭЦ-5', brand='nani', type='kotel', s_number='january', r_number='MARCH', count_hosts=0, is_relative=True)
#admin = Users.create(name='roma', password='123')
#admin2 = Users.create(name='dima', password='123')
#tec_5 = Institution.create(name='ТЭЦ-5', owner='Омск', count_units=5, is_relative=True)
#tec_4 = Institution.create(name='ТЭЦ-4', owner='Омск', count_units=4, is_relative=True)
#tec_3 = Institution.create(name='ТЭЦ-3', owner='Омск', count_units=3, is_relative=True)
#city = City.create(name='Новосибирск', count_institution = 0, is_relative=True)

#city = Institution.select().get()
#grandma_ = Institution.get(Institution.name == 'ТЭЦ-5')

#print(Institution.select().get().name, Users.select().get().name)

#for person in Institution.select():
#	print(person.name, person.owner, person.count_units)

#for i in Users.select():
#	print(i.name, i.password)

#for i in City.select():
#	print(i.name, i.count_institution)
	
db.close()
