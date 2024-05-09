# 22. closest_pair_dist() 알고리즘을 O(n log2 n)으로 개선하라. 이를 위해, strip_closest()에서 정렬 문장을 제거해야 하고, closest_pair_dist()에서 병합 정렬의 병합 기법(알고리즘 5.2)을 사용해야 할 것이다.

import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair_dist(points):
    n = len(points)
    if n <= 3:
        return min(dist(points[i], points[j]) for i in range(n) for j in range(i + 1, n))

    points.sort(key=lambda x: x[0])

    mid = n // 2
    left_dist = closest_pair_dist(points[:mid])
    right_dist = closest_pair_dist(points[mid:])

    min_dist = min(left_dist, right_dist)

    strip = [p for p in points if abs(p[0] - points[mid][0]) < min_dist]
    strip.sort(key=lambda x: x[1])
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            min_dist = min(min_dist, dist(strip[i], strip[j]))

    return min_dist

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

print("가장 가까운 두 점 사이의 거리:", closest_pair_dist(points))