# Campus Rover Architecture
The goal of this repository is to design an architecture for the campus rover robot. This robot should be able to deliver small packages by navigating both indoor and outdoor terrain, along with handling issues like opening doors. Upon completion, this repository should provide a skeleton of the campus rover's design.

# Nodes
Below are all the nodes used within the campus rover, with documentation for usage.

## teleop
Allows the campus rover to be controlled via teleop. This node takes in keyboard input, and publishes twists to the `cmd_vel` topic.

## mux
Subscribes to the `state` node to determine the current state of the robot (teleoping or navigating). Based on the state, it publishes to `/driver` either a teleop twist or a navigation twist. 

## driver
Recieves a twist from `mux` that it publishes to `/cmd_vel` 

## state
Subscribes to the `teleop` and `fake_navigation`. Currently, it receives either 0 or 1 telling it whether the robot is teleoping or navigating.

0 = teleop
1 = navigate

## fake_navigation
A placeholder for navigation algorithm. Currently, drives straight only.


#### Publishers
* `cmd_vel`
	* Type: `Twist`
* `mux`
	* Type: `Twist` 
* `state`
	* Type: `Int32`

#### Subscribers
* `state`
	* Type: `Int32`
* `fake_navigation`
	* Type: `Twist`
* `teleop`
	* Type: `Twist`
