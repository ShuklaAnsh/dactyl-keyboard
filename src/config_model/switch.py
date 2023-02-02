from dataclasses import dataclass
from typing import Literal


@dataclass
class SwitchConfig:
    '''
    Switch Hole Configuration.
    '''

    plate_style: Literal['HOLE', 'NUB', 'UNDERCUT', 'NOTCH', 'HS_NUB', 'HS_UNDERCUT', 'HS_NOTCH']
    '''
    Available thumb styles:
        - `HOLE`: Square hole. Useful for applying custom plate files.
        - `NUB`: Original side nubs
        - `UNDERCUT`: Snap fit undercut.  May require `clip_thickness` and possibly `clip_undercut` tweaking and/or filing to get proper snap.
        - `NOTCH`: snap fit undercut only near switch clip.  May require `clip_thickness` and possibly `clip_undercut` tweaking and/or filing to get proper snap.
        - `HS_NUB`: hot swap underside with nubs.
        - `HS_UNDERCUT`: hot swap underside with undercut. Does not generate properly.  Hot swap step needs to be modified.
        - `HS_NOTCH`: hot swap underside with notch.  Does not generate properly.  Hot swap step needs to be modified.
    '''

    switch_size: float
    '''
    height/width of keyswitch. Defaults:
        - 14 for hole
        - 14.4 for nub
        - 14 for undercut
    '''

    notch_width: float
    ''' If using notch, it is identical to undecut, but only locally by the switch clip '''

    sa_profile_key_height: float
    sa_length: float
    sa_double_length: float
    plate_thickness: float
    plate_rim: float

    clip_thickness: float
    ''' Notch/Undercut dimenstions'''

    clip_undercut: float
    ''' Notch/Undercut dimenstions'''

    undercut_transition: float
    ''' 
    Undercut dimenstions
    NOT FUNCTIONAL WITH OPENSCAD, ONLY WORKS WITH CADQUERY
    '''

    plate_file: str
    ''' Custom plate stl filepath '''

    plate_offset: float
    ''' Offset for custom plate '''