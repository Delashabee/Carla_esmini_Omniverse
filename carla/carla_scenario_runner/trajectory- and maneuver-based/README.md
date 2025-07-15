1. Trajectory-based approach

Definition:

Scenario description method based on the actual measured trajectory of the vehicle (e.g., GNSS coordinates).

The description method is mainly to record the exact coordinates, relative position, velocity distribution, and trajectory shape of the vehicle.

Peculiarity:

Merit:

The real driving path of the vehicle can be reproduced very accurately.

Ideal for accurately reproducing recorded driving scenarios.

Shortcoming:

The reusability of the scene is poor, and it is difficult to transfer the scene to a new road or traffic environment due to the original road geometry conditions.

It is difficult to make flexible modifications to the trajectories, such as adjusting the trajectories in different road environments to accommodate new test needs.

2. Maneuver-based approach

Definition:

A high-level abstraction method based on driving actions (Maneuver, e.g. changing lanes, overtaking, braking, etc.).

Instead of being described in terms of coordinates and trajectories, the scene is represented by a sequence of driving actions, such as "follow the car first and then change lanes to overtake".

Peculiarity:

Merit:

It is more flexible, easy to parameterize and modify, and can be transferred between different scenarios and different road geometry conditions.

It facilitates the creation of a large number of varied, more general test scenarios to enhance the validation of autonomous driving systems.

Shortcoming:

Abstract descriptions are more complex and require a clear definition of the action and the start and end conditions.

It is difficult to accurately describe very detailed vehicle behavior (such as precise lateral displacement, speed fluctuations and other microscopic features), and there are certain abstraction errors.