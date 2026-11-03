# 🏥 Hospital Patient Management System

A lightweight, web-based **Hospital Patient Management System** built with **Python**, **Streamlit**, and **Pandas**. Developed as part of **U25CSG05 — Computational Problem Solving Using Python** at the **Department of Artificial Intelligence and Data Science, KPR Institute of Engineering and Technology**.

## 📌 Problem Statement

Managing hospital records manually through paper registers or basic spreadsheets is slow, unreliable, and difficult to scale. Small clinics and hospitals often face missing patient files, scheduling conflicts, and a lack of data analytics.

This application provides an intuitive browser-based interface that enables hospital staff to:
- **Register Patients** with their personal details (`id`, `name`, `age`, `gender`) and diagnosed `disease`.
- **Register Doctors** along with their personal details and medical `specialization`.
- **Book Appointments** by linking patients to doctors on selected dates.
- **View Reports & Analytics** through interactive tables and real-time charts.

## 🛠️ Tech Stack & Modules Used

| Module | Category | Role in Project |
| :--- | :--- | :--- |
| `streamlit` | Third-Party | Builds the interactive web-based graphical interface (menus, inputs, buttons, tables, and bar charts). |
| `pandas` | Third-Party | Reads and writes CSV files, creates `DataFrame` tables for display, and computes summary analytics. |
| `os` | Standard Library | Checks whether CSV files exist (`os.path.exists()`) so column headers are written only once on file creation. |

## 🧩 Architecture & OOP Concepts Demonstrated

### Architectural Layers

| Layer | Components | Responsibility |
| :--- | :--- | :--- |
| **Data Model** | `Person`, `Doctor`, `Patient`, `Appointment` | Defines the structure of all domain entities using Object-Oriented Programming. |
| **Validation** | `InvalidDataError`, `validate_age()` | Rejects invalid input (zero or negative age) before it reaches storage. |
| **Storage** | `save_to_csv()`, `load_csv()` | Reads and appends records to `patients.csv`, `doctors.csv`, and `appointments.csv`. |
| **Interface** | Streamlit widgets (`st.*`) | Renders the sidebar navigation and forms for all four modules. |
| **Analytics** | `value_counts()`, `mean()`, `st.bar_chart()` | Computes and visualizes disease frequency, average patient age, and daily appointment workload. |

### Object-Oriented Programming Breakdown

- **Class & Object**: `Person`, `Doctor`, `Patient`, and `Appointment` model real-world entities and are instantiated on form submission.
- **Inheritance & `super()`**: `Doctor` and `Patient` inherit `id`, `name`, `age`, and `gender` from the `Person` base class via `super().__init__()`, eliminating code duplication.
- **Encapsulation**: Entity attributes are bundled inside class instances and serialized via `vars()` into dictionaries for CSV storage.
- **Custom Exception Handling**: `InvalidDataError` extends Python's built-in `Exception` class to catch domain-specific input errors cleanly in the UI.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ShyamSR19/HOSPITAL-PATIENT-MANAGEMENT-SYSTEM.git
cd HOSPITAL-PATIENT-MANAGEMENT-SYSTEM
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

## 📊 Application Workflow

1. **Add Patient**: Enter Patient ID, Name, Age, Gender, and Disease. Validates that `age > 0` and saves the record to `patients.csv`.
2. **Add Doctor**: Enter Doctor ID, Name, Age, Gender, and Specialization. Validates `age > 0` and saves the record to `doctors.csv`.
3. **Book Appointment**: Enter Appointment ID, Patient ID, Doctor ID, and select a Date to append the booking to `appointments.csv`.
4. **View Reports**:
   - Interactive tables for **Patients Data**, **Doctors Data**, and **Appointments Data**.
   - **Most Common Diseases** bar chart (`patient_df['disease'].value_counts()`).
   - **Average Age of Patients** metric (`patient_df['age'].mean()`).
   - **Appointments per Day** bar chart (`appointment_df['date'].value_counts()`).

## 🔮 Future Enhancements

- **Database Integration**: Replace CSV storage with SQLite or PostgreSQL/MySQL for relational integrity.
- **Role-Based Authentication**: Add secure login for doctors, receptionists, and administrators.
- **CRUD Operations**: Support searching, editing, and deleting existing patient, doctor, and appointment records.
- **Cross-Reference Validation**: Verify unique IDs and confirm Patient ID / Doctor ID existence before booking appointments.
- **Export & Notifications**: Export reports to PDF/Excel and send automated SMS/email appointment reminders.

## 👥 Team Members

**Institution**: KPR Institute of Engineering and Technology (Autonomous, NAAC "A")  
**Department**: Artificial Intelligence and Data Science (AD-C)  
**Course**: U25CSG05 — Computational Problem Solving Using Python (2025–26)

| Sl. No | Roll No | Name |
| :---: | :---: | :--- |
| 1 | 25AD156 | **SHYAM S R** |
| 2 | 25AD176 | **TURIN R S** |
| 3 | 25AD160 | **SIVAVISHNU M** |
| 4 | 25AD173 | **THANNYAN K M** |
| 5 | 25AD150 | **SANTHOSH KUMAR A** |
| 6 | 25AD185 | **VISHVASH V** |
| 7 | 25AD187 | **YOJESHKUMAR S U** |
| 8 | 25AD190 | **YAGAVAN T M** |
