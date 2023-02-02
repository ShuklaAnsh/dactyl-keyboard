from dataclasses import dataclass
from math import pi
from typing import Literal
from config_model.bottom_plate import BottomPlateConfig
from config_model.controller import ControllerConfig
from config_model.export import ExportConfig
from config_model.oled import OLEDConfig
from config_model.screw import ScrewConfig
from config_model.shape import ShapeConfig
from config_model.switch import SwitchConfig


@dataclass
class DactylManuform:
    ''' Keyboard configuration '''

    engine: Literal["solid", "cadquery"]
    '''
    Engine to generate models
        - None: engine will be picked via environment variable
        - `solid`: generates OpenSCAD files
        - `cadquery`: generates step files
    '''

    exportConfig: ExportConfig
    ''' Export Configuration. '''

    shapeConfig: ShapeConfig
    ''' Configuration for the keyboard to define its shape '''

    switchConfig: SwitchConfig
    ''' Switch Hole Configuration '''

    oledConfig: OLEDConfig
    ''' Oled Mount Configuration '''

    screwConfig: ScrewConfig
    ''' Screw Insert Configuration '''

    controllerConfig: ControllerConfig
    ''' Controller Mount / Connectors Configuration '''

    plateConfig: BottomPlateConfig
    ''' Bottom plate + PCB Configuration '''


d2r = pi / 180
r2d = 180 / pi

exportConfig = ExportConfig(
    save_dir="../things",
    parts_dir="./parts",
    config_name="dm"
)

shapeConfig = ShapeConfig(
    show_caps="MX",
    show_pcbs=False,
    nrows=5,
    ncols=6,
    col_curve=pi/12.0,
    row_curve=pi/36.0,
    tenting=3,
    tilt=3,
    tenting_angle=pi/12.0,
    symmetry="symmetric",
    column_style="orthographic",
    column_offsets=[
        [0, 0, 0],
        [0, 0, 0],
        [0, 2.82, -4.5],
        [0, 0, 0],
        [0, -6, 5],# REDUCED STAGGER
        [0, -6, 5],# REDUCED STAGGER
        [0, -6, 5],# NOT USED IN MOST FORMATS (7th column)
    ],
    thumb_offset=[6, -3, 7],
    keyboard_z_offset=9,
    extra_height=1.0,
    extra_width=2.5,
    skeletal_walls=False,
    wall_z_offset=15,  # length of the first downward_sloping part of the wall
    # offset in the x and/or y direction for the first downward_sloping part of the wall (negative)
    wall_x_offset=5,
    # offset in the x and/or y direction for the first downward_sloping part of the wall (negative)
    wall_y_offset=6,
    # specific values for the left side due to the minimal wall.
    left_wall_x_offset=12,
    # specific values for the left side due to the minimal wall.
    left_wall_z_offset=3,
    left_wall_lower_x_offset=0,  # specific values for the lower left corner.
    left_wall_lower_y_offset=0,  # specific values for the lower left corner.
    left_wall_lower_z_offset=0,
    wall_thickness=4.5,  # wall thickness parameter used on upper/mid stage of the wall
    wall_base_y_thickness=4.5,  # wall thickness at the lower stage
    wall_base_x_thickness=4.5,  # wall thickness at the lower stage
    # wall thickness at the lower stage in the specifically in back for interface.
    wall_base_back_thickness=4.5,
)
if (shapeConfig.ncols >= 4):
    shapeConfig.col_offset = [0, -12, 5.54]
elif (shapeConfig.ncols == 2):
    shapeConfig.col_offset = [0, 2.82, -4.5]
else:
    shapeConfig.col_offset = [0, 0, 0]

if (shapeConfig.column_style == "fixed"):
    # The defaults roughly match Maltron settings
    #   http://patentimages.storage.googleapis.com/EP0219944A2/imgf0002.png
    # fixed_z overrides the z portion of the column ofsets above.
    # NOTE: Apparently "THIS DOESN'T WORK QUITE LIKE I'D HOPED."
    shapeConfig.fixed_angles = [
        d2r * 10, d2r * 10, 0, 0, 0, d2r * -15, d2r * -15]
    shapeConfig.fixed_x = [-41.5, -22.5, 0, 20.3, 41.4,
                           65.5, 89.6]  # relative to the middle finger
    shapeConfig.fixed_z = [12.1, 8.3, 0, 5, 10.7, 14.5, 17.5]
    shapeConfigfixed_tenting = d2r * 0

switchConfig = SwitchConfig(
    plate_style="HS_UNDERCUT",
    switch_size=14.0,
    notch_width=6.0,
    sa_profile_key_height=12.7,
    sa_length=18.5,
    sa_double_length=37.5,
    plate_thickness=4 + 1.1,
    plate_rim=1.5 + 0.5,
    clip_thickness=1.1,
    clip_undercut=1.0,
    undercut_transition=0.2,
    plate_file=None,
    plate_offset=0.0
)

oledConfig = OLEDConfig(
    oled_center_row=1,  # if not None, this will override the oled_mount_location_xyz and oled_mount_rotation_xyz settings
    # Z offset tweaks are expected depending on curvature and OLED mount choice.
    oled_translation_offset=(0, 0, 4),
    oled_rotation_offset=(-15, -25, 95),  # Rotatation offset of the OLED
    oled_screen_length=15.5,
    oled_screen_width=30,
    oled_height=34 + 0.2,  # whole OLED length
    oled_width=36 + 0.2,  # whole OLED width,
    oled_depth=15.0,  # whole module depth
    oled_thickness=4.3,  # thickness of OLED, plus clearance.  Must include components
    oled_mount_rim=1.5,
    oled_mount_cut_depth=20.0,
    # will be overwritten if oled_center_row is not None
    oled_mount_location_xyz=(-78.0, 20.0, 42.0),
    # will be overwritten if oled_center_row is not None
    oled_mount_rotation_xyz=(12.0, 0.0, -6.0),
    oled_left_wall_x_offset_override=50.0,
    oled_left_wall_z_offset_override=2.0,
    oled_left_wall_lower_y_offset=0.0,
    oled_left_wall_lower_z_offset=0.0,
    oled_mount_connector_hole=7.5,
    oled_screen_start_from_conn_end=6.5,
    oled_clip_bezel_chamfer=2.0,  # depth of the 45 degree chamfer
    oled_clip_bezel_thickness=3.5,  # z thickness of clip bezel
    oled_clip_thickness=1.5,
    oled_clip_width=6.0,
    oled_clip_overhang=1.0,
    oled_clip_extension=5.0,
    oled_clip_width_clearance=0.5,
    oled_clip_undercut=0.5,
    oled_clip_undercut_thickness=2.5,
    oled_clip_y_gap=0.2,
    oled_clip_z_gap=0.2,
)

screwConfig = ScrewConfig(
    screws_offset="OUTSIDE",
    screw_insert_height=5.0,
    screw_insert_bottom_radius=5.21 / 2,
    screw_insert_top_radius=5.10 / 2,
    screw_insert_outer_radius=4.25
)

controllerConfig = ControllerConfig(
    controller_mount_type="EXTERNAL",
    external_holder_height=12.5,
    external_holder_width=28.75,
    external_holder_xoffset=-5.0,
    external_holder_yoffset=-4.5,
)

plateConfig = BottomPlateConfig(
    ###################################
    # Bottom Plate Dimensions
    ###################################
    screw_hole_diameter=3,
    # USED FOR CADQUERY ONLY
    base_thickness=3.0,  # thickness in the middle of the plate
    # Both start flat/flush on the bottom.  This offsets the base up (if positive)
    base_offset=3.0,
    base_rim_thickness=5.0,  # thickness on the outer frame with screws
    screw_cbore_diameter=6.0,
    screw_cbore_depth=2.5,

    ###################################
    ## PCB Screw Mount               ##
    ###################################
    pcb_mount_ref_offset=[0, -5, 0],
    pcb_holder_size=[34.6, 7, 4],
    pcb_holder_offset=[8.9, 0, 0],

    pcb_usb_hole_size=[7.5, 10.0, 4],
    pcb_usb_hole_offset=[15, 0, 4.5],

    wall_thinner_size=[34, 7, 10],

    trrs_hole_size=[3, 20],
    trrs_offset=[0, 0, 1.5],

    pcb_screw_hole_size=[.5, 10],
    # for the screw positions off of reference
    pcb_screw_x_offsets=[- 5.5, 7.75, 22],
    pcb_screw_y_offset=-2,

    # Offset is from the top inner corner of the top inner key.

    ###################################
    # HOLES ON PLATE FOR PCB MOUNT
    ###################################
    pcb_holes=True,
    pcb_holes_xy_offset=(0.0, 0.0),
    pcb_holes_width=14.3,
    pcb_holes_height=14.3,
    pcb_holes_diameter=1.6,
    pcb_holes_depth=20.0,

    ###################################
    # EXPERIMENTAL
    pcb_clear=False,
    pcb_size=(18.5, 18.5, 5),
    pcb_offset=(0, 0, 0),  # this is off of the back of the plate size.
    ###################################

    ###################################
    # SHOW PCB FOR FIT CHECK
    ###################################
    pcb_width=18.0,
    pcb_height=18.0,
    pcb_thickness=1.5,
    pcb_hole_diameter=2,
    pcb_hole_pattern_width=14.3,
    pcb_hole_pattern_height=14.3,
)

dm = DactylManuform(
    engine=None,
    exportConfig=exportConfig,
    shapeConfig=shapeConfig,
    switchConfig=switchConfig,
    screwConfig=screwConfig,
    controllerConfig=controllerConfig,
    plateConfig=plateConfig
)
