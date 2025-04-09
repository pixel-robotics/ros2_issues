import launch
from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer, Node
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    # 1. Composable container loading the composable publisher ("simple" variant)
    composable_container = ComposableNodeContainer(
        name='publisher_simple_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',  # or use 'component_container_mt' for multi-threaded execution
        composable_node_descriptions=[
            ComposableNode(
                package='ros2_issues',
                plugin='TestPublisher<ros2_issues::msg::TestArraySimple>',
                name='publisher_simple_composable'
            ),
        ],
        output='screen'
    )

    # 2. Standalone node launched in simple mode (using the "-s" command-line option)
    simple_node = Node(
        package='ros2_issues',
        executable='publisher_node',  # this executable should support a "-s" mode
        name='publisher_simple_exe',
        arguments=['-s'],
        output='screen'
    )

    # 3. Standalone node launched in events executor mode (using the "-e" command-line option)
    events_executor_node = Node(
        package='ros2_issues',
        executable='publisher_node',  # this executable should support a "-e" mode
        name='publisher_event_executor_exe',
        arguments=['-e'],
        output='screen'
    )

    return LaunchDescription([
        composable_container,
        simple_node,
        events_executor_node
    ])
