# Fastapi Start!

Reference at [Building a Website Starter with FastAPI](https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864).

## Overview


- app
- test
- README.md
- requirements.txt
- static
- templates

## Requirement

See requirements.txt for updates.

```sh
- requests==2.26.0
- fastapi==0.70.0
- uvicorn==0.15.0
- python-dotenv==0.19.1
- aiofiles==0.7.0
- python-multipart==0.0.5
- jinja2==3.0.2
- Markdown==3.3.4
- pytest==6.2.5
- Pillow==8.4.0
```

## Installation & Usage

```bash
# change the directory
$ cd fastapi-web-starter
# install packages
$ pip install -r requirements.txt
# start the server
$ uvicorn app.main:app --reload
```
## Test

All tests are under `tests` directory.

```bash
# Change the directory
$ cd fastapi-web-starter
# Run tests
$ pytest -v
```
