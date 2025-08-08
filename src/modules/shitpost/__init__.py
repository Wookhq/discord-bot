import os
import random

shitpost_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "shitpost")
)

def get_random_shitpost():
    files = [
        f for f in os.listdir(shitpost_dir)
        if f.lower().endswith((".gif", ".png", ".jpg", ".jpeg", ".mp4"))
    ]
    if not files:
        raise FileNotFoundError(f"no shitposts found in {shitpost_dir}")

    return os.path.join(shitpost_dir, random.choice(files))
