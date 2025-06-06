# Learning & Integration Notes

This document summarizes the learning process, pitfalls, and future plans for integrating CARLA, esmini, and Omniverse.

---

## Learning Roadmap

### esmini

- Explored and successfully ran example scenarios such as:
  - `basic_cut_in.xosc`: Demonstrates a cut-in maneuver using OpenSCENARIO
  - `esmini_gui`: Observed how ego vehicle follows a predefined path
  - more info can be found in esmini/README.md

### CARLA Python API

- Learned how to:
  - Spawn and control vehicles
  - Attach camera and Lidar sensors
  - Retrieve sensor data (image, point cloud)
  - Export ego vehicle trajectory
  - more infor can be found in carla/README.md

---

## Pitfalls & Debug Notes

### esmini Installation

- On Linux, required installing SDL2 and GLM manually
- CMake build worked well, but runtime dependencies were undocumented

### CARLA ↔ Omniverse (USD) Interfacing

- CARLA does not export `.usd` directly
- Required intermediate formats (e.g., `.fbx`, `.obj`) and use of Omniverse USD Composer to convert
- Coordinate systems differ; needed adjustments during import

---

## CARLA + Omniverse Interface Plans

### Tools Explored

- USD Composer (Omniverse) for manual scene loading
- Omniverse Kit SDK (planned) for scripting and live editing

### File Formats

- Target: `.usd` or `.usdc` (binary format)
- Attempted: Converting CARLA maps and meshes for loading in Omniverse

### Results So Far

- Partial success loading static scene
- Sensor integration and animation still pending

---

## Future Plans (TODO)

- [ ] Export and visualize CARLA sensor data (camera, lidar) as `.usd` assets
- [ ] Use esmini scenarios to influence CARLA ego behavior
- [ ] Live connection between CARLA runtime and Omniverse Composer for visualization
- [ ] Evaluate Omniverse Isaac Sim as an alternative integration path

---


