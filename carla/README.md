## 🤝 Integrating esmini and CARLA (Conceptual Guide)

Although esmini and CARLA are standalone simulators, combining their strengths is possible through a hybrid workflow.

### Goal

Use esmini to:
- Define vehicle behaviors and maneuvers using OpenSCENARIO
Use CARLA to:
- Render high-fidelity 3D simulation
- Simulate realistic physics, sensors, and weather

### ⚠Challenges

- CARLA **does not natively support OpenSCENARIO or OpenDRIVE** formats (except in some forks or via third-party tools)
- esmini uses its own simple physics engine, while CARLA has complex dynamic modeling

### Possible Solutions

#### 1. Use esmini as a behavior planner

- Parse `.xosc` files in Python
- Extract vehicle intentions (lane change, braking, speed profiles)
- Re-implement them as CARLA Python API commands (e.g., apply control)

#### 2. Road network synchronization

- Export `.xodr` files and try matching them to CARLA maps (requires modification)
- Alternatively, accept the mismatch and focus only on behavior synchronization

#### 3. Time synchronization (Advanced)

- Run esmini and CARLA in parallel
- Communicate via middleware (e.g., ROS bridge or custom WebSocket server)
- Use esmini to publish planned trajectories and CARLA to execute and render them

###  Tools That May Help

- **pyOpenSCENARIO**: For parsing `.xosc` files
- **CARLA ROS Bridge**: For real-time control and integration
- **CARLA Map Editor**: For custom road networks if `.xodr` import is not feasible

### Current Status (based on this repo)

- esmini scenarios running independently and visualized via GUI
- CARLA Python scripts can simulate basic versions of those scenarios
- Live integration not yet established — under future consideration
