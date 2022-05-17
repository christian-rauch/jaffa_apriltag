
# Install
Clone into workspace and resolve dependencies:
```sh
rosdep install --from-paths src --ignore-src -y
colcon build
```

# Setup
Print the tags in [`tags.pdf`](tags/tags.pdf) at 100% scale. See [`tags.tex`](tags/tags.tex) for printing the tag images and `config/tags.yaml` for the setup.

# Usage
Run the Azure Kinect launch file [`kinect_rgbd.launch`](https://github.com/microsoft/Azure_Kinect_ROS_Driver/blob/melodic/launch/kinect_rgbd.launch) and then start the AprilTag detection via:
```sh
. install/setup.sh
roslaunch jaffa_apriltag apriltag.launch
```

A debug image with the detected tags is published on topic `/tag_detections_image`.
