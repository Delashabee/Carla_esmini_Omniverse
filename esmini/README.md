#### 🛣️ Creating OpenDRIVE (.xodr) Files

OpenDRIVE defines the road network. You can create `.xodr` files using the following methods:

1. **Road Design Tools:**
   - [RoadRunner](https://www.mathworks.com/products/roadrunner.html) (commercial, with .xodr export)
   - [OpenDRIVE Designer](https://github.com/esmini/openodr-designer) (open-source GUI)
   - Manual editing in text editor using existing `.xodr` examples

2. **Best Practices:**
   - Use a consistent coordinate system (esmini assumes Z-up)
   - Start with a simple road (e.g., straight with lane markings) and test it in esmini

3. **Usage in esmini:**
   - Once you have a `.xodr` and a corresponding `.xosc`, run:
     ```bash
     ./esmini path/to/your_scenario.xosc
     ```

#### 🎬 Creating OpenSCENARIO (.xosc) Files

OpenSCENARIO defines how vehicles behave. You can create `.xosc` files by:

1. **Manual XML editing:**
   - Define catalog references (vehicle types)
   - Set initial positions using `Init`, and define behaviors using `Storyboard`
   - Use existing esmini examples as templates

2. **Scenario Editors:**
   - [ScenarioEditor](https://github.com/esmini/OpenSCENARIOEditor)
   - Other tools (e.g., dSPACE, VIRES, etc.)

3. **Test Tips:**
   - Always test your `.xosc` in esmini before attempting to port the logic elsewhere
   - Visualize via esmini GUI to debug start positions and actions
