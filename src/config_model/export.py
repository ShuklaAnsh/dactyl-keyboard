from dataclasses import dataclass


@dataclass
class ExportConfig:
    ''' Export Configuration. '''

    save_dir: str
    ''' directory to save exports '''

    parts_dir: str
    ''' directory for pre-created parts (such as hotswap plates) '''

    config_name: str
    ''' config name, prefixed in export files' names '''
