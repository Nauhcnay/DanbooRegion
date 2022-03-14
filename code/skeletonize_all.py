import cv2
import os
from skeletonize import get_skeleton

for _ in range(3377):
    if os.path.exists('./DanbooRegion2020/train/' + str(_) + '.skeleton.png'): continue
    region = cv2.imread('./DanbooRegion2020/train/' + str(_) + '.region.png')
    skeleton = get_skeleton(region)
    cv2.imwrite('./DanbooRegion2020/train/' + str(_) + '.skeleton.png', skeleton)
    print('Writing   ./DanbooRegion2020/train/' + str(_) + '.skeleton.png   ' + str(_ + 1) + '/3377')
