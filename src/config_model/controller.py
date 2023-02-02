from dataclasses import dataclass
from typing import Literal


@dataclass
class ControllerConfig:
    ''' Controller Mount + Connection Configuration. '''

    controller_mount_type: Literal['RJ9_USB_WALL', 'USB_WALL', 'RJ9_USB_TEENSY', 'USB_TEENSY', 'EXTERNAL', 'NONE']
    ''' 
    connector options are
        - `RJ9_USB_WALL` Standard internal plate with RJ9 opening and square cutout for connection.
        - `USB_WALL` Standard internal plate with a square cutout for connection, no RJ9.
        - `RJ9_USB_TEENSY` Teensy holder
        - `USB_TEENSY` Teensy holder, no RJ9
        - `EXTERNAL` Square cutout for a holder such as the one from lolligagger.
        - `NONE`
    '''

    external_holder_height: float
    '''
    Set if mount type is external.
    '''

    external_holder_width: float
    '''
    Set if mount type is external.
    '''

    external_holder_xoffset: float
    ''' 
    Set if mount type is external.
    Offset is from the top inner corner of the top inner key.
    '''

    external_holder_yoffset : float
    '''
    Set if mount type is external.
    Offset is from the top inner corner of the top inner key.
    Tweak this value to get the right undercut for the tray engagement.
    '''
