# SpongebobCLIBot

## Setup

### Account and API key
1. Visit https://ai.sooners.usLinks to an external site.

2. Click Sign up and register with your email.

3. After logging in, open Settings → Account → API Keys.

4. Create a new API key and copy it.

#### Create Local .env file
Create /.soonerai.env with:

SOONERAI_API_KEY=your_key_here
SOONERAI_BASE_URL=https://ai.sooners.us
SOONERAI_MODEL=gemma3:4b

### Python and python package installation
Install Python 3.12.1
Check Python version:
- python3 -v

Run the following commands via your terminal:
- pip install -r requirements.txt

## Run the Spongebob ChatBot
python3 spongebob_cli.py
End the conversation with "Bye"