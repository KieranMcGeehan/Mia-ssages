#!/bin/env python3

from dataclasses import dataclass
import os
from pathlib import Path
import random
import sys
from urllib.parse import urljoin
import requests

def main():
    env_vars = get_environment_variables()
    webhook_url = env_vars["MIA_WEBHOOK"]
    image_url = env_vars["IMAGE_URL"]
    dry_run = "DRY_RUN" in env_vars
    mia = Mia(webhook=webhook_url, image_url_root=image_url, dry_run=dry_run)
    mode = sys.argv[1]

    match mode:
        case "eyes-tablet-antibiotics":
            mia.send_message("Nyaaa~ eyes pwease. I awso need some antibiwotics n supplimewnts")
        case "eyes-tablet":
            mia.send_message("Nyaaa~ eyes pwease. I awso need some antibiwotics 🥺")
        case "eyes":
            mia.send_message("Nyaaa~ eyes pwease!")
        case "food":
            mia.send_message("Parents. Please feed me")
        case _:
            raise Exception(f"Invalid mode '{mode}'")

@dataclass
class Mia:
    webhook: str
    image_url_root: str
    dry_run: bool

    def send_message(self, content: str):
        avatar = None
        if random.random() < 0.001:
            avatar = urljoin(self.image_url_root+"/", "mia_buttocks.png")
        
        print(f"Sending '{content}'")
        if not self.dry_run:
            send_webhook(self.webhook, content, avatar_url=avatar)

def send_webhook(webhook_url: str, content: str, username: str | None = None, avatar_url: str | None = None):
    json_post_data = {
        "content": content,
        "username": username,
        "avatar_url": avatar_url
    }
    # Remove unspecified fields
    json_post_data = {k:v for k,v in json_post_data.items() if v}
    # Send a http request to discord
    result = requests.post(
        webhook_url,
        json=json_post_data
    )
    # Raise an exception if discord returned an error
    result.raise_for_status()

def get_environment_variables() -> dict[str, str]:
    environ: dict[str, str] = {}
    # Load environment variables from file
    environ_file = Path("./.env")
    if environ_file.exists():
        with open(environ_file, "r") as f:
            line_number = 1
            for line in f:
                if len(line.strip()) == 0 or line.startswith("#"):
                    continue
                if not "=" in line:
                    raise Exception(f"Error on line {line_number} of {environ_file}. Lines should be formatted as key=val")
                [key,val] = line.split("=", 1)
                environ[key] = val
    # Load actual environment variables, overriding any in the file
    for key,val in os.environ.items():
        environ[key] = val
    return environ

if __name__ == "__main__":
    main()