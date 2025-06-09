Record sensor data in CARLA
Use CARLA's Python API to capture outputs from sensors such as cameras, LiDAR, and radar.

Convert the data into .usd files (or intermediate formats like point clouds)
Transform image or point cloud data into formats recognizable by NVIDIA Omniverse, such as:

    Point clouds: convert to .ply or .usd point structures

    Images: use as texture maps or camera view inputs

    Sensor poses and trajectories: represent them as USD animations or stage objects

Upload to Omniverse Cloud for visual rendering, data augmentation, and environment reconstruction
Use Omniverse Cloud’s rendering engine (e.g., RTX ray tracing) to generate high-quality simulated images in the cloud, and perform:

    Scene visualization

    Multi-angle data generation

    Enhanced processing with dynamic objects and weather variations

Inject custom sensor models into the simulation via Cloud API
Use NVIDIA Omniverse Cloud APIs to dynamically load your own sensor models (e.g., customized radar, ultrasonic sensors, camera parameters) into the simulation environment for further training and algorithm testing.
