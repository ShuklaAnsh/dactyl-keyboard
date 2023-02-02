from dataclasses import dataclass
from typing import Literal


@dataclass
class ScrewConfig:
    ''' Screw Insert Configuration. '''

    screws_offset: Literal['INSIDE', 'OUTSIDE', 'ORIGINAL']
    ''' 
    Specify where the screws will go
        - `INSIDE`
        - `OUTSIDE`
        - `ORIGINAL`
    '''

    screw_insert_height: float
    ''' How high up the screw inserts will go '''

    screw_insert_bottom_radius: str
    '''
    5.21 / 2 designed for inserts
    2.50 / 2 designed for self tapping
    '''

    screw_insert_top_radius: str
    '''
    5.10 / 2 designed for inserts
    2.50 / 2 designed for self tapping
    '''

    screw_insert_outer_radius : str
    '''
    4.25 is common to keep interface to base
    '''
