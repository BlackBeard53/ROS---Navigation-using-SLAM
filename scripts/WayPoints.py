#! /usr/bin/env python3
# author 1: Bipin Koirala
# author 2: Dongho Park
import rospy
import actionlib
from move_base_msgs.msg  import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseArray, Pose, Quaternion, Twist, Point

print ('Waiting for User Response: Please Provide 2D Pose Estimate in RViz') 

rospy.init_node('custom_waypoints')


def CustomWayPoints():
    # Create a dictionary to store waypoints
    points = dict()
    points['waypoint1'] = Pose(Point(2.5700, 0.53, 0.000), Quaternion(0.000, 0.000, 0.96, -0.256))
    points['waypoint2'] = Pose(Point(3.355, -0.6, 0.000), Quaternion(0.000, 0.000, 0.9999, 0.008))
    points['waypoint3'] = Pose(Point(0.354, -0.56, 0.000), Quaternion(0.000, 0.000, 0.96, 1.0))
    
    return points

'''Function to visuzlize waypoints in Rviz'''
def wayPointsRviz(waypointsList):
    publishArray = rospy.Publisher('/waypoints', PoseArray, queue_size = 1)
    waypoints = PoseArray()
    waypoints.header.frame_id = 'map'
    waypointPoses = []

    for key, value in waypointsList.items():
        waypointPoses.append(waypointsList[key])

    waypoints.poses = waypointPoses
    publishArray.publish(waypoints)

    return waypoints

def sendGoals(waypoints):
    '''Using message type PoseWithCovarianceStamped'''
    initial_pose = PoseWithCovarianceStamped()

    def update_initial_pose(initial_pose):
        initial_pose = initial_pose

    '''setting initial pose of TURTLEBOT3'''
    initial_pose = PoseWithCovarianceStamped()
    rospy.Subscriber('initialpose', PoseWithCovarianceStamped, update_initial_pose)

    '''Get initial position using RViz --- user needs to click on the map to estimate pose'''
    rospy.wait_for_message('initialpose', PoseWithCovarianceStamped)

    '''Subscribe to action server'''
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    #rospy.loginfo('Waiting for User Response: Please Provide 2D Pose Estimate in RViz ')
    client.wait_for_server() # waits for server to start listening for goals
    

    wayPointsRviz(waypoints) # display waypoints in RViz ---> red arrows

    '''Iterate over all three waypoints'''
    i = 1
    for key, value in waypoints.items():
        if i <= 3:
            print ('===================================')
            print ('Travelling to WayPoint {}'.format(i))

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position.x = waypoints[key].position.x
        goal.target_pose.pose.position.y = waypoints[key].position.y
        goal.target_pose.pose.position.z = waypoints[key].position.z

        goal.target_pose.pose.orientation.x = waypoints[key].orientation.x
        goal.target_pose.pose.orientation.y = waypoints[key].orientation.y
        goal.target_pose.pose.orientation.z = waypoints[key].orientation.z
        goal.target_pose.pose.orientation.w = waypoints[key].orientation.w

        client.send_goal(goal)
        #wait = client.wait_for_result(timeout = rospy.Duration(2))
        wait = client.wait_for_result()
        print ('WayPoint {} reached. Sleeping for 2 seconds'.format(i))
        print ('======================================')
        print ('                                      ')

        rospy.sleep(2)
        i += 1
    rospy.loginfo('All Goals Reached Successfully')

three_locs = CustomWayPoints()
send_goals = sendGoals(three_locs)

