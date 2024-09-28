import requests
import json
import time
import sys
import os
import http.server
import socketserver
import threading
from platform import system

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"ITZ HACKER FOLLOW ME ON FACEBOOK (www.facebook.com/prembabu001)")

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def load_group_info():
    try:
        with open('group_info.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"[!] Error loading group info: {e}")
        sys.exit()

def get_current_group_name():
    # Yeh function current group name ko fetch karne ka logic rakhega
    # Yahan aapko Facebook API ya kisi aur method se group name get karna hoga
    return "सचिन बेटा तेरी मां की चूदाई होती रहेगी भागना मत 🙂🤞"  # Replace with actual logic to get current group name

def validate_and_set_group_name():
    # Load group info from JSON
    group_info = load_group_info()
    original_group_name = group_info['group_name']

    # Get the current group name
    current_group_name = get_current_group_name()

    # Check if the current group name matches the original
    if current_group_name != original_group_name:
        print("[-] Group name has been changed! Resetting to original...")
        group_info['group_name'] = original_group_name  # Reset to original name
        with open('group_info.json', 'w') as file:
            json.dump(group_info, file)
        print(f"[+] Group name reset to: {original_group_name}")
    else:
        print("[+] Group name is valid.")

def send_messages():
    # Load group info to validate
    group_info = load_group_info()
    group_name = group_info['group_name']

    with open('password.txt', 'r') as file:
        password = file.read().strip()

    # If you want to implement password verification
    entered_password = password
    if entered_password != password:
        print('[-] <==> Incorrect Password!')
        sys.exit()

    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')

    cls()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    access_tokens = [token.strip() for token in tokens]

    # Read all conversation IDs (UIDs)
    with open('convo.txt', 'r') as file:
        convo_ids = [line.strip() for line in file.readlines()]

    with open('file.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    while True:
        try:
            # Validate and set group name
            validate_and_set_group_name()

            # Iterate through the messages and UIDs
            for message_index in range(num_messages):
                # Get the current UID based on the message index
                convo_index = message_index % len(convo_ids)
                convo_id = convo_ids[convo_index]

                token_index = message_index % num_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                url = f"https://graph.facebook.com/v15.0/t_{convo_id}/"
                parameters = {
                    'access_token': access_token,
                    'message': f"{haters_name} {message}"
                }
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"[+] Message {message_index + 1} of Convo {convo_id} sent by Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}")
                else:
                    print(f"[x] Failed to send message {message_index + 1} of Convo {convo_id} with Token {token_index + 1}: {haters_name} {message}")
                    print(f"  - Time: {current_time}")

                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print(f"[!] An error occurred: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    send_messages()

if __name__ == '__main__':
    main()
