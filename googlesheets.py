#Correr desde HOME

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import os
import httplib2
import argparse

try:
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'Downloads/secreto_cliente.json'
APPLICATION_NAME = 'Descargas'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_Data_temblor():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
#    spreadsheetId = 'Necesidades de Zonas Afectadas y Albergues '
    spreadsheetId = '19S (Responses)'
    #####DAÑOS Y DERRUMBES VERIFICADOS
    #####Para descargar otras páginas cambiar el onmbre en el campo range
    result = service.spreadsheets().values().get(
#        spreadsheetId='1tI4tyg7is4kmSiBOI5siEhM-NRSV-8gM4Ka3UzTTJic',
#        range='DAÑOS Y DERRUMBES VERIFICADOS!A1:H1500').execute()
        spreadsheetId='1CC5BqKv7Pqx5V2wtoJUNN7fOGOPtFyT5XOhSjfVhai8',
        range='Form Responses 1!A1:AJ150').execute()
    values = result.get('values', [])
    print(values)


if __name__ == '__main__':
    data=get_Data_temblor()
    print(data)
