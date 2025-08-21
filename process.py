"""
CLI Script to process input CSVs from CubeSpace EOS
Simulation Results

Author: Vikas Katari
Date: 08/18/2025
"""
import sys
import src.data_parser as dp


def main() -> None:
    args = sys.argv
    df = dp.excel_to_df(args[1])
    df = dp.compare_cols(df)
    dp.create_plot(df)

if __name__ == "__main__":
    main()
