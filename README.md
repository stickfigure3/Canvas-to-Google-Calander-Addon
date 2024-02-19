Akash and Adam (+ Keshav) created this wonderful application




Lambda requirements for Google Token and Event: 
{
  "token": {
    "token": "ya29.a0ARrdaM...",
    "refresh_token": "1//04i...",
    "token_uri": "https://oauth2.googleapis.com/token",
    "client_id": "your-client-id.apps.googleusercontent.com",
    "client_secret": "your-client-secret",
    "scopes": ["https://www.googleapis.com/auth/calendar"]
  },
  "event": {
    "summary": "Google I/O 2025",
    "location": "800 Howard St., San Francisco, CA 94103",
    "description": "A chance to hear more about Google's developer products.",
    "start": {
      "dateTime": "2025-05-28T09:00:00-07:00",
      "timeZone": "America/Los_Angeles",
    },
    "end": {
      "dateTime": "2025-05-28T17:00:00-07:00",
      "timeZone": "America/Los_Angeles",
    },
    "reminders": {
      "useDefault": false,
      "overrides": [
        {"method": "email", "minutes": 24 * 60},
        {"method": "popup", "minutes": 10},
      ],
    },
  }
}
