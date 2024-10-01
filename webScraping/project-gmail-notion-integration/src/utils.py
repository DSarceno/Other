import os 
import base64
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


class gmailAPI_authenticate:
    def __init__(self) -> None:
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    def get_authentication(self):
        creds = None

        # verificar si hay credenciales guardadas
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        
        # si no hay credenciales validas, autenticarse con OAuth
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # fluir de OAuth para pedir autorizacion
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        # devolver el servicio de gmail
        return build('gmail', 'v1', credentials=creds)