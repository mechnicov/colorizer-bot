## Colorizer Telegram bot

### Description

If you need to colorize black and white photos, just send this photo as document or as usual photo to the bot. And he will reply with colorized photo

Realized in Python. Language: Russian.

### Launching

1. Download or clone repo.

2. Use your own credentials as in example

```
$ cp .env.example .env
```

2. Create docker image

```console
$ docker build -t colorizer .
```

3. Run docker container

```console
$ docker run --name colorizer -d colorizer
```

### License

MIT – see `LICENSE`

### Contacts

Email me at

```py
''.join(list(map(lambda ch: chr(ord(ch) + 1), list('dcdl-snotynu?fl`hk-bnl'))))
```
