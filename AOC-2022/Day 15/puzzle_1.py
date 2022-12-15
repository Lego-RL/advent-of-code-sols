from math import sqrt

with open("input.txt", "r") as f:
    data = f.readlines()

# with open("fakeinput.txt", "r") as f:
#     data = f.readlines()


data = [x.strip("\n") for x in data]


def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


class Sensor:
    def __init__(self, sensor_x: int, sensor_y: int, beacon_x: int, beacon_y: int):
        self.sensor_x: int = sensor_x
        self.sensor_y: int = sensor_y
        self.sensor_coords: tuple[int, int] = (sensor_x, sensor_y)

        self.beacon_x: int = beacon_x
        self.beacon_y: int = beacon_y
        self.beacon_coords: tuple[int, int] = (beacon_x, beacon_y)

        self.man_dist: int = manhattan(self.sensor_coords, self.beacon_coords)

    def __str__(self):
        return f"Sensor @ {self.sensor_x}, {self.sensor_y}; beacon - {self.beacon_x}, {self.beacon_y}"


sensors: list[Sensor] = []
beacons: set[tuple[int, int]] = set()
# process input
for line in data:
    shorter_line: str = line.strip("Sensor at ")
    sensor_coords: list[str] = shorter_line.split(",")
    sensor_coords[1] = sensor_coords[1].strip()

    colon_idx: int = sensor_coords[1].find(":")

    sensor_x, sensor_y = int(sensor_coords[0][2:]), int(sensor_coords[1][2:colon_idx])

    shorter_line = shorter_line[shorter_line.index("is at") + 5 :]

    beacon_coords: list[str] = shorter_line.split(",")
    beacon_coords[1] = beacon_coords[1].strip()

    beacon_x, beacon_y = int(beacon_coords[0][3:]), int(beacon_coords[1][2:])
    sensor: Sensor = Sensor(sensor_x, sensor_y, beacon_x, beacon_y)
    sensors.append(sensor)
    beacons.add(sensor.beacon_coords)

# TARGET_ROW: int = 10
TARGET_ROW: int = 2000000

min_x, max_x = sensors[0].sensor_x, sensors[0].sensor_x
min_y, max_y = sensors[0].sensor_y, sensors[0].sensor_y

# find bounds of sensor area
for sensor in sensors:

    beacon_x_dist = abs(sensor.sensor_x - sensor.beacon_x)
    beacon_y_dist = abs(sensor.sensor_y - sensor.beacon_y)

    if (furthest_left := sensor.sensor_x - beacon_x_dist) < min_x:
        min_x = furthest_left

    if (furthest_right := sensor.sensor_x + beacon_x_dist) > max_x:
        max_x = furthest_right

    if (furthest_up := sensor.sensor_y - beacon_y_dist) < min_y:
        min_y = furthest_up

    if (furthest_down := sensor.sensor_y + beacon_y_dist) > max_y:
        max_y = furthest_down

print(beacons)
print(f"{min_x=}, {max_x=}")

impossible_beacon_locs: set[tuple[int, int]] = set()
for i in range(min_x, max_x + 1):
    coord: tuple[int, int] = (i, TARGET_ROW)

    # skip spaces where beacons already exist
    if coord in beacons:
        continue

    for sensor in sensors:
        dist_to_sensor = manhattan(coord, sensor.sensor_coords)
        if dist_to_sensor <= sensor.man_dist:
            impossible_beacon_locs.add(coord)
            break

print(len(impossible_beacon_locs))
