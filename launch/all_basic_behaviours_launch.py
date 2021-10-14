from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('drone_id', default_value='drone0'),
        Node(
            package='as2_basic_behaviours',
            executable='takeoff_behaviour_node',
            name='takeoff_behaviour_node',
            namespace=LaunchConfiguration('drone_id'),
            output='screen',
            emulate_tty=True
        ),
        Node(
            package='as2_basic_behaviours',
            executable='land_behaviour_node',
            name='land_behaviour_node',
            namespace=LaunchConfiguration('drone_id'),
            output='screen',
            emulate_tty=True
        ),
        Node(
            package='as2_basic_behaviours',
            executable='gotowaypoint_behaviour_node',
            name='gotowaypoint_behaviour_node',
            namespace=LaunchConfiguration('drone_id'),
            output='screen',
            emulate_tty=True
        ),
        Node(
            package='as2_basic_behaviours',
            executable='follow_path_behaviour_node',
            name='follow_path_behaviour_node',
            namespace=LaunchConfiguration('drone_id'),
            output='screen',
            emulate_tty=True
        )
    ])