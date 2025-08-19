"""
Source containing logic to parse data input from the CLI

Author: Vikas Katari
Date: 08/18/2025
"""
import pandas as pd

"""
DFs will be of size [n: 10] where we introduce a new
index column and keep the time since start column on
index 1

The Columns are all floats except for the first (int)

index | col name
0 Time Since Start
1 MOCI.Satellite Kinematic State.Euler Angles.Roll
2 MOCI.Satellite Kinematic State.Euler Angles.Pitch
3 MOCI.Satellite Kinematic State.Euler Angles.Yaw
4 CubeACP.Estimated Kinematic State.Euler Angles.Roll
5 CubeACP.Estimated Kinematic State.Euler Angles.Pitch
6 CubeACP.Estimated Kinematic State.Euler Angles.Yaw
7 CubeACP.Estimated Roll Error
8 CubeACP.Estimated Pitch Error
9 CubeACP.Estimated Yaw Error

With all the DFs do not use .loc(), just use .iloc() only
"""

def excel_to_df(file: str) -> pd.DataFrame:
    """Excel -> Pandas DF"""
    df = pd.read_excel(file) 
    return df
