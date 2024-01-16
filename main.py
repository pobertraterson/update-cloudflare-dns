import CloudFlare
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# You can replace this with your actual CloudFlare API key,
# I just use dotenv to be a bit more safe.
cloudFlareSuperSecretApiKey = os.getenv('cloudFlareSuperSecretApiKey')

