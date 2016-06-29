from django.db import models
from mongoengine import *

# Create your models here.

class Customer(DynamicDocument):
	email = StringField(max_length=100)
	name = StringField(max_length=100)
	meta = {'collection': 'customers'}
	

class Restaurant(DynamicDocument):
	location = StringField(max_length=100)
	name = StringField(max_length=100)
	meta = {'collection': 'restaurants'}    

class Beer(DynamicDocument):
	brand = StringField(max_length=100)
	restaurant = ObjectIdField
	customer = ObjectIdField
	meta = {'collection': 'bears'}