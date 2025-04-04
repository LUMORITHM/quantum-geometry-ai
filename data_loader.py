# data_loader.py
import json
from utils.logger import logger
from config_manager import Config

cfg = Config()
DATA_PATH = cfg.get("data.polytope_path", "data/sample_polytopes.json")

def load_polytopes_lazy(path=DATA_PATH):
    """Lazily loads polytopes from a JSONL file (1 polytope per line)."""
    try:
        with open(path, "r") as f:
            for line in f:
                yield json.loads(line)
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        raise

