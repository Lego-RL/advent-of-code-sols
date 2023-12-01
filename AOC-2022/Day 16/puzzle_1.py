# with open("input.txt", "r") as f:
#     data = f.readlines()

with open("fakeinput.txt", "r") as f:
    data = f.readlines()


data = [x.strip("\n") for x in data]


class Valve:
    def __init__(self, valve_name: str, pressure: int, connections: list[str]):
        self.name = valve_name
        self.pressure = pressure
        self.connections = connections

    def __str__(self):
        return f"{self.name} @ {self.pressure}: connects to {self.connections}"


class Path:
    def __init__(
        self,
        start_valve: str,
        path: list[str],
        current_open_valves: list[str] = [],
        time_left: int = 30,
        pressure_release: int = 0,
    ):
        self.start_valve: str = start_valve
        self.path: list[str] = path
        self.current_open_valves: list[str] = current_open_valves

        self.time_left: int = time_left
        self.pressure_release: int = pressure_release

    def __str__(self):
        return f"released {self.pressure_release} with path: {self.path}"


valves: dict[str, Valve] = {}

for line in data:
    tokens: list[str] = line.split(" ")
    valve_name: str = tokens[1]
    valve_pressure: int = int(tokens[4].strip("rate=")[:-1])

    valve_tokens: list[str] = tokens[9:]
    valve_connections: list[str] = [
        valve if "," not in valve else valve[:-1] for valve in valve_tokens
    ]

    # valves.append(Valve(valve_name, valve_pressure, valve_connections))
    valves[valve_name] = Valve(valve_name, valve_pressure, valve_connections)

start_valve: Valve = valves["AA"]
# paths: list[Path] = []
paths: list[Path] = []
highest_path_pressure: int = 0

# initial path obj
start_path = Path(start_valve.name, ["AA"])
paths.append(start_path)

# while paths and (path := paths.pop()):
while paths:
    path: Path = paths.pop()

    at_valve: str = path.path[-1]
    at_valve_obj: Valve = valves[at_valve]

    # no more valves can be opened for pressure to be released
    # @ one minute left
    if path.time_left == 1:
        if path.pressure_release > highest_path_pressure:
            highest_path_pressure = path.pressure_release
        continue

    # if valve not open, append path where you open valve, and one
    # where you leave valve closed
    if at_valve_obj.name not in path.current_open_valves:
        # add path where open valve
        valve_pressure_release: int = (path.time_left - 1) * valves[at_valve].pressure
        new_path: Path = Path(
            path.start_valve,
            path.path,
            path.current_open_valves + [at_valve],
            path.time_left - 1,
            path.pressure_release + valve_pressure_release,
        )
        paths.append(new_path)

    for connection in at_valve_obj.connections:

        if len(path.path) > 1:
            if connection == path.path[-2]:
                continue

        new_path_lst: list[str] = path.path + [connection]
        new_path: Path = Path(
            path.start_valve,
            # path.path + [connection],
            new_path_lst,
            path.current_open_valves,
            path.time_left - 1,
            path.pressure_release,
        )
        paths.append(new_path)

    # [print(path) for path in paths]
    # exit()

print(highest_path_pressure)
