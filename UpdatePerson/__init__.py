import logging
import pyodbc
import azure.functions as func

server = '<insert_server_name>'
database = '<insert_DB_name>'
username = '<insert_username>'
password = '<insert_password>'
driver= '{ODBC Driver 17 for SQL Server}'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    person_id = req.route_params.get('id')
    
    if not person_id:
        return func.HttpResponse(
            "Please provide PersonId in the URI",
            status_code=400
        ) 
    
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
    cursor.execute("UPDATE PERSON SET FirstName = ?, LastName = ?, PhoneNumber = ? WHERE PersonId= ?", name, surname, phone_number, person_id)
    cursor.commit()
    
    return func.HttpResponse(
        "User updated",
        status_code=200
    )
