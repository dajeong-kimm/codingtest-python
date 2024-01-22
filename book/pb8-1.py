from ast import List

def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) -1 

    while(left<right):
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if(left_max<=right_max):
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume    