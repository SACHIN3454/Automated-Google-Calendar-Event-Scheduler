markdown
Copy code
# Automated Google Calendar Event Scheduler

A Python script that automates the creation of events in Google Calendar using the Google Calendar API. This tool allows users to set up reminders for tasks with specified start and end times, managing authentication and API requests efficiently.

## Features

- Automates the process of creating events in Google Calendar.
- Utilizes Google OAuth2 for secure authentication.
- Handles time normalization to ensure consistent scheduling.
- Allows customization of event details such as summary, location, description, and time.

## Prerequisites

- Python 3.x installed on your system.
- Google Calendar API credentials (OAuth 2.0).

## Installation

1. **Clone the repository**:
   ```bash
   gh repo clone SACHIN3454/Automated-Google-Calendar-Event-Scheduler
   cd Automated-Google-Calendar-Event-Scheduler
Install the required Python libraries:

bash
Copy code
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
Set up Google API credentials:

Go to the Google Cloud Console.
Create a new project.
Enable the Google Calendar API for the project.
Download the credentials.json file and place it in the root directory of the project.
Usage
Run the script:

bash
Copy code
python remainder.py
Authenticate with Google:

On the first run, the script will open a web browser for Google authentication.
Follow the on-screen instructions to grant access to your Google Calendar.
Set up your event:

The script creates a sample event titled "Sample Event" by default.
Customize the remainder() function call in remainder.py to change the event details like task name, start time, end time, and date.
Example
Here’s an example of how to modify the remainder() function to create a custom event:

python
Copy code
if __name__ == "__main__":
    date_str = dt.datetime.now().strftime("%Y-%m-%d")
    start_time_str = "9:00 AM"
    end_time_str = "10:00 AM"

    start_time = normalize_time_format(start_time_str, date_str)
    end_time = normalize_time_format(end_time_str, date_str)

    remainder("Team Meeting", start_time, end_time, date_str)
Code Overview
remainder.py: The main script that includes functions for authentication (get_service), time normalization (normalize_time_format), and creating events (remainder).
Notes
Make sure your system time matches the timezone set in the script (Asia/Kolkata) for accurate scheduling.
The script creates events on the primary Google Calendar associated with your account.
Troubleshooting
If you encounter an HttpError, check your internet connection and ensure the Google Calendar API is enabled in the Google Cloud Console.
If authentication fails, delete token.json and rerun the script to initiate the OAuth flow again.
To-Do
Add support for recurring events.
Enhance error handling for various Google API exceptions.
Include more customizable event features like attendees and reminders.
Author
Sachin S.

Visit my GitHub profile: SACHIN3454

For any issues or suggestions, feel free to contact me or create a new issue on the GitHub repository.
