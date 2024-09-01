import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime as dt
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_service():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)

def normalize_time_format(time_str, date_str):
    try:
        time_obj = dt.datetime.strptime(time_str, "%I:%M %p")
        full_datetime = dt.datetime.strptime(date_str, "%Y-%m-%d") + dt.timedelta(
            hours=time_obj.hour, minutes=time_obj.minute
        )
        return full_datetime.isoformat() + "+05:30"
    except ValueError:
        return time_str

def remainder(task, start_time, end_time, date_str):
    service = get_service()

    try:
        event = {
            "summary": task,
            "location": "Virtual",
            "description": "PROJ DEVELOPMENT",
            "colorId": 6,
            'start': {
                'dateTime': start_time,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_time if end_time else start_time,
                'timeZone': 'Asia/Kolkata',
            },
        }

        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event Created: {event.get('htmlLink')}")

    except HttpError as error:
        print("An Error occurred:", error)

if __name__ == "__main__":
    date_str = dt.datetime.now().strftime("%Y-%m-%d")
    start_time_str = "7:00 PM"
    end_time_str = "8:00 PM"

    start_time = normalize_time_format(start_time_str, date_str)
    end_time = normalize_time_format(end_time_str, date_str)

    remainder("Sample Event", start_time, end_time, date_str)
