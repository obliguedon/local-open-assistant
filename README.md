# Get your local AI

simple example to help you getting started building your own local ChatBot.

## Get the LLM

the LLM repo on Hugging Face :
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/tree/main

```
mkdir /home/models
cd /home/models
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

if you want to use a different model, remmember **"the bigger, the better"**.

## The API

than to run llama type this command in this folder :

```
docker compose up -d
```
> also work with Podman

to stop it:
```
docker compose stop
```
> in the same folder as the compose file

## the script

run the python script by typing:
```
python3 ./post_completion.py
```

or just run the script [start_chat.sh](./start_chat.sh)

## Additionnal infos

- View the API docimentation at http://localhost:8000/docs

- prompt template for Mistral AI 7B:
```
<s>[INST] Instruction [/INST] Model answer</s>[INST] Follow-up instruction [/INST]
```
> see the full article on [PromptingGuide.ai](https://www.promptingguide.ai/models/mistral-7b)

- Look at [this repo](https://github.com/f/awesome-chatgpt-prompts/blob/main/prompts.csv) for example prompts for Chat GPT

- **big thanks to Ana Arieias for this easy tutorial [HERE](https://medium.com/@ana_areias/quickly-serve-mistral-7b-on-cpu-using-docker-5fce00c27ffc#:~:text=Quickly%20serve%20Mistral-7B%20on%20CPU%20using%20Docker%201,3.%20Access%20the%20API%20by%20navigating%20to%20localhost%3A8000%2Fdocs.)**
