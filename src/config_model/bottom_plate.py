from dataclasses import dataclass


@dataclass
class BottomPlateConfig:
    ''' Bottom plate + PCB Configuration '''

    screw_hole_diameter: float
    ''' In mm. Use 3 for M3 screws '''
    
    base_thickness: float
    '''
    thickness in the middle of the plate
    USED FOR CADQUERY ONLY
    '''

    base_offset: float
    '''
    Both start flat/flush on the bottom.  This offsets the base up (if positive)
    USED FOR CADQUERY ONLY
    '''
    
    base_rim_thickness: float
    '''
    thickness on the outer frame with screws
    USED FOR CADQUERY ONLY
    '''

    screw_cbore_diameter: float
    '''
    USED FOR CADQUERY ONLY
    '''

    screw_cbore_depth: float
    '''
    USED FOR CADQUERY ONLY
    '''

    pcb_holes: bool
    '''
    Enable holes on plate for PCB mount
    '''

    pcb_mount_ref_offset: tuple[float]
    pcb_holder_size: tuple[float]
    pcb_holder_offset: tuple[float]

    pcb_usb_hole_size: tuple[float]
    pcb_usb_hole_offset: tuple[float]

    wall_thinner_size: tuple[float]

    trrs_hole_size: tuple[float]
    trrs_offset: tuple[float]

    pcb_screw_hole_size: tuple[float]
    pcb_screw_x_offsets: tuple[float]
    ''' for the screw positions off of reference '''
    pcb_screw_y_offset: float

    pcb_holes_xy_offset: tuple[float]

    pcb_holes_width: float
    
    pcb_holes_height: float
    
    pcb_holes_diameter: float
    
    pcb_holes_depth: float

    pcb_width: float
    '''
    Used for showing PCV for fit check
    '''

    pcb_height: float
    '''
    Used for showing PCV for fit check
    '''

    pcb_thickness: float
    '''
    Used for showing PCV for fit check
    '''
    
    pcb_hole_diameter: float
    '''
    Used for showing PCV for fit check
    '''
    
    pcb_hole_pattern_width: float
    '''
    Used for showing PCV for fit check
    '''

    pcb_hole_pattern_height: float
    '''
    Used for showing PCV for fit check
    '''

    pcb_clear: bool
    '''
    EXPERIMENTAL
    '''

    pcb_size: tuple[float]
    '''
    EXPERIMENTAL
    '''

    pcb_offset: tuple[float]
    '''
    this is off of the back of the plate size.
    EXPERIMENTAL
    '''