class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for i in range(len(position)): 
            time = (target-position[i])/speed[i]
            cars.append((position[i],time))

        cars.sort(reverse=True)

        fleets = 0
        slowest_time_ahead = 0

        for pos, time in cars:
            if time> slowest_time_ahead:
                fleets +=1
                slowest_time_ahead = time

        return fleets

        