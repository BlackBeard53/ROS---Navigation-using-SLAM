# ROS---Navigation-using-SLAM
![ScreenShot](gazebo_maze.png)

SLAM Mapped Env

_________________________________________

To simulate in provided gazebo_maze environemnt:
copy entire file to catkin_ws/src

----------------------------------------------------------
>> <pre><code>export TURTLEBOT3_MODEL=burger</pre></code> (or whichever model ...like waffle perhaps?)
>> <pre><code>roslaunch turtlebot3_gazebo turtlebot3_maze.launch</pre></code> (use turtlebot bringup if you want to use SLAM to generate map in real world. Then save the map in maps folder)
----------------------------------------------------------
>> <pre><code>export TURTLEBOT3_MODEL=burger</pre></code>
>> 
>> <pre><code>roslaunch insert_your_catkin_package_name turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/insert_your_catkin_package_name/maps/gazebo_maze.yaml</pre></code> (or use real map file if running in real world)
  
----------------------------------------------------------
>> <pre><code>cd ~/catkin_ws/src/insert_your_catkin_package_name/scripts && rosrun -insert your catkin package name- WayPoints.py</pre></code>

  NOTE: gazebo_maze.yaml was mapped using a custom environment. Feel free to map any envionemnt and use it instead of 'gazebo_maze' map.
