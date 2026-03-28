# Email Triage OpenEnv

AI environment for handling customer emails.

## Features
- Spam detection
- Priority classification
- Response decision

## Run
python server.py

## Docker
docker build -t email-env .
docker run -p 7860:7860 email-env