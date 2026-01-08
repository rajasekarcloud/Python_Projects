# A strobogrammatic number looks the same when rotated 180 degrees (upside down).
# To determine if a number is strobogrammatic:
# 808 -> 808
# 11 - 11
# 69 -> 69
# 96 -> 96

def is_strobogrammatic(num):
    left = 0
    right = len(num)-1
    # Valid pair of numbers for is_strobogrammatic when rotated 180 degress
    rotate = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    while left <= right:
        if num[left] not in rotate:
            return False
        if rotate[num[left]] != num[right]:
            return  False
        left +=1
        right -=1
    return True


print(is_strobogrammatic('916'))
