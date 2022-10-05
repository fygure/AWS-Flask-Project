# Project to demonstrate skills
# Maximillian Chalitsios 10/2/2022
#===========================================================================#
from urllib import response
import app.data_scripting.iam_functions as iam_functions
import psycopg2
from psycopg2 import OperationalError
from dotenv import dotenv_values
import requests
#===========================================================================#
"""Azure to script connection"""
config = dotenv_values("app/data_scripting/.env")
DB_NAME = config["DB_NAME"]
DB_USER = config["DB_USER"]
DB_PW = config["DB_PW"]
DB_HOST = config["DB_HOST"]
DB_PORT = config["DB_PORT"]

AZURE_SUB_ID=config["AZURE_SUB_ID"]
AZURE_RS_GR=config["AZURE_RS_GR"]
AZURE_SRV_NAME=config["AZURE_SRV_NAME"]
AZURE_DB_NAME=config["AZURE_DB_NAME"]

#===========================================================================#
# Function that returns connection string built
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None;
    try:
        connection = psycopg2.connect(
            database = db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            sslmode = "require"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as err:
        print(f"The error '{err}' occured")
    return connection
#===========================================================================#
# Create connection to PostgreSQL database (on Azure)
# moved below to main.py
#connection = create_connection(DB_NAME, DB_USER, DB_PW, DB_HOST, DB_PORT)
#===========================================================================#
# Not needed, just utilize psycopg2
# link = f"https://management.azure.com/subscriptions/{AZURE_SUB_ID}/resourceGroups/{AZURE_RS_GR}/providers/Microsoft.DBforPostgreSQL/servers/{AZURE_SRV_NAME}/databases/{AZURE_DB_NAME}?api-version=2017-12-01"
# def put_data(user_obj):
#     try:
#         data = {
#             'UserName': user_obj.username,
#             'User_ID': user_obj.user_ID,
#             'User_ARN':user_obj.user_arn,
#             'Date_Created': user_obj.date_created,
#             'User_Groups': user_obj.user_groups
#         }
#         response = requests.put(link, data = data)
#         print("success")
        
#     except OperationalError as err:
#         print(f"The error '{err}' occured")
#===========================================================================#

