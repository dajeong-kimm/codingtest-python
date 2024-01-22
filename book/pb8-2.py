from ast import List


def trap(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while(stack and height[i]>height[stack[-1]]):
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] -1
            water = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * water
        stack.append(i)
    return volume