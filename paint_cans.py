import math
def paint_calc(height, width, cover):
    return math.ceil((height*width)/cover)
test_h=int(input("Enter the height of the wall: "))
test_w=int(input("Enter the width of the wall: "))
coverage=5
result=paint_calc(height=test_h,width=test_w,cover=coverage)
print(f"You'll need {result} cans of paint.")