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

# min_x, max_x = 0, 20
# min_y, max_y = 0, 20

min_x, max_x = 0, 4000000
min_y, max_y = 0, 4000000

# find bounds of sensor area


# loop over every row/y value and determine whether sensors
# cover the entire row or not
for y in range(max_y + 1):
    if y % 10000 == 0:
        print(y)
    ranges: list[tuple[int, int]] = []

    for sensor in sensors:
        # check if sensor even reaches this row, skip if not
        if sensor.sensor_y < y and ((sensor.sensor_y + sensor.man_dist) < y):
            continue

        if sensor.sensor_y > y and ((sensor.sensor_y - sensor.man_dist) > y):
            continue

        max_x_reach: int = sensor.man_dist - abs(sensor.sensor_y - y)
        furthest_left, furthest_right = (
            sensor.sensor_x - max_x_reach,
            sensor.sensor_x + max_x_reach,
        )

        if furthest_left < 0:
            furthest_left = 0

        if furthest_right > 4000000:
            furthest_right = 4000000

        ranges.append((furthest_left, furthest_right))

    # sort each range by their leftmost value
    ranges = sorted(ranges, key=lambda x: x[0])
    furthest = ranges[0][1]

    for range in ranges:
        if range[0] > furthest + 1:
            skipped_range: tuple[int, int] = (furthest + 1, y)
            tuning_freq: int = (skipped_range[0] * 4000000) + skipped_range[1]
            print(f"skipped {furthest+1}, {y} - {tuning_freq=}")
            exit()

        if range[1] > furthest:
            furthest = range[1]
