from django.db import models
from mongoengine import *

# Customer Model.

class Customer(DynamicDocument):
	email = StringField(max_length=100)
	name = StringField(max_length=100)
	meta = {'collection': 'customers'}

# Restaurant Model.

class Restaurant(DynamicDocument):
	location = StringField(max_length=100)
	name = StringField(max_length=100)
	meta = {'collection': 'restaurants'}

# Customer Beer Model.

class Beer(DynamicDocument):
	brand = StringField(max_length=100)
	restaurant = ObjectIdField
	customer = ObjectIdField
	meta = {'collection': 'bears'}