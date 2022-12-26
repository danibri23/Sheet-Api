# probando@dani-datos.iam.gserviceaccount.com

from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'llave.json'
credentials = service_account.Credentials.from_service_account_file(
    filename=SERVICE_ACCOUNT_FILE
)

service_sheets = build('sheets', 'v4', credentials=credentials)
GOOGLE_SHEETS_ID = '1zsCw3bD6eg77UyJUR5A1c__y81_gnkcHIP73kadxteY'
worksheet_name = 'tabla!'


cont = 2

def subir_a_sheets(gastos, egresos):
    global cont
    
    cell_range_insert = ('B' + str(cont) + ':' + 'C' + str(cont))

    cont = cont + 1
    
    values = (
        (gastos, egresos),
    )
    value_range_body = { 
        'majorDimension': 'ROWS',
        'values': values
    }

    service_sheets.spreadsheets().values().update(
        spreadsheetId=GOOGLE_SHEETS_ID,
        valueInputOption='USER_ENTERED',
        range=worksheet_name + cell_range_insert,
        body=value_range_body
    ).execute()

subir_a_sheets(300, 250)

