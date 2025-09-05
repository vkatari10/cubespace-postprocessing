"""
This file contains numerical methods to convert between 
Euler angles and quaternions 

Author: Vikas Katari
Date: 09/05/2025
"""
from scipy.spatial.transform import Rotation as R   
from typing import List

def euler_to_quaternion(roll: float, pitch: float, yaw: float) -> List[float]:
    """Returns x, y, z, w as a list of floats given Euler angle roll, pitch, and yaw"""
    r = R.from_euler('xyz', [roll, pitch, yaw])
    return r.as_quat()

if __name__ == "__main__": # test

    roll = 0.1   # rotation around x-axis
    pitch = 0.2  # rotation around y-axis
    yaw = 0.3    # rotation around z-axis

    qx, qy, qz, qw = euler_to_quaternion(roll, pitch, yaw)
    
    
