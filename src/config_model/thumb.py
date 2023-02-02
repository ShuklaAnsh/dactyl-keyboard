from dataclasses import dataclass
from typing import Literal


@dataclass
class ThumbConfig:
    '''
    Configuration for thumb cluster
    '''

    thumb_style: Literal['DEFAULT', 'MINI', 'CARBONFET', 'MINIDOX', 'TRACKBALL_ORBYL']
    '''
    Available thumb styles:
        - `DEFAULT`: 6-key
        - `MINI`: 5-key 
        - `CARBONFET`: 6-key
        - `MINIDOX`: 3-key
        - `TRACKBALL_ORBYL`
        - `TRACKBALL_CJ`
    '''
    
    default_1U_cluster: bool
    '''
    only used with default, makes top right thumb cluster key 1U
    '''
    
    minidox_Usize: str
    '''
    config name, prefixed in export files' names
    '''

    mini_index_key: bool