"""Advent Of Code 2022 : Day 15
"""
from utils import get_input
import numpy as np
from tqdm import tqdm


raw_input = get_input(day=15)


def get_sensors_and_closest_beacon():
    sensors_and_beacons = []
    for line in raw_input:
        sensor_data, beacon_data = line.split(": ")
        sensor_position = tuple([
            int(sensor_part.split(" ")[-1].split("=")[-1])
            for sensor_part in sensor_data.split(", ")
        ])
        
        beacon_position = tuple([
            int(beacon_part.split(" ")[-1].split("=")[-1])
            for beacon_part in beacon_data.split(", ")
        ])
        
        sensors_and_beacons.append((
            sensor_position,
            beacon_position
        ))
    return sensors_and_beacons


sensors = np.asarray([sensor for sensor, _ in get_sensors_and_closest_beacon()])
beacons = np.asarray([beacon for _, beacon in get_sensors_and_closest_beacon()])
np_manhattan_distances = np.abs(sensors - beacons).sum(1)
def manhattan_distance(sensor_id):
    return np_manhattan_distances[sensor_id]


def get_clear_points_on_row(sensors_and_beacons: list[tuple], wanted_row: int,
                            max_column: int = None,
                            remove_beacons: bool = True):
    beacons = set()
    clear_points = set()
    for sensor_id, (sensor, beacon) in enumerate(sensors_and_beacons):
        beacons.add(beacon)
        beacon_distance = manhattan_distance(sensor_id)
        row_distance = abs(sensor[1] - wanted_row)
        
        if beacon_distance >= row_distance:  # row covered
            x_distance = abs(beacon_distance - row_distance)
            for clear_point_x in range(sensor[0] - x_distance, sensor[0] + x_distance + 1):
                if not max_column or clear_point_x <= max_column:
                    clear_points.add((clear_point_x, wanted_row))
    
    if remove_beacons:
        return clear_points - beacons
    return clear_points


def part1():
    sensors_and_beacons = get_sensors_and_closest_beacon()

    wanted_row = 10

    return len(get_clear_points_on_row(sensors_and_beacons, wanted_row))


def part2():
    sensors_and_beacons = get_sensors_and_closest_beacon()
    
    max_coord_value = 4_000_000
    
    min_x = 0
    max_x = 0
    
    tmp_points = {}
    for y_value in tqdm(range(max_coord_value + 1)):
        definitly_not_beacon_points = get_clear_points_on_row(
            sensors_and_beacons,
            wanted_row=y_value,
            max_column=max_coord_value,
            remove_beacons=False
        )
        min_x = min(min_x, min(definitly_not_beacon_points, key=lambda x: x[0])[0])
        max_x = max(max_x, max(definitly_not_beacon_points, key=lambda x: x[0])[0])
        
        tmp_points[y_value] = definitly_not_beacon_points
    
    res = np.zeros((max_coord_value + 1, max_x - min_x + 1))
    for y_value, points in tmp_points.items():
        for point in points:
            res[y_value, point[0] - min_x] = 1

    candidates = [(np_point[1] + min_x, np_point[0]) for np_point in np.argwhere(res == 0) \
        if np_point[1] + min_x > 0]
    return candidates[-1]


if __name__ == "__main__":
    # print(f"Part 1 result : {part1()}")
    print(f"Part 2 result : {part2()}")
