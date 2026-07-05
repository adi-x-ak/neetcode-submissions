class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []


        for i in range(len(temperatures)):

            today_temp = temperatures[i]

            while stack and today_temp > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result
        

            