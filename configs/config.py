from typing import List, Dict, Any
from pydantic_settings import BaseSettings
from configs.config_loader import ConfigReaderInstance

class Config(BaseSettings):
    """Returns a config instance depending on the ENV_STATE variable."""
    CONF: Dict[str, Any] = ConfigReaderInstance.yaml.read_config_from_file(f"settings/config.yml")

settings = Config()