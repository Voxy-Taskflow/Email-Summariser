import os
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import config
from datetime import date
import email.utils
from zoneinfo import ZoneInfo

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


def extract_full_body(messages):
    payload = messages.get('payload', {})
    body = payload.get('body', {}).get('data')
    
    if body:
        return base64.urlsafe_b64decode(body.encode('ASCII')).decode('utf-8', errors='ignore')
    
    parts = payload.get('parts', [])
    while parts:
        next_parts = []
        for part in parts:
            mime_type = part.get('mimeType')
            part_body = part.get('body', {}).get('data')
    
            if mime_type == 'text/plain' and part_body:
                return base64.urlsafe_b64decode(part_body.encode('ASCII')).decode('utf-8', errors='ignore')
    
            if 'parts' in part:
                next_parts.extend(part['parts'])
    
            parts = next_parts
    return "No plain content found"

def get_latest_emails(service = get_mail_service, max_results=config.max_requests):
    results = service.users().messages().list(userId='me', maxResults=max_results, q="label:INBOX").execute()
    messages = results.get('messages', [])
    if not messages:
        print("No Emails Found")
        return

    for msg in messages:
        msg_details = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
        headers = msg_details.get('payload', {}).get('headers', [])

        #Get Subject
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '(No Subject)')
        #Get Sender
        from_user = next((h['value'] for h in headers if h['name'].lower() == 'from'), '(Unknown Sender)')
        #Get Date
        sent_date = next((h['value'] for h in headers if h['name'].lower() == 'date'), '(Unknown Date)')
        #Formating the date
        formatted_date = email.utils.parsedate_to_datetime(sent_date).date()
        
        if formatted_date == date.today():
            for message in messages:
                msg = (
                    service.users().messages().get(userId="me", id=message["id"]).execute()
                )
                print(extract_full_body(msg))
        else:
            print("No mails today")
        
    
        

