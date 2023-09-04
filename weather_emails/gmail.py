import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage

EMAIL_CONTENT = 'Today in Warsaw is ... C degrees.'
EMAIL_RECIPIENT = 'jkstycz91@gmail.com'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
SUBJECT = 'Tempreture today'
TOKEN_FILE_NAME = 'token.json'
CREDENTIALS_FILE_NAME = 'credentials.json'


def get_credentials():
    creds = None
    
    if os.path.exists(TOKEN_FILE_NAME):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE_NAME, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE_NAME, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE_NAME, 'w') as token:
            token.write(creds.to_json())

    return creds

def send_email(creds):
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()
        message.set_content(EMAIL_CONTENT)
        message['To'] = EMAIL_RECIPIENT
        message['Subject'] = SUBJECT
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


def main():
    creds = get_credentials()
    message_id = send_email(creds)
    print(message_id)


if __name__ == '__main__':
    main()