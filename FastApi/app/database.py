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



class CategoryModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "categories"


class OrderModel(Model):
    id = AutoField(primary_key=True)
    customer_id = CharField(max_length=50)
    products = CharField(max_length=50)
    total = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "orders"



class PaymentModel(Model):
    id = AutoField(primary_key=True)
    order_id = CharField(max_length=50)
    payment_method = CharField(max_length=50)
    amount = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "payments"



class ProductModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    price = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "products"