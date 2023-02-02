from dataclasses import dataclass


@dataclass
class OLEDConfig:
    ''' OLED Mount Configuration '''

    oled_center_row: float
    ''' if not None, this will override the `oled_mount_location_xyz` and `oled_mount_rotation_xyz` settings '''

    oled_translation_offset: tuple[float]

    oled_rotation_offset: tuple[float]

    oled_screen_length: float
    ''' OLED screen length '''

    oled_screen_width: float
    ''' OLED screen width '''

    oled_height: float
    ''' Whole OLED module height '''

    oled_width: float
    ''' Whole OLED module width '''

    oled_thickness: float
    ''' Thickness of OLED, plus clearance.  Must include components '''

    oled_depth: float

    oled_mount_rim: float

    oled_mount_height: float
    ''' Height of mount, not including clip height '''

    oled_mount_cut_depth: float
    ''' Depth to cut from main body '''

    oled_mount_location_xyz: tuple[float]
    ''' will be overwritten if oled_center_row is not None '''
    
    oled_mount_rotation_xyz: tuple[float]
    ''' will be overwritten if oled_center_row is not None '''

    oled_clip_bezel_thickness: float
    ''' thickness of clip bezel '''

    oled_clip_bezel_chamfer: float
    ''' depth of the 45 degree chamfer towards the screen '''

    oled_clip_thickness: float

    oled_clip_width: float
    
    oled_clip_overhang: float
    
    oled_clip_extension: float
    
    oled_clip_width_clearance: float
    
    oled_clip_undercut: float
    
    oled_clip_undercut_thickness: float
    
    oled_clip_y_gap: float
    
    oled_clip_z_gap: float

    oled_mount_connector_hole: float

    oled_screen_start_from_conn_end: float

    oled_left_wall_x_offset_override: float
    ''' Offset for how far the wall next to the mount is from the baseline '''

    oled_left_wall_z_offset_override: float
    ''' Offset for how high the wall next to the mount  mount is '''

    oled_left_wall_lower_y_offset: float

    oled_left_wall_lower_z_offset: float


