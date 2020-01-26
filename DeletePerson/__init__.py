import logging
import pyodbc
import azure.functions as func

server = 'fmmb-sql.database.windows.net'
database = 'People'
username = 'fmmb'
password = 'Aa1Bb2Cc3'
driver= '{ODBC Driver 17 for SQL Server}'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    person_id = req.route_params.get('id')
    if not person_id:
        return func.HttpResponse(
            "Please provide PersonId in the URI",
            status_code=400
        )

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM PERSON WHERE PersonId= ?", person_id)
    cursor.commit()
    
    return func.HttpResponse(
        "User deleted",
        status_code=200
    )
