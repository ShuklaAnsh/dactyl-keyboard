from dataclasses import dataclass
from typing import Literal


@dataclass
class ShapeConfig:
    '''
    Configuration for the keyboard to define its shape
    '''

    show_caps: Literal['MX']
    '''
    If keycap preview should be generated. 
    These are useful for visualizing cap placements.
    '''
    
    show_pcbs: bool
    ''' 
    If PCB preview should be generated. 
    Only shows if set to `True` and if `show_caps` is set 
    '''
    
    nrows: int
    ''' number of key rows '''

    ncols: int
    ''' number of key columns '''
    
    row_curve: float
    ''' Curvature of the rows '''

    col_curve: float
    ''' Curvature of the cols '''

    tenting: int
    ''' controls left -> right tilt by center column offset. ''' 

    tenting_angle: float
    ''' More precise tenting control '''

    tilt: int
    ''' controls front -> back tilt by center row offset '''

    symmetry: Literal['symmetric', 'asymmetric']
    ''' symetric or asymetric build. Asymetric doubles generation time '''

    column_style: Literal['orthographic', 'standard', 'fixed']
    '''
    Orthographic and Standard styles only availble if `nrows` >= 5
    '''

    column_offsets: tuple[float]

    fixed_angles: tuple[float]
    ''' Used when `column_style=fixed`'''
    
    fixed_x: tuple[float]
    ''' Used when `column_style=fixed`. Relative to middle finger'''

    fixed_z: tuple[float]
    ''' Used when `column_style=fixed`. Relative to middle finger'''
    
    fixed_tenting: float

    col_offset: tuple[float]
    ''' 
    (X,Y,Z) tuple defining col offsets 
    Original=[0, -5.8, 5.64]
    '''

    thumb_offset: tuple[float]
    ''' (X,Y,Z) tuple defining thumb offsets '''

    keyboard_z_offset: int
    ''' 
    controls overall height
    original=9 with centercol=3
    use 16 for centercol=2
    '''

    extra_width: float
    ''' extra space between the base of keys. Original=2 '''

    extra_height: float
    ''' Original=0.5 '''

    skeletal_walls: bool
    ''' Experimental. Make walls skeletal '''

    wall_z_offset: int
    ''' length of the first downward_sloping part of the wall '''

    wall_x_offset: int
    ''' offset in the x and/or y direction for the first downward_sloping part of the wall (negative) '''

    wall_y_offset: int
    ''' offset in the x and/or y direction for the first downward_sloping part of the wall (negative) '''

    left_wall_x_offset: int
    ''' specific values for the left side due to the minimal wall. '''
    
    left_wall_z_offset: int
    ''' specific values for the left side due to the minimal wall. '''
    
    left_wall_lower_x_offset: int
    ''' specific values for the lower left corner. '''
    
    left_wall_lower_y_offset: int
    ''' specific values for the lower left corner. '''
    
    left_wall_lower_z_offset: int
    ''' specific values for the lower left corner. '''
    
    wall_thickness: float
    ''' wall thickness parameter used on upper/mid stage of the wall '''
    
    wall_base_y_thickness: float
    ''' wall thickness at the lower stage '''
    
    wall_base_x_thickness: float
    ''' wall thickness at the lower stage '''
    
    wall_base_back_thickness: float
    ''' wall thickness at the lower stage in the specifically in back for interface. '''


