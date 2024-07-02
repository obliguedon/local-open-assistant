import requests
import json

url = 'http://localhost:8000/v1/completions'

payload = {
  "prompt": "",
  "stop": [],
  "max_tokens": 600 # the max lenght of the output
}

class TextColor:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

in_text = str()

print("enter \"exit\" to close.")
print("Give me a prompt specifying my role and what to do.")

while in_text != "exit":
    in_text = input(f"{TextColor.BLUE}PROMPT : {TextColor.RESET}\n ")

    if (in_text != "exit"):
        payload["prompt"] = f"[INST] {in_text} [/INST]"
        response = requests.post(url, json=payload)
        # TODO: check if response is OK (code 200)
        json_data = json.loads(response.content)
        # print(json_data["choices"])
        print(f"{TextColor.GREEN}ANSWER : {TextColor.RESET}\n{json_data['choices'][0]['text']}")
    else:
        print(f"{TextColor.GREEN}ANSWER : {TextColor.RESET}\n See you next time !")
