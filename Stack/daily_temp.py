'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

def dailyTemperature(temperatures):
    res = [0]*len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]:
            tmp, stack_i = stack.pop()
            res[stack_i] = (i - stack_i)
        stack.append([temperatures[i],i])
    return res

print(dailyTemperature([73,74,75,71,69,72,76,73]))