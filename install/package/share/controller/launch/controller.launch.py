
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():


    controller_node = Node(
        package='package',
        executable='controller_node',
        name='controller_node',
        parameters=[{
            'cmd_vel_topic': '/cmd_vel',
            'dominant_color_topic': '/dominant_color',
            'color_sensor_topic': '/turtle1/color_sensor',
        }]
    )

    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim_node'
    )



    return LaunchDescription([controller_node, turtlesim_node])