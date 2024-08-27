from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"



class LibraryModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    category = CharField(max_length=50)
    color = CharField(max_length=50)
    author = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "libraries"


class CarModel(Model):
    id = AutoField(primary_key=True)
    planeNumber = CharField(max_length=50)
    type = CharField(max_length=50)
    color = CharField(max_length=50)
    cilindraje = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "cars"



class BankModel(Model):
    id = AutoField(primary_key=True)
    number = CharField(max_length=50)
    user = CharField(max_length=50)
    balance = CharField(max_length=50)
    type = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "banks"



class AnimalModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    species = CharField(max_length=50)
    age = CharField(max_length=50)
    weight = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "animals"