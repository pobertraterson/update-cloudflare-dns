import CloudFlare
import os
import sys
from dotenv import load_dotenv

def defineOS():
    platform = sys.platform
    if platform == "win32":
        return "windows"
    elif platform == "linux" or sys.platform == "linux2":
        return "linux"
def networkCommands():
    windows_commands=["PowerShell Invoke-RestMethod ipinfo.io/ip"]
    linux_commands=["dig +short myip.opendns.com @resolver1.opendns.com"]

load_dotenv()

# You can replace this with your actual CloudFlare API key,
# I just use dotenv to be a bit more safe.
cloudFlareSuperSecretApiKey = os.getenv('cloudFlareSuperSecretApiKey')


