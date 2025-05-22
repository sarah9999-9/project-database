import sqlite3
import os
import tkinter as tk
from tkinter import ttk, messagebox

# -------- Database path --------
db_path = os.path.join(os.path.expanduser("~"), "medical_lab.db")

# -------- Database Setup --------
def create_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Laboratorian (
        Laboratorian_ID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number TEXT,
        address TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Patient (
        Patient_ID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number TEXT,
        address TEXT,
        birth_date TEXT,
        job TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Component (
        Component_ID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        available_quantity INTEGER NOT NULL,
        minimum_quantity INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Medical_Test (
        Test_ID INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Test_Result (
        Result_ID INTEGER PRIMARY KEY,
        Test_ID INTEGER,
        date TEXT NOT NULL,
        Patient_ID INTEGER,
        Laboratorian_ID INTEGER,
        result TEXT,
        FOREIGN KEY(Test_ID) REFERENCES Medical_Test(Test_ID),
        FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID),
        FOREIGN KEY(Laboratorian_ID) REFERENCES Laboratorian(Laboratorian_ID)
    )
    ''')

    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    laboratorians = [
        (1, 'Ahmed Ali', '0123456789', 'Cairo'),
        (2, 'Mona Hassan', '0112233445', 'Alexandria'),
        (3, 'Omar Saeed', '0156789456', 'Giza'),
        (4, 'Sara Khaled', '0109988776', 'Cairo'),
        (5, 'Ali Mahmoud', '0123344556', 'Tanta'),
        (6, 'Hana Youssef', '0115566778', 'Mansoura'),
        (7, 'Khaled Farag', '0101234567', 'Cairo'),
        (8, 'Nadia Ibrahim', '0129876543', 'Alexandria'),
        (9, 'Tamer Adel', '0111112222', 'Cairo'),
        (10, 'Dina Samir', '0122223333', 'Giza')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Laboratorian VALUES (?,?,?,?)', laboratorians)

    patients = [
        (1001, 'Mohamed Salah', '0111111111', 'Cairo', '1985-07-15', 'Engineer'),
        (1002, 'Fatma Ahmed', '0122222222', 'Alexandria', '1990-03-20', 'Teacher'),
        (1003, 'Hany Mahmoud', '0103333333', 'Giza', '1975-11-05', 'Doctor'),
        (1004, 'Laila Hassan', '0114444444', 'Cairo', '1988-06-30', 'Nurse'),
        (1005, 'Ali Mohamed', '0125555555', 'Tanta', '1992-01-10', 'Student'),
        (1006, 'Sara Khaled', '0106666666', 'Mansoura', '1980-12-25', 'Lawyer'),
        (1007, 'Ahmed Youssef', '0117777777', 'Cairo', '1987-09-15', 'Accountant'),
        (1008, 'Nora Sami', '0128888888', 'Alexandria', '1995-05-22', 'Designer'),
        (1009, 'Tarek Adel', '0109999999', 'Giza', '1978-08-18', 'Architect'),
        (1010, 'Dina Samir', '0110000000', 'Cairo', '1993-04-02', 'Pharmacist')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Patient VALUES (?,?,?,?,?,?)', patients)

    components = [
        (1, 'Blood Sample Tube', 50, 10),
        (2, 'Glucose Reagent', 30, 15),
        (3, 'Hemoglobin Reagent', 40, 20),
        (4, 'Microscope Slides', 60, 25),
        (5, 'Urine Sample Cup', 45, 15),
        (6, 'Chemical Reagent A', 20, 10),
        (7, 'Chemical Reagent B', 15, 10),
        (8, 'Test Tubes', 35, 10),
        (9, 'Alcohol Swabs', 80, 30),
        (10, 'Gloves', 100, 50)
    ]
    cursor.executemany('INSERT OR IGNORE INTO Component VALUES (?,?,?,?)', components)

    medical_tests = [
        (101, 'CBC', 150.00),
        (102, 'Blood Sugar', 120.00),
        (103, 'Urinalysis', 130.00),
        (104, 'Liver Function Test', 200.00),
        (105, 'Kidney Function Test', 190.00),
        (106, 'Lipid Profile', 180.00),
        (107, 'Thyroid Test', 170.00),
        (108, 'Vitamin D Test', 160.00),
        (109, 'COVID-19 PCR', 300.00),
        (110, 'Electrolyte Panel', 140.00)
    ]
    cursor.executemany('INSERT OR IGNORE INTO Medical_Test VALUES (?,?,?)', medical_tests)

    test_results = [
        (1, 101, '2024-04-01', 1001, 1, 'Normal CBC results'),
        (2, 102, '2024-04-03', 1002, 2, 'High blood sugar level'),
        (3, 103, '2024-03-30', 1003, 3, 'Normal urine analysis'),
        (4, 104, '2024-04-05', 1004, 4, 'Elevated liver enzymes'),
        (5, 105, '2024-04-07', 1005, 5, 'Normal kidney function'),
        (6, 106, '2024-04-09', 1006, 6, 'High cholesterol'),
        (7, 107, '2024-04-11', 1007, 7, 'Normal thyroid levels'),
        (8, 108, '2024-04-13', 1008, 8, 'Vitamin D deficiency'),
        (9, 109, '2024-04-15', 1009, 9, 'Negative COVID-19 PCR'),
        (10, 110, '2024-04-17', 1010, 10, 'Normal electrolyte levels')
    ]
    cursor.executemany('INSERT OR IGNORE INTO Test_Result VALUES (?,?,?,?,?,?)', test_results)

    conn.commit()
    conn.close()

class MedicalLabApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Laboratory Management System")
        self.geometry("1000x650")

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self)
        self.tabs = {}

        tab_names = ['Laboratorians', 'Patients', 'Components', 'Medical Tests', 'Test Results']
        for name in tab_names:
            frame = ttk.Frame(tab_control)
            tab_control.add(frame, text=name)
            self.tabs[name] = frame

        tab_control.pack(expand=1, fill='both')

        self.setup_laboratorian_tab()
        self.setup_patient_tab()
        self.setup_component_tab()
        self.setup_medical_test_tab()
        self.setup_test_result_tab()

    # Laboratorian Tab
    def setup_laboratorian_tab(self):
        frame = self.tabs['Laboratorians']
        columns = ('ID', 'Name', 'Phone', 'Address')
        self.tree_laboratorian = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_laboratorian.heading(col, text=col)
            self.tree_laboratorian.column(col, width=150)
        self.tree_laboratorian.pack(fill='both', expand=True)
        self.load_laboratorians()

        form = ttk.Frame(frame)
        form.pack(pady=10)

        ttk.Label(form, text='ID').grid(row=0, column=0, padx=5, pady=5)
        self.lab_id = ttk.Entry(form)
        self.lab_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text='Name').grid(row=1, column=0, padx=5, pady=5)
        self.lab_name = ttk.Entry(form)
        self.lab_name.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text='Phone').grid(row=2, column=0, padx=5, pady=5)
        self.lab_phone = ttk.Entry(form)
        self.lab_phone.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text='Address').grid(row=3, column=0, padx=5, pady=5)
        self.lab_address = ttk.Entry(form)
        self.lab_address.grid(row=3, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack()

        ttk.Button(btn_frame, text='Add', command=self.add_laboratorian).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text='Update', command=self.update_laboratorian).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text='Delete', command=self.delete_laboratorian).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text='Refresh', command=self.load_laboratorians).grid(row=0, column=3, padx=5, pady=5)

        self.tree_laboratorian.bind('<<TreeviewSelect>>', self.select_laboratorian)

    def load_laboratorians(self):
        for i in self.tree_laboratorian.get_children():
            self.tree_laboratorian.delete(i)
        self.cursor.execute("SELECT * FROM Laboratorian")
        for row in self.cursor.fetchall():
            self.tree_laboratorian.insert('', 'end', values=row)

    def add_laboratorian(self):
        try:
            id_ = int(self.lab_id.get())
            name = self.lab_name.get()
            phone = self.lab_phone.get()
            address = self.lab_address.get()
            self.cursor.execute("INSERT INTO Laboratorian VALUES (?, ?, ?, ?)", (id_, name, phone, address))
            self.conn.commit()
            self.load_laboratorians()
            messagebox.showinfo("Success", "Laboratorian added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_laboratorian(self):
        try:
            id_ = int(self.lab_id.get())
            name = self.lab_name.get()
            phone = self.lab_phone.get()
            address = self.lab_address.get()
            self.cursor.execute("UPDATE Laboratorian SET name=?, phone_number=?, address=? WHERE Laboratorian_ID=?", (name, phone, address, id_))
            self.conn.commit()
            self.load_laboratorians()
            messagebox.showinfo("Success", "Laboratorian updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_laboratorian(self):
        try:
            id_ = int(self.lab_id.get())
            self.cursor.execute("DELETE FROM Laboratorian WHERE Laboratorian_ID=?", (id_,))
            self.conn.commit()
            self.load_laboratorians()
            messagebox.showinfo("Success", "Laboratorian deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_laboratorian(self, event):
        selected = self.tree_laboratorian.selection()
        if selected:
            values = self.tree_laboratorian.item(selected[0])['values']
            self.lab_id.delete(0, tk.END)
            self.lab_id.insert(0, values[0])
            self.lab_name.delete(0, tk.END)
            self.lab_name.insert(0, values[1])
            self.lab_phone.delete(0, tk.END)
            self.lab_phone.insert(0, values[2])
            self.lab_address.delete(0, tk.END)
            self.lab_address.insert(0, values[3])

    # Patient Tab
    def setup_patient_tab(self):
        frame = self.tabs['Patients']
        columns = ('ID', 'Name', 'Phone', 'Address', 'Birth Date', 'Job')
        self.tree_patient = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_patient.heading(col, text=col)
            self.tree_patient.column(col, width=120)
        self.tree_patient.pack(fill='both', expand=True)
        self.load_patients()

        form = ttk.Frame(frame)
        form.pack(pady=10)

        ttk.Label(form, text='ID').grid(row=0, column=0, padx=5, pady=5)
        self.patient_id = ttk.Entry(form)
        self.patient_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text='Name').grid(row=1, column=0, padx=5, pady=5)
        self.patient_name = ttk.Entry(form)
        self.patient_name.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text='Phone').grid(row=2, column=0, padx=5, pady=5)
        self.patient_phone = ttk.Entry(form)
        self.patient_phone.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text='Address').grid(row=3, column=0, padx=5, pady=5)
        self.patient_address = ttk.Entry(form)
        self.patient_address.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(form, text='Birth Date (YYYY-MM-DD)').grid(row=4, column=0, padx=5, pady=5)
        self.patient_birthdate = ttk.Entry(form)
        self.patient_birthdate.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(form, text='Job').grid(row=5, column=0, padx=5, pady=5)
        self.patient_job = ttk.Entry(form)
        self.patient_job.grid(row=5, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack()

        ttk.Button(btn_frame, text='Add', command=self.add_patient).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text='Update', command=self.update_patient).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text='Delete', command=self.delete_patient).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text='Refresh', command=self.load_patients).grid(row=0, column=3, padx=5, pady=5)

        self.tree_patient.bind('<<TreeviewSelect>>', self.select_patient)

    def load_patients(self):
        for i in self.tree_patient.get_children():
            self.tree_patient.delete(i)
        self.cursor.execute("SELECT * FROM Patient")
        for row in self.cursor.fetchall():
            self.tree_patient.insert('', 'end', values=row)

    def add_patient(self):
        try:
            id_ = int(self.patient_id.get())
            name = self.patient_name.get()
            phone = self.patient_phone.get()
            address = self.patient_address.get()
            birthdate = self.patient_birthdate.get()
            job = self.patient_job.get()
            self.cursor.execute("INSERT INTO Patient VALUES (?, ?, ?, ?, ?, ?)", (id_, name, phone, address, birthdate, job))
            self.conn.commit()
            self.load_patients()
            messagebox.showinfo("Success", "Patient added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_patient(self):
        try:
            id_ = int(self.patient_id.get())
            name = self.patient_name.get()
            phone = self.patient_phone.get()
            address = self.patient_address.get()
            birthdate = self.patient_birthdate.get()
            job = self.patient_job.get()
            self.cursor.execute("""
                UPDATE Patient SET name=?, phone_number=?, address=?, birth_date=?, job=?
                WHERE Patient_ID=?
            """, (name, phone, address, birthdate, job, id_))
            self.conn.commit()
            self.load_patients()
            messagebox.showinfo("Success", "Patient updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_patient(self):
        try:
            id_ = int(self.patient_id.get())
            self.cursor.execute("DELETE FROM Patient WHERE Patient_ID=?", (id_,))
            self.conn.commit()
            self.load_patients()
            messagebox.showinfo("Success", "Patient deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_patient(self, event):
        selected = self.tree_patient.selection()
        if selected:
            values = self.tree_patient.item(selected[0])['values']
            self.patient_id.delete(0, tk.END)
            self.patient_id.insert(0, values[0])
            self.patient_name.delete(0, tk.END)
            self.patient_name.insert(0, values[1])
            self.patient_phone.delete(0, tk.END)
            self.patient_phone.insert(0, values[2])
            self.patient_address.delete(0, tk.END)
            self.patient_address.insert(0, values[3])
            self.patient_birthdate.delete(0, tk.END)
            self.patient_birthdate.insert(0, values[4])
            self.patient_job.delete(0, tk.END)
            self.patient_job.insert(0, values[5])

    # Component Tab
    def setup_component_tab(self):
        frame = self.tabs['Components']
        columns = ('ID', 'Name', 'Available Qty', 'Minimum Qty')
        self.tree_component = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_component.heading(col, text=col)
            self.tree_component.column(col, width=120)
        self.tree_component.pack(fill='both', expand=True)
        self.load_components()

        form = ttk.Frame(frame)
        form.pack(pady=10)

        ttk.Label(form, text='ID').grid(row=0, column=0, padx=5, pady=5)
        self.comp_id = ttk.Entry(form)
        self.comp_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text='Name').grid(row=1, column=0, padx=5, pady=5)
        self.comp_name = ttk.Entry(form)
        self.comp_name.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text='Available Quantity').grid(row=2, column=0, padx=5, pady=5)
        self.comp_avail = ttk.Entry(form)
        self.comp_avail.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text='Minimum Quantity').grid(row=3, column=0, padx=5, pady=5)
        self.comp_min = ttk.Entry(form)
        self.comp_min.grid(row=3, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack()

        ttk.Button(btn_frame, text='Add', command=self.add_component).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text='Update', command=self.update_component).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text='Delete', command=self.delete_component).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text='Refresh', command=self.load_components).grid(row=0, column=3, padx=5, pady=5)

        self.tree_component.bind('<<TreeviewSelect>>', self.select_component)

    def load_components(self):
        for i in self.tree_component.get_children():
            self.tree_component.delete(i)
        self.cursor.execute("SELECT * FROM Component")
        for row in self.cursor.fetchall():
            self.tree_component.insert('', 'end', values=row)

    def add_component(self):
        try:
            id_ = int(self.comp_id.get())
            name = self.comp_name.get()
            avail = int(self.comp_avail.get())
            minimum = int(self.comp_min.get())
            self.cursor.execute("INSERT INTO Component VALUES (?, ?, ?, ?)", (id_, name, avail, minimum))
            self.conn.commit()
            self.load_components()
            messagebox.showinfo("Success", "Component added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_component(self):
        try:
            id_ = int(self.comp_id.get())
            name = self.comp_name.get()
            avail = int(self.comp_avail.get())
            minimum = int(self.comp_min.get())
            self.cursor.execute("""
                UPDATE Component SET name=?, available_quantity=?, minimum_quantity=?
                WHERE Component_ID=?
            """, (name, avail, minimum, id_))
            self.conn.commit()
            self.load_components()
            messagebox.showinfo("Success", "Component updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_component(self):
        try:
            id_ = int(self.comp_id.get())
            self.cursor.execute("DELETE FROM Component WHERE Component_ID=?", (id_,))
            self.conn.commit()
            self.load_components()
            messagebox.showinfo("Success", "Component deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_component(self, event):
        selected = self.tree_component.selection()
        if selected:
            values = self.tree_component.item(selected[0])['values']
            self.comp_id.delete(0, tk.END)
            self.comp_id.insert(0, values[0])
            self.comp_name.delete(0, tk.END)
            self.comp_name.insert(0, values[1])
            self.comp_avail.delete(0, tk.END)
            self.comp_avail.insert(0, values[2])
            self.comp_min.delete(0, tk.END)
            self.comp_min.insert(0, values[3])

    # Medical Test Tab
    def setup_medical_test_tab(self):
        frame = self.tabs['Medical Tests']
        columns = ('ID', 'Name', 'Price')
        self.tree_medtest = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_medtest.heading(col, text=col)
            self.tree_medtest.column(col, width=150)
        self.tree_medtest.pack(fill='both', expand=True)
        self.load_medtests()

        form = ttk.Frame(frame)
        form.pack(pady=10)

        ttk.Label(form, text='ID').grid(row=0, column=0, padx=5, pady=5)
        self.medtest_id = ttk.Entry(form)
        self.medtest_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text='Name').grid(row=1, column=0, padx=5, pady=5)
        self.medtest_name = ttk.Entry(form)
        self.medtest_name.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text='Price').grid(row=2, column=0, padx=5, pady=5)
        self.medtest_price = ttk.Entry(form)
        self.medtest_price.grid(row=2, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack()

        ttk.Button(btn_frame, text='Add', command=self.add_medtest).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text='Update', command=self.update_medtest).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text='Delete', command=self.delete_medtest).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text='Refresh', command=self.load_medtests).grid(row=0, column=3, padx=5, pady=5)

        self.tree_medtest.bind('<<TreeviewSelect>>', self.select_medtest)

    def load_medtests(self):
        for i in self.tree_medtest.get_children():
            self.tree_medtest.delete(i)
        self.cursor.execute("SELECT * FROM Medical_Test")
        for row in self.cursor.fetchall():
            self.tree_medtest.insert('', 'end', values=row)

    def add_medtest(self):
        try:
            id_ = int(self.medtest_id.get())
            name = self.medtest_name.get()
            price = float(self.medtest_price.get())
            self.cursor.execute("INSERT INTO Medical_Test VALUES (?, ?, ?)", (id_, name, price))
            self.conn.commit()
            self.load_medtests()
            messagebox.showinfo("Success", "Medical Test added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_medtest(self):
        try:
            id_ = int(self.medtest_id.get())
            name = self.medtest_name.get()
            price = float(self.medtest_price.get())
            self.cursor.execute("""
                UPDATE Medical_Test SET name=?, price=?
                WHERE Test_ID=?
            """, (name, price, id_))
            self.conn.commit()
            self.load_medtests()
            messagebox.showinfo("Success", "Medical Test updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_medtest(self):
        try:
            id_ = int(self.medtest_id.get())
            self.cursor.execute("DELETE FROM Medical_Test WHERE Test_ID=?", (id_,))
            self.conn.commit()
            self.load_medtests()
            messagebox.showinfo("Success", "Medical Test deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_medtest(self, event):
        selected = self.tree_medtest.selection()
        if selected:
            values = self.tree_medtest.item(selected[0])['values']
            self.medtest_id.delete(0, tk.END)
            self.medtest_id.insert(0, values[0])
            self.medtest_name.delete(0, tk.END)
            self.medtest_name.insert(0, values[1])
            self.medtest_price.delete(0, tk.END)
            self.medtest_price.insert(0, values[2])

    # Test Result Tab
    def setup_test_result_tab(self):
        frame = self.tabs['Test Results']
        columns = ('ID', 'Test ID', 'Date', 'Patient ID', 'Laboratorian ID', 'Result')
        self.tree_testresult = ttk.Treeview(frame, columns=columns, show='headings')
        for col in columns:
            self.tree_testresult.heading(col, text=col)
            self.tree_testresult.column(col, width=120)
        self.tree_testresult.pack(fill='both', expand=True)
        self.load_testresults()

        form = ttk.Frame(frame)
        form.pack(pady=10)

        ttk.Label(form, text='ID').grid(row=0, column=0, padx=5, pady=5)
        self.testresult_id = ttk.Entry(form)
        self.testresult_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form, text='Test ID').grid(row=1, column=0, padx=5, pady=5)
        self.testresult_testid = ttk.Entry(form)
        self.testresult_testid.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form, text='Date (YYYY-MM-DD)').grid(row=2, column=0, padx=5, pady=5)
        self.testresult_date = ttk.Entry(form)
        self.testresult_date.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form, text='Patient ID').grid(row=3, column=0, padx=5, pady=5)
        self.testresult_patientid = ttk.Entry(form)
        self.testresult_patientid.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(form, text='Laboratorian ID').grid(row=4, column=0, padx=5, pady=5)
        self.testresult_laboratorianid = ttk.Entry(form)
        self.testresult_laboratorianid.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(form, text='Result').grid(row=5, column=0, padx=5, pady=5)
        self.testresult_result = ttk.Entry(form)
        self.testresult_result.grid(row=5, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack()

        ttk.Button(btn_frame, text='Add', command=self.add_testresult).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text='Update', command=self.update_testresult).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text='Delete', command=self.delete_testresult).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(btn_frame, text='Refresh', command=self.load_testresults).grid(row=0, column=3, padx=5, pady=5)

        self.tree_testresult.bind('<<TreeviewSelect>>', self.select_testresult)

    def load_testresults(self):
        for i in self.tree_testresult.get_children():
            self.tree_testresult.delete(i)
        self.cursor.execute("SELECT * FROM Test_Result")
        for row in self.cursor.fetchall():
            self.tree_testresult.insert('', 'end', values=row)

    def add_testresult(self):
        try:
            id_ = int(self.testresult_id.get())
            test_id = int(self.testresult_testid.get())
            date = self.testresult_date.get()
            patient_id = int(self.testresult_patientid.get())
            laboratorian_id = int(self.testresult_laboratorianid.get())
            result = self.testresult_result.get()
            self.cursor.execute("INSERT INTO Test_Result VALUES (?, ?, ?, ?, ?, ?)", (id_, test_id, date, patient_id, laboratorian_id, result))
            self.conn.commit()
            self.load_testresults()
            messagebox.showinfo("Success", "Test Result added successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_testresult(self):
        try:
            id_ = int(self.testresult_id.get())
            test_id = int(self.testresult_testid.get())
            date = self.testresult_date.get()
            patient_id = int(self.testresult_patientid.get())
            laboratorian_id = int(self.testresult_laboratorianid.get())
            result = self.testresult_result.get()
            self.cursor.execute("""
                UPDATE Test_Result SET Test_ID=?, date=?, Patient_ID=?, Laboratorian_ID=?, result=?
                WHERE Result_ID=?
            """, (test_id, date, patient_id, laboratorian_id, result, id_))
            self.conn.commit()
            self.load_testresults()
            messagebox.showinfo("Success", "Test Result updated successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_testresult(self):
        try:
            id_ = int(self.testresult_id.get())
            self.cursor.execute("DELETE FROM Test_Result WHERE Result_ID=?", (id_,))
            self.conn.commit()
            self.load_testresults()
            messagebox.showinfo("Success", "Test Result deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def select_testresult(self, event):
        selected = self.tree_testresult.selection()
        if selected:
            values = self.tree_testresult.item(selected[0])['values']
            self.testresult_id.delete(0, tk.END)
            self.testresult_id.insert(0, values[0])
            self.testresult_testid.delete(0, tk.END)
            self.testresult_testid.insert(0, values[1])
            self.testresult_date.delete(0, tk.END)
            self.testresult_date.insert(0, values[2])
            self.testresult_patientid.delete(0, tk.END)
            self.testresult_patientid.insert(0, values[3])
            self.testresult_laboratorianid.delete(0, tk.END)
            self.testresult_laboratorianid.insert(0, values[4])
            self.testresult_result.delete(0, tk.END)
            self.testresult_result.insert(0, values[5])

def main():
    create_db()
    insert_sample_data()
    app = MedicalLabApp()
    app.mainloop()

if __name__ == "__main__":
    main()
