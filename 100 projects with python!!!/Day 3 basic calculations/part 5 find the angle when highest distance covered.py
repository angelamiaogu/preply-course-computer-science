# A ball is thrown with the angle of theta
# find the angle at which i will have highest distance
# viloctiy is 10 m/s and gradity is 9.8 m/s**""
import numpy as np
#sorry

v = 10
g = 9.8
# 20 mintues continue
for angle in range(0,90):
    theta = np.radians(angle)
    D = v**2 *  np.sin( 2 * theta) /g
    print(angle,D)