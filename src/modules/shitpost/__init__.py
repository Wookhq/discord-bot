import os
import random

shitpost_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "shitpost")
)

def get_random_shitpost():
    files = [
        f for f in os.listdir(shitpost_dir)
        if f.lower().endswith((".gif", ".png", ".jpg", ".jpeg", ".mp4", ".mov"))
    ]
    if not files:
        raise FileNotFoundError(f"no shitposts found in {shitpost_dir}")

    return os.path.join(shitpost_dir, random.choice(files))
class ShitpostIterator:
    def __init__(self):
        self.files = self._get_shitpost_files()
        self.index = 0
        self.shuffle_count = 0
        random.shuffle(self.files)

    def _get_shitpost_files(self):
        files = [
            f for f in os.listdir(shitpost_dir)
            if f.lower().endswith((".gif", ".png", ".jpg", ".jpeg", ".mp4", ".mov"))
        ]
        if not files:
            raise FileNotFoundError(f"no shitposts found in {shitpost_dir}")
        return files

    def get_next_shitpost(self):
        if not self.files:
            self.files = self._get_shitpost_files()
            random.shuffle(self.files)
            self.index = 0
            self.shuffle_count = 0

        if self.index >= len(self.files) or self.shuffle_count >= 10:
            random.shuffle(self.files)
            self.index = 0
            self.shuffle_count = 0

        shitpost_path = os.path.join(shitpost_dir, self.files[self.index])
        self.index += 1
        self.shuffle_count += 1
        return shitpost_path

shitpost_iterator = ShitpostIterator()

def get_next_shitpost():
    return shitpost_iterator.get_next_shitpost()
