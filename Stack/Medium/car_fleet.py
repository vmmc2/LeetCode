class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()
        
        stack = []
        numFleets = 0

        current = n - 1

        while current >= 0:
            if len(stack) == 0:
                stack.append(cars[current])
            else: # Need to check whether the current car will be able to catch up to the next one
                p1, s1 = cars[current][0], cars[current][1]
                p2, s2 = stack[-1][0], stack[-1][1]
                if s1 > s2:
                    t = (p2 - p1)/(s1 - s2)
                    if t < 0:
                        stack.append(cars[current])
                        current -= 1
                        continue
                    sMeet = p1 + s1 * t
                    if 0 <= sMeet and sMeet <= target: # The current car will make part of the fleet.
                        previous = stack.pop()
                        stack.append(cars[current] if cars[current][1] <= previous[1] else previous)
                    else: # The current car will start another fleet.
                        stack.append(cars[current])
                elif s2 > s1:
                    t = (p1 - p2)/(s2 - s1)
                    if t < 0:
                        stack.append(cars[current])
                        current -= 1
                        continue                      
                    sMeet = p1 + s1 * t
                    if 0 <= sMeet and sMeet <= target: # The current car will make part of the fleet.
                        previous = stack.pop()
                        stack.append(cars[current] if cars[current][1] <= previous[1] else previous)
                    else: # The current car will start another fleet.
                        stack.append(cars[current])
                else: # The current car will never catch up to the next one. Thus, creates another fleet
                    stack.append(cars[current])
            current -= 1


        numFleets = len(stack)

        return numFleets
