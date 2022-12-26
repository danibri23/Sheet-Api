"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint

from googleapiclient import discovery

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'
credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to update.
spreadsheet_id = '1zsCw3bD6eg77UyJUR5A1c__y81_gnkcHIP73kadxteY'
# TODO: Update placeholder value.
def borrar_datos(gastos, egresos):
    # The A1 notation of the values to clear.
    range_ = 'B2:C2'  # TODO: Update placeholder value.

    clear_values_request_body = {
        (gastos, egresos),
    }

    request = service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range=range_, body=clear_values_request_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    pprint(response)

borrar_datos(300, 250)