# CubeSpace EOS ADCS Postprocessing Visualizer

Python Tool to easily get visual results from CubeSpace EOS ADCS testing results. 

## Usage 

Bring the Microsoft Excel spreadsheet into the root of the repo, and simply call 

```Python
python3 process.py <YOUR_EXCEL_SHEET_NAME>
```

Then you can find your resulting graphs inside the `results/` folder which includes deviations from the Satellite ADCS system and the values from CubeSpace EOS for Roll, Pitch, and Yaw values. They will be contained in a folder with the timestamp of when you started the execution. 