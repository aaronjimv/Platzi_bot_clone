import openai
import requests
import time
import creds


def get_updates(offset):
    '''
    Get updates from the Telegram chat.

    :param offset: The update identifier from which to retrieve updates.
    :return: A JSON dictionary containing chat updates.
    '''
    url = f"https://api.telegram.org/bot{creds.TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]


def send_messages(chat_id, text):
    '''
    Send a text message to the Telegram chat.

    :param chat_id: The chat ID to which to send the message.
    :param text: The text of the message to send.
    :return: The response from the HTTP message sending request.
    '''
    url = f"https://api.telegram.org/bot{creds.TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response


def get_openai_response(prompt):
    '''
    Get a response generated by the OpenAI language model.

    :param prompt: The input text to generate the response.
    :return: The response generated by the model.
    '''
    model_engine = creds.model_ft # use the name of your costume fine tunnig model.
    response = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 200,
        n = 1,
        stop = " END",
        temperature = 0.5
    )
    return response.choices[0].text.strip()


def main():
    '''
    The main function that starts the Telegram bot and responds to chat updates.
    '''
    print("Starting bot...")
    offset = 0
    while True:
        updates = get_updates(offset)
        if updates:
            for update in updates:
                offset = update["update_id"] +1
                chat_id = update["message"]["chat"]['id']
                user_message = update["message"]["text"]
                print(f"Received message: {user_message}")
                GPT = get_openai_response(user_message)
                send_messages(chat_id, GPT)
        else:
            time.sleep(1)
if __name__ == '__main__':
    main()
