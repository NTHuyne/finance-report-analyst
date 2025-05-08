from pydantic.dataclasses import dataclass

from configs.config_loader.read_yaml import YamlConfigReader

@dataclass
class ConfigReaderInstance:
    yaml = YamlConfigReader()