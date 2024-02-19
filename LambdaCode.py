import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def lambda_handler(event, context):
    # Extract the token and event details from the input event
    try:
        token_info = json.loads(event['body'])['token']
        event_details = json.loads(event['body'])['event']
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing required parameter: {str(e)}')
        }

    # Reconstruct credentials
    creds = Credentials(token=token_info['token'],
                        refresh_token=token_info['refresh_token'],
                        token_uri=token_info['token_uri'],
                        client_id=token_info['client_id'],
                        client_secret=token_info['client_secret'],
                        scopes=token_info['scopes'])

    try:
        service = build('calendar', 'v3', credentials=creds)
        event = service.events().insert(calendarId='primary', body=event_details).execute()
        return {
            'statusCode': 200,
            'body': json.dumps('Event created: %s' % (event.get('htmlLink')))
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error creating event: %s' % str(e))
        }
