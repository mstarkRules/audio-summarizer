# Audio summarizer

## About project

The app is a python project that will can read an ogg (whatsapp audio type) audio file and to convert to text

The main goal is to use chat gpt to resume audio files from WhatsApp hehehe

## How to use

_Runing Manually_
For now, you can run in your local machine if, in adittion to having python, you have all packages that the project need

All these packages can be found on requirements.txt

Rename your audio file to audio.ogg

Copy the ogg audio file to src/assets/audio.ogg

From root folder, run src/main.py file to run python script

```sh
python3 src/main.py
```

_Docker and Docker Compose_
To avoid install all packages manually, you can use docker and docker compose to install all packages.

Rename your audio file to audio.ogg

Copy the ogg audio file to src/assets/audio.ogg

From root folder, run

```sh
docker-compose up --build
```

## Next steps

- At the moment, project only can read an audio file and to convert to text
- Next step is to create an Api to receive an audio and to proccess it
- So we can take the returned text and send to chat gpt
- Chat gpt will summarize for us (oh god)
- We can return the answer to client
- In addition of that, we also can create a whatsapp bot to receive audio file and return it in same chat

> Important Note: the original audio in assets is from my Grandma 😍
