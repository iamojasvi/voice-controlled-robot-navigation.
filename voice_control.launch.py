from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='voice_control_nav',
            executable='speech_to_text',
            name='speech_to_text'
        ),
        Node(
            package='voice_control_nav',
            executable='voice_navigation',
            name='voice_navigation'
        )
    ])
