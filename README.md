# Campus Rover Architecture
The goal of this repository is to design an architecture for the campus rover robot. This robot should be able to deliver small packages by navigating both indoor and outdoor terrain, along with handling issues like opening doors. Upon completion, this repository should provide a skeleton of the campus rover's design.

# Nodes
Below are all the nodes used within the campus rover, with documentation for usage.

## turtlebot3_teleop_key
Allows the campus rover to be controlled view teleop. This node takes in keyboard input, and publishes twists to the `cmd_vel` topic.

#### Publishers
* `cmd_vel`
	* Type: `Twist`
#### Subscribers
* None
