import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import numpy as np
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DEFAULT_DATA_PATH = os.path.join("data", "students.csv")

class StudentPerformanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Performance Analyzer (Simple)")
        self.geometry("1000x700")
        self.data = None
        self._build_tabs()
        self.load_default_data()

    def _build_tabs(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.tab_data = ttk.Frame(notebook)
        notebook.add(self.tab_data, text="Data")

        self.tab_dashboard = ttk.Frame(notebook)
        notebook.add(self.tab_dashboard, text="Dashboard")

        self.tab_predict = ttk.Frame(notebook)
        notebook.add(self.tab_predict, text="Predict")

        self._build_data_tab()
        self._build_dashboard_tab()
        self._build_predict_tab()

    # ---------------- Data Tab ----------------
    def _build_data_tab(self):
        ttk.Button(self.tab_data, text="Import CSV", command=self.import_csv).pack(pady=5)
        self.tree = ttk.Treeview(self.tab_data, show="headings")
        self.tree.pack(fill="both", expand=True)

    def import_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            self.data = pd.read_csv(path)
            self._populate_tree()

    def load_default_data(self):
        if os.path.exists(DEFAULT_DATA_PATH):
            self.data = pd.read_csv(DEFAULT_DATA_PATH)
            self._populate_tree()

    def _populate_tree(self):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(self.data.columns)
        for col in self.data.columns:
            self.tree.heading(col, text=col)
        for _, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row.values))

    # ---------------- Dashboard Tab ----------------
    def _build_dashboard_tab(self):
        ttk.Button(self.tab_dashboard, text="Show Charts", command=self.draw_dashboard).pack(pady=5)
        self.chart_frame = ttk.Frame(self.tab_dashboard)
        self.chart_frame.pack(fill="both", expand=True)

    def draw_dashboard(self):
        if self.data is None: return
        df = self.data.copy()
        df["final_score"] = df[["math","science","english"]].mean(axis=1)

        fig = Figure(figsize=(10,6))
        ax1 = fig.add_subplot(2,2,1)
        ax2 = fig.add_subplot(2,2,2)
        ax3 = fig.add_subplot(2,2,3)
        ax4 = fig.add_subplot(2,2,4)

        # Subject averages
        subject_means = df[["math","science","english"]].mean()
        ax1.bar(subject_means.index, subject_means.values, color="skyblue")
        ax1.set_title("Subject-wise averages")

        # Attendance vs score
        ax2.scatter(df["attendance_pct"], df["final_score"], color="green")
        ax2.set_title("Attendance vs Score")

        # Study hours vs score
        ax3.scatter(df["study_hours_week"], df["final_score"], color="purple")
        ax3.set_title("Study Hours vs Score")

        # Tests vs score
        ax4.scatter(df["class_tests_avg"], df["final_score"], color="orange")
        ax4.set_title("Class Tests vs Score")

        fig.tight_layout()
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # ---------------- Predict Tab ----------------
    def _build_predict_tab(self):
        form = ttk.Frame(self.tab_predict)
        form.pack(side="left", padx=10, pady=10)

        self.var_attendance = tk.DoubleVar(value=80)
        self.var_study_hours = tk.DoubleVar(value=8)
        self.var_tests_avg = tk.DoubleVar(value=70)
        self.var_prev_avg = tk.DoubleVar(value=68)
        self.var_math = tk.DoubleVar(value=70)
        self.var_science = tk.DoubleVar(value=70)
        self.var_english = tk.DoubleVar(value=70)

        fields = [
            ("Attendance %", self.var_attendance),
            ("Study hours/week", self.var_study_hours),
            ("Class tests avg", self.var_tests_avg),
            ("Previous term avg", self.var_prev_avg),
            ("Math current", self.var_math),
            ("Science current", self.var_science),
            ("English current", self.var_english),
        ]
        for label, var in fields:
            ttk.Label(form, text=label).pack(anchor="w")
            ttk.Entry(form, textvariable=var).pack(fill="x", pady=2)

        ttk.Button(form, text="Predict", command=self.predict_now).pack(pady=10)

        self.lbl_score = ttk.Label(self.tab_predict, text="Expected Final Score: -")
        self.lbl_score.pack(anchor="w", pady=5)
        self.lbl_passfail = ttk.Label(self.tab_predict, text="Pass/Fail Prediction: -")
        self.lbl_passfail.pack(anchor="w", pady=5)
        self.alert_box = tk.Text(self.tab_predict, height=6)
        self.alert_box.pack(fill="both", expand=True, pady=10)

    def predict_now(self):
        score = np.mean([self.var_math.get(), self.var_science.get(), self.var_english.get()])
        # Simple rule: average with attendance and tests
        final_score = (score + self.var_attendance.get()/2 + self.var_tests_avg.get()/2 + self.var_prev_avg.get())/3
        pass_fail = "Pass" if final_score >= 50 else "Fail"

        self.lbl_score.config(text=f"Expected Final Score: {final_score:.1f}")
        self.lbl_passfail.config(text=f"Pass/Fail Prediction: {pass_fail}")

        alerts = []
        if self.var_attendance.get() < 75:
            alerts.append("Low attendance: High risk of failure.")
        if self.var_study_hours.get() < 6:
            alerts.append("Study hours are low. Try +2 hrs/week.")
        if score < 60:
            alerts.append("Weak subject scores. Practice more.")
        self.alert_box.delete("1.0","end")
        self.alert_box.insert("end","\n".join(alerts) if alerts else "No alerts. Keep going!")

if __name__ == "__main__":
    app = StudentPerformanceApp()
    app.mainloop()
