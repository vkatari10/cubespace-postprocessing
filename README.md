# CubeSpace EOS ADCS Test Postprocessing

Python Tool to easily postprocess data from CubeSpace EOS ADCS testing results. 

## Usage 

Bring the Microsoft Excel spreadsheet into the root of the repo, and simply call 

```
python3 process.py <YOUR_EXCEL_SHEET_NAME>
```

Resulting plots will be stored in the `results/` folder with a timestamp of when the test was ran. Contained inside each of these folders are the visual graphs for the Roll, Pitch, and Yaw values from the satelite against the physics engine values.  

# Setup

1. Ensure you have the latest Python installation locally on your computer
2. Clone this repo 
3. Create the virtual environment `python3 -m venv .venv`
4. Download required dependencies `pip install -r requirements.txt`

# Author
Vikas Katari
