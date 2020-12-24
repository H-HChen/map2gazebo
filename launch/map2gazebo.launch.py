import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():
    config = Path(get_package_share_directory('map2gazebo'), 'default.yaml')

    return LaunchDescription([

        Node(
            package='map2gazebo',
            executable='map2gazebo',
            name='map2gazebo',
            output='screen',
            parameters=[config],
        ),
    ])
