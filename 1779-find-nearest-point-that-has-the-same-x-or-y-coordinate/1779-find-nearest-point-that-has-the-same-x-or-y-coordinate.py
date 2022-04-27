class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        valid_points = []
        
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                valid_points.append([point[0], point[1], i])
                
        min_distance = [sys.maxsize, -1]     
        
        for point in valid_points:
            distance = abs(point[0] - x) + abs(point[1] - y)
            
            if distance < min_distance[0]:
                min_distance[0] = distance                
                min_distance[1] = point[2]
                
        return min_distance[1] 