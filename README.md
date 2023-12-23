For further information, like the background of this dataset, dataset characteristics, file structures, and more, you can check out the Readme file. So in here, I won't explain it any further.

1. File Structures
.
├── dashboard
│   ├── dashboard.py
│   └── all_data.csv
├── data
│   ├── day.csv
|   └── hour.csv
├── README.md
├── notebook.ipynb
└── requirements.txt
2. Project work cycle
Data Wrangling:
Gathering data
Assessing data
Cleaning data
Exploratory Data Analysis:
Defined business questions for data exploration
Create Data exploration
Data Visualization:
Create Data Visualization that answer business questions
Dashboard:
Set up the DataFrame which will be used
Make filter components on the dashboard
Complete the dashboard with various data visualizations

3. Getting Started
notebook.ipynb
Download this project.
Open your favorite IDE like Jupyter Notebook or Google Colaboratory (but in here I will use Jupyter notebook).
Create a New Notebook.
Upload and select the file with .ipynb extension.
Connect to hosted runtime.
Lastly, run the code cells.
dashboard/dashboard.py
Download this project.
Install the Streamlit in your terminal or command prompt using pip install streamlit. Install another libraries like pandas, numpy, scipy, matplotlib, and seaborn if you haven't.
Please note, don't move the csv file because it acts a data source. keep it in one folder as dashboard.py
Open your VSCode and run the file by clicking the terminal and write it streamlit run dashboard.py.
