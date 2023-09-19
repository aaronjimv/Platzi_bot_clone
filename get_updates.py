import requests
import time
import creds

def get_updates(token, offset=None):
    '''
    Get updates from the Telegram chat.

    :param token: The Telegram token to authenticate API requests.
    :param offset: The update identifier from which to retrieve updates.
    :return: A JSON dictionary containing chat updates.
    '''
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    params = {'offset': offset} if offset else {}
    response = requests.get(url, params=params)
    return response.json()

def print_new_messages(token):
    '''
    Print new messages from the Telegram chat to the console.

    :param token: The Telegram token to authenticate API requests.
    '''
    offset = None
    while True:
        updates = get_updates(token, offset)
        if "result" in updates:
            for update in updates["result"]:
                message = update["message"]
                id = message["from"]["id"]
                username = message["from"]["first_name"]
                text = message.get("text")
                print(f"Usuario: {username} ({id})")
                print(f"Mensaje: {text}")
                print("---")
                offset = update["update_id"] + 1
        time.sleep(1)  # wait 1s

print_new_messages(creds.TOKEN)
