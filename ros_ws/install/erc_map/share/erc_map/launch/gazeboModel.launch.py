import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node
import xacro



def generate_launch_description():


    robotXacroName='differential_drive_robot'

    namePackage='robot_wheel'
    modelFileRelPath='model/robot.xacro'
    worldFileRelPath='world/mars.world'

    pathModelFile=os.path.join(get_package_share_directory(namePackage),modelFileRelPath)
    pathWorldFile=os.path.join(get_package_share_directory(namePackage),worldFileRelPath)

    gazeboRosPackageLaunch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'))

    gazeboLaunch=IncludeLaunchDescription(gazeboRosPackageLaunch,launch_arguments={'world':"/media/exhausted/DATA DRIVE/stuff/mrm/ERC-2025/gitstuff/ERC-2024_AIA_2026/ros_ws/src/erc_map/world/mars.world"}.items())

   


    LaunchDescriptionObject=LaunchDescription()
    LaunchDescriptionObject.add_action(gazeboLaunch)
    return LaunchDescriptionObject


