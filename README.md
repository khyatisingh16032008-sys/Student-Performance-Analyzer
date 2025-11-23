# Student-Performance-Analyzer
Designed to help classrooms improve learning outcomes, this analyzer highlights weak areas, attendance issues, and study patterns, making academic data easy to understand and act upon.
The Student Performance Analyzer is a Python-based desktop application designed to analyze and predict students' academic performance using real data. The software provides an interactive graphical user interface built with Tkinter, allowing users to load student information from a CSV file and view it in an organized table format. It also includes a dashboard that automatically generates multiple visual charts using Matplotlib, such as subject-wise average scores, attendance versus performance, study hours correlation, and class test score impact. These visual insights help users easily identify performance trends and areas that need improvement. Additionally, the application features a prediction system that estimates the student’s expected final score based on learning factors like attendance, study time, current subject scores, and previous academic results. It also displays pass/fail status and offers helpful alerts for low performance or attendance issues. With the power of Pandas and NumPy for data handling and calculation, this tool acts as a smart assistant for teachers and students to monitor progress, make better decisions, and improve academic outcomes effectively.

**Features:-**
1. Import student data from a CSV file.
2. Display data in a tabular format.
3. Dashboard with charts:
  a. Subject-wise average performance.
  b. Attendance vs Score scatter plot.
  c. Study hours vs Score scatter plot.
  d. Class test score vs Final Score.
4. Predict expected final performance.
5. Pass/Fail status and improvement alerts.

**Tech Stack Used:-**
Python – Core programming language.
Tkinter – GUI for file selection dialogs.
Pandas – Data loading & processing (CSV handling).
NumPy – Numeric operations.
Matplotlib – Data visualization (Scatter Plot).

**Project File Structuce**
**Student-Performance-Analyzer:-**
│
├── main.py               # Main application code (Tkinter GUI + analysis + plots)
├── requirements.txt      # List of dependencies (pandas, numpy, matplotlib)
├── README.md             # Project documentation
│
├── data/                 # Folder containing CSV files for analysis
│   ├── students.csv 
│
├── assets/ (optional)    # Screenshots, images, or icons for README/GitHub
│
└── venv/ (optional)      # Virtual environment (ignored in .gitignore if using GitHub)

**How to Run the Application:-**
Follow these simple steps to run the CSV Scatter Plot Generator on your system:
1. Install Python
   Make sure Python (version 3.8 or above) is installed on your computer.
   You can download it from the official Python website.
2.Install Required Libraries
   Open Command Prompt / Terminal and run the below command:
   pip install pandas numpy matplotlib
3. Download or Copy the Project Files
   Save the provided Python script (scatter_plot_app.py) in a folder of your choice.
4. Run the Application
   Open Command Prompt / Terminal in the folder where the script is stored.
   Run the command:
   python scatter_plot_app.py
5. Upload Your CSV File
   A file explorer window will open.
   Select a valid .csv file that contains at least two numeric columns.
6. View Scatter Plot
   The application will automatically display a scatter plot graph based on selected columns from your CSV.
7. Close the Plot
   Close the plotted window after reviewing the result.
   You can rerun the program again to try another CSV file.
   
**Future Improvements:-**
1. Add an interactive UI using Tkinter or PyQt to allow column selection dynamically.
2. Include support for multiple charts like line plots, bar charts, and histograms.
3. Implement real-time data processing for streaming datasets.
4. Add error highlighting with detailed user-friendly messages.
5. Save scatter plots as image files (PNG/JPEG) automatically.
6. Provide data summary and statistics view before plotting.
7. Add color customization and style themes for better visualization.
8. Enable drag-and-drop functionality for uploading files.
9. Support larger datasets using optimized memory handling.
10 Convert the tool into a desktop application (EXE) using PyInstaller.

   
