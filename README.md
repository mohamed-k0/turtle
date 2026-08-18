# turtle Control

- This project is a *ROS2 package* that consists of one **controller node** that is responsible for controlling the movement of the turtle in *turtleSim* and reading the color of the background

--- 

- **The velocity commands** are published by the controller node through "/cmd_vel" topic; And that in turn required *remapping* the topic that the turtle subscribes to normally.

---

- **The perception** of controller node subscribes to the default *color sensor* topic of turtlesim node where it publishes the values of *color channels*(i.e. Red, Green, Blue).


- The controller node takes the reading of color values and then determines the **dominant color** that is then published to the "/dominant_color" topic.

---

### dependencies:

/>> This program uses **pynput** library to read the keyboard keys *globally*.

/>> Parameters are declared using **declare_parameter()** function inherited from *Node* imported from *rclpy.node*.

