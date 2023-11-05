import os.path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage


CREDENTIALS_FILE_NAME = 'credentials.json'
SCOPES = ('https://www.googleapis.com/auth/gmail.send',)
TOKEN_FILE_NAME = 'token.json'



def get_credentials():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE_NAME, SCOPES) if os.path.exists(TOKEN_FILE_NAME) else None
                
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE_NAME, SCOPES)
        creds = flow.run_local_server(port=0)
    elif creds.expired and creds.refresh_token:
        creds.refresh(Request())
    with open(TOKEN_FILE_NAME, 'w') as token:
        token.write(creds.to_json())
           
    return creds


def send_email(creds, email_content, email_recipient, subject):
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()
        message.set_content(email_content)
        message['To'] = email_recipient
        message['Subject'] = subject
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')
        send_message = None
    return send_message


def main():
    creds = get_credentials()
    message_id = send_email(creds)
    print(message_id)


if __name__ == '__main__':
    main()