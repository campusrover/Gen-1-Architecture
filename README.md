# Campus Rover Architecture
The goal of this repository is to design an architecture for the campus rover robot. This robot should be able to deliver small packages by navigating both indoor and outdoor terrain, along with handling issues like opening doors. Upon completion, this repository should provide a skeleton of the campus rover's design.

# Usage

## installation
To install the package, navigate to your ROS workspace and use the command `git clone https://github.com/campusrover/Gen-1-Architecture.git campus_rover`. After executing this command, navigate to the root of your ROS workspace and run the command `catkin_make`.

# Nodes
Below are all the nodes used within the campus rover, with documentation for usage.

## teleop
Allows the campus rover to be controlled via teleop.

#### Publishers

* `teleop`
	* Type: `Twist`
* `teleop/state`
	* Type: `Int32`
 
#### Subscribers
none


## mux
Subscribes to the `state` node to determine the current state of the robot (teleoping or navigating). Based on the state, it publishes to `/driver` either a teleop twist or a navigation twist. 

#### Publishers

* `mux`
	* Type: `Twist` 

#### Subscribers

* `state`
	* Type: `Int32`
* `fake_navigation`
	* Type: `Twist`
* `teleop`
	* Type: `Twist`

## driver
Recieves a twist from `mux` that it publishes to `cmd_vel` 

#### Publishers

* `cmd_vel`
	* Type: `Twist` 

#### Subscribers

* `mux`
	* Type: `Twist`

## state
Subscribes to the `teleop` and `fake_navigation`. Currently, it receives either 0 or 1 telling it whether the robot is teleoping or navigating.

0 = teleop
1 = navigate

#### Publishers

* `state`
	* Type: `Int32` 

#### Subscribers

* `teleop/state`
	* Type: `Int32`

## fake_navigation
A placeholder for navigation algorithm. Currently, drives straight only.


#### Publishers
* `fake_navigation`
	* Type: `Twist` 

#### Subscribers
none
