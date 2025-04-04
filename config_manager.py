# config_manager.py
import yaml

class Config:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as f:
            self.config = yaml.safe_load(f)

    def get(self, key_path, default=None):
        keys = key_path.split(".")
        val = self.config
        for key in keys:
            val = val.get(key, {})
        return val if val else default
