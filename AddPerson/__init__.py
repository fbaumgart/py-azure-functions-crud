import logging
import json
import pyodbc
import azure.functions as func

server = '<insert_server_name>'
database = '<insert_DB_name>'
username = '<insert_username>'
password = '<insert_password>'
driver= '{ODBC Driver 17 for SQL Server}'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        request_json = req.get_json()
        name = request_json.get('first_name')
        surname = request_json.get('last_name')
        phone_number = request_json.get('phone_number')
    except:
        return func.HttpResponse(
            "Please put a valid JSON in the request",
            status_code=400
        )
    
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO PERSON VALUES (?, ?, ?)", name, surname, phone_number)
    cursor.commit()
    
    return func.HttpResponse(
        "User added",
        status_code=201
    )
