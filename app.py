import os
import pandas as pd
import streamlit as st


# ==========================================
# 1. OOP Class Definitions
# ==========================================
class Person:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


class Doctor(Person):
    def __init__(self, id, name, age, gender, specialization):
        super().__init__(id, name, age, gender)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, id, name, age, gender, disease):
        super().__init__(id, name, age, gender)
        self.disease = disease


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date


# ==========================================
# 2. Exception Handling & Validation
# ==========================================
class InvalidDataError(Exception):
    pass


def validate_age(age):
    if age <= 0:
        raise InvalidDataError("Age must be positive")


# ==========================================
# 3. File Handling Functions
# ==========================================
PATIENT_FILE = "patients.csv"
DOCTOR_FILE = "doctors.csv"
APPOINTMENT_FILE = "appointments.csv"


def save_to_csv(file, data):
    df = pd.DataFrame([data])
    if not os.path.exists(file):
        df.to_csv(file, index=False)  # new file
    else:
        df.to_csv(file, mode="a", header=False, index=False)  # append


def load_csv(file):
    if os.path.exists(file):
        return pd.read_csv(file)
    return pd.DataFrame()  # empty if missing


# ==========================================
# 4. Streamlit User Interface
# ==========================================
st.title("🏥 Hospital Patient Management Portal")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Patient", "Add Doctor", "Book Appointment", "View Reports"],
)

if menu == "Add Patient":
    st.header("Add Patient")
    pid = st.text_input("Patient ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    disease = st.text_input("Disease")

    if st.button("Save Patient"):
        try:
            validate_age(age)
            patient = Patient(pid, name, age, gender, disease)
            save_to_csv(PATIENT_FILE, vars(patient))
            st.success("Patient saved successfully!")
        except InvalidDataError as e:
            st.error(str(e))

elif menu == "Add Doctor":
    st.header("Add Doctor")
    did = st.text_input("Doctor ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    specialization = st.text_input("Specialization")

    if st.button("Save Doctor"):
        try:
            validate_age(age)
            doctor = Doctor(did, name, age, gender, specialization)
            save_to_csv(DOCTOR_FILE, vars(doctor))
            st.success("Doctor saved successfully!")
        except InvalidDataError as e:
            st.error(str(e))

elif menu == "Book Appointment":
    st.header("Book Appointment")
    aid = st.text_input("Appointment ID")
    pid = st.text_input("Patient ID")
    did = st.text_input("Doctor ID")
    date = st.date_input("Date")

    if st.button("Book Appointment"):
        appointment = Appointment(aid, pid, did, str(date))
        save_to_csv(APPOINTMENT_FILE, vars(appointment))
        st.success("Appointment booked successfully!")

elif menu == "View Reports":
    st.header("Reports")

    st.subheader("Patients Data")
    patient_df = load_csv(PATIENT_FILE)
    st.dataframe(patient_df)

    st.subheader("Doctors Data")
    doctor_df = load_csv(DOCTOR_FILE)
    st.dataframe(doctor_df)

    st.subheader("Appointments Data")
    appointment_df = load_csv(APPOINTMENT_FILE)
    st.dataframe(appointment_df)

    if not patient_df.empty:
        st.subheader("Most Common Diseases")
        st.bar_chart(patient_df["disease"].value_counts())

        st.subheader("Average Age of Patients")
        st.write(patient_df["age"].mean())

    if not appointment_df.empty:
        st.subheader("Appointments per Day")
        st.bar_chart(appointment_df["date"].value_counts())
