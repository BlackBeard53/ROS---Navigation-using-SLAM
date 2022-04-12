To simulate in provided gazebo_maze environemnt:
copy entire file to catkin_ws/src


I have already used SLAM to generate map of simulation maze environment.
----------------------------------------------------------
>> export TURTLEBOT3_MODEL=burger
>> roslaunch turtlebot3_gazebo turtlebot3_maze.launch (use turtlebot bringup if you want to use SLAM to generate map in real world. Then save the map in maps folder)
----------------------------------------------------------
>> export TURTLEBOT3_MODEL=burger
>> roslaunch bipark_lab5 turtlebot3_navigation.launch map_file:=$HOME/catkin_ws/src/bipark_lab5/maps/gazebo_maze.yaml (or use real map file if running in real world)
----------------------------------------------------------
>> cd ~/catkin_ws/src/bipark_lab5/scripts && rosrun bipark_lab5 WayPoints.py
----------------------------------------------------------
