import logging
import pyodbc
import json
import azure.functions as func

server = '<insert_server_name>'
database = '<insert_DB_name>'
username = '<insert_username>'
password = '<insert_password>'
driver= '{ODBC Driver 17 for SQL Server}'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM PERSON")
    row = cursor.fetchone()
    json_list = list()
    while row:
        person_id = str(row[0])
        person_first_name = str(row[1])
        person_last_name = str(row[2])
        person_phone_number = str(row[3])
        single_record_json = {"id": person_id, "first name": person_first_name, "last name": person_last_name, "phone number": person_phone_number}
        json_list.append(single_record_json)
        response = json.dumps(json_list)
        row = cursor.fetchone()
    return func.HttpResponse(response)
