import os
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import config

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_mail_service():
    creds = None
    service = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_tokens:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port = 0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def get_latest_emails(service = get_mail_service, max_results=config.max_requests):
    print(f"\n---- Fetching the last {max_results} emails ----")

    results = service.users().messages().list(userId='me', maxResults=max_results, q="label:INBOX").execute()
    messages = results.get('messages', [])
    if not messages:
        print("No Emails Found")
        return

    for msg in messages:
        msg_details = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
        headers = msg_details.get('payload', {}).get('headers', [])


        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '(No Subject)')

        from_user = next((h['value'] for h in headers if h['name'].lower() == 'from'), '(Unknown Sender)')

        print(f"From: {from_user} | Subject: {subject}")