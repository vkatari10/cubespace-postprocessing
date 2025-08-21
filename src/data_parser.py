"""
Source containing logic to parse data input from the CLI

Author: Vikas Katari
Date: 08/18/2025
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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


def compare_cols(df: pd.DataFrame) -> pd.DataFrame:
    """Compares columns 1->4; 2->5, 3->6 comparing MOCI results to EOS estimates"""
    new_cols = ['Roll_Difference', 'Pitch_Difference', 'Yaw_Difference']
    for i in range(1, 4):
        diff = df.iloc[:, i] - df.iloc[:, i + 3]

        df[new_cols[i - 1]] = diff

    return df


def create_plot(df: pd.DataFrame) -> None:
    """
    Generates a plot of the results

    Note: the folder paths assume they are being called from the root
    of the repo, not from where this file is located 

    i.e. results/ is the valid path, NOT ../results
    """

    curr_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    os.makedirs(f"results/{curr_time}", exist_ok=True)
    
    X = df.index

    Y_labels = ['Roll', 'Pitch', 'Yaw']

    for col in range(10, 13): # first col added at index 10
        plt.figure()
        plt.xlabel("Time Since Start")
        plt.title(f"Difference between MOCI and EOS ADCS {Y_labels[col - 10]} Values")
        plt.ylabel(f"{Y_labels[col - 10]} Difference (Euler Angle)")
        Y = df.iloc[:, col]
        plt.plot(X, Y)


        plt.savefig(f"results/{curr_time}/{curr_time}_{Y_labels[col - 10]}_graph.png")

        plt.close()