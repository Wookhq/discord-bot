import json
import os
from dotenv import load_dotenv
from github import Github
from github import Auth

load_dotenv()
auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

g = Github(auth=auth)
repo = g.get_repo("Wookhq/Lution-Marketplace")

class LutionMarketplace:
    def __init__(self):
        self.themedata = repo.get_contents("Assets/Themes/content.json")
        self.moddata = repo.get_contents("Assets/Mods/content.json")
        self.themeinfo = repo.get_contents("Assets/Themes/info.json")
        

    def get_themes(self):
        content = self.themedata
        data = json.loads(content.decoded_content.decode())
        themes = [theme["title"] for theme in data if "title" in theme]
        return themes

    def get_mods(self):
        content = self.moddata
        data = json.loads(content.decoded_content.decode())
        mods = [mod["title"] for mod in data if "title" in mod]
        return mods

    def get_theme_description(self, title):
        content = self.themedata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == title:
                return item.get("body", None)
            
    def get_mod_description(self, mod):
        content = self.moddata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == mod:
                return item.get("body", None)

    def get_theme_sb(self, title):
        content = self.themedata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == title:
                return item.get("sb", None)

    def get_mod_sb(self, mod):
        content = self.moddata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == mod:
                return item.get("sb", None)
            
    def get_theme_image(self, title):
        content = self.themedata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == title:
                return item.get("image", None)
    
    def get_mod_image(self, mod):
        content = self.moddata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == mod:
                return item.get("image", None)
            
    def get_theme_author(self, title):
        content = self.themedata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == title:
                return item.get("author", None)
            
    def get_mod_author(self, mod):
        content = self.moddata
        data = json.loads(content.decoded_content.decode())
        for item in data:
            if item.get("title") == mod:
                return item.get("author", None)
    
    def get_theme_download(self, theme):
        content = self.themedata
        info_list = json.loads(content.decoded_content.decode())
        entry = next((item for item in info_list if isinstance(item, dict) and item.get("name") == theme), None)
        path = entry["path"]
        if entry:
            return f"https://api.github.com/repos/Wookhq/Lution-marketplace/contents/{path}"
        else:
            return None
    
    def get_mod_download(self, mod):
        content = self.themedata
        info_list = json.loads(content.decoded_content.decode())
        entry = next((item for item in info_list if isinstance(item, dict) and item.get("name") == mod), None)
        path = entry["path"]
        if entry: 
            return f"https://api.github.com/repos/Wookhq/Lution-marketplace/contents/{path}" 
        else:
            return None