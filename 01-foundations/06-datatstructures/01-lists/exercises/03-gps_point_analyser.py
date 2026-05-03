from typing import List, TypeAlias
import math


# Types
Point: TypeAlias = List[float]

# GPS Points
points: list[Point] = [
    [325456.12, 541278.55],
    [325500.44, 541300.90],
    [325544.76, 541323.25],
    [325589.08, 541345.60],
    [325633.40, 541367.95],
    [325677.72, 541390.30],
    [325722.04, 541412.65],
    [325766.36, 541435.00],
    [325810.68, 541457.35],
    [325855.00, 541479.70]
]

# Utils
def formatted_points(points: List[Point]) -> dict[str | Point]:
    return {f"P{i + 1}": point for i, point in enumerate(points)}

def calculate_distance(p1: Point, p2: Point) -> float:
    return round(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2), 3)

# Calculate distances
def calculate_distances(points: List[Point]) -> dict[str | List[dict]]:
    f_points: dict[str | Point] = formatted_points(points)
    return {
        name: {
            other: calculate_distance(coord, f_points[other])
            for other in f_points if other != name
        }
        for name, coord in f_points.items()
    }

def find_nearest_point(points: List[Point]) -> dict[str, tuple[str, float]]:
    distances = calculate_distances(points)
    return {
        point: min(neighbors.items(), key=lambda x: x[1])
        for point, neighbors in distances.items()
    }

def find_farthest_point(points: List[Point]) -> dict[str, tuple[str, float]]:
    distances = calculate_distances(points)
    return {
        point: max(neighbors.items(), key=lambda x: x[1])
        for point, neighbors in distances.items()
    }
