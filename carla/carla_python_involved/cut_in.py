import glob
import sys
import os
import time

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

def main():
    client = carla.Client("localhost", 2000)
    client.set_timeout(10.0)

    xodr_path = os.path.expanduser("~/esmini/resources/xodr/e6mini.xodr")
    with open(xodr_path, 'r') as f:
        xodr_content = f.read()
    world = client.generate_opendrive_world(xodr_content)
    print("[INFO] Map loaded.")

    blueprint_library = world.get_blueprint_library()
    ego_bp = blueprint_library.filter("vehicle.tesla.model3")[0]
    overtaker_bp = blueprint_library.filter("vehicle.audi.tt")[0]

    waypoints = world.get_map().generate_waypoints(2.0)
    for wp in waypoints:
        loc = wp.transform.location
        world.debug.draw_string(loc, f"lane: {wp.lane_id}", draw_shadow=False,
                                color=carla.Color(r=255, g=0, b=0), life_time=10.0, persistent_lines=False)
    for wp in waypoints:
        start = wp.transform.location + carla.Location(z=0.5)
        direction = wp.transform.get_forward_vector()
        end = start + direction * 2.0  # 箭头长度
        world.debug.draw_arrow(start, end, thickness=0.1, arrow_size=0.3,
                            color=carla.Color(r=0, g=255, b=0), life_time=10.0)

    forward_wps = [wp for wp in waypoints if wp.lane_id < 0]  # same direction lanes

    if len(forward_wps) < 120:
        print("[ERROR] Not enough forward waypoints.")
        return

    ego_wp = forward_wps[100]
    overtaker_wp = forward_wps[80]

    ego_transform = ego_wp.transform
    ego_transform.location.z += 0.5
    overtaker_transform = overtaker_wp.transform
    overtaker_transform.location.z += 0.5

    ego = world.try_spawn_actor(ego_bp, ego_transform)
    overtaker = world.try_spawn_actor(overtaker_bp, overtaker_transform)

    if not ego or not overtaker:
        print("[ERROR] Failed to spawn one or both vehicles.")
        return

    print("[INFO] Vehicles spawned.")
    print("Ego:", ego.get_location())
    print("Overtaker:", overtaker.get_location())

    # Overhead camera
    spectator = world.get_spectator()
    midpoint = ego.get_location() + (overtaker.get_location() - ego.get_location()) * 0.5
    midpoint.z += 50
    spectator.set_transform(carla.Transform(midpoint, carla.Rotation(pitch=-90)))

    # Ego steady
    ego.apply_control(carla.VehicleControl(throttle=0.2))

    time.sleep(2)

    # Overtaker speeds up
    overtaker.apply_control(carla.VehicleControl(throttle=0.6))
    time.sleep(2)

    # Smooth lane change (simulate cut-in)
    overtaker.apply_control(carla.VehicleControl(throttle=0.6, steer=-0.3))
    time.sleep(1.0)

    # 加一个轻微“右打方向”纠正车头偏移
    overtaker.apply_control(carla.VehicleControl(throttle=0.6, steer=+0.3))
    time.sleep(1.0)

    # 回正方向盘
    overtaker.apply_control(carla.VehicleControl(throttle=0.6, steer=0.0))
    time.sleep(3.0)


    print("[INFO] Overtaker cut-in done.")

    # Brake
    overtaker.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
    print("[INFO] Overtaker braking.")

    time.sleep(4)

    # Cleanup
    ego.destroy()
    overtaker.destroy()
    print("[INFO] Scenario complete.")

if __name__ == '__main__':
    main()
