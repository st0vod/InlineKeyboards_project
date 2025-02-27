import logging
from configs.config import load_config, Config


logger = logging.getLogger()
config: Config = load_config()
