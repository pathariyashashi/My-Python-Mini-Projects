# Patient Class
class Patient:

    # Constructor
    def __init__(self, patient_id, name, age):

        self.patient_id = patient_id
        self.name = name
        self.age = age

    # Show Patient Details
    def show_patient(self):

        print("\nPatient ID:", self.patient_id)

        print("Patient Name:", self.name)

        print("Age:", self.age)


# Doctor Class
class Doctor:

    # Constructor
    def __init__(self, doctor_id, name, specialization):

        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    # Show Doctor Details
    def show_doctor(self):

        print("\nDoctor ID:", self.doctor_id)

        print("Doctor Name:", self.name)

        print("Specialization:", self.specialization)


# Appointment Class
class Appointment:

    # Constructor
    def __init__(self, patient, doctor, fees):

        self.patient = patient

        self.doctor = doctor

        self.fees = fees

        self.status = "Booked"

    # Show Appointment
    def show_appointment(self):

        print("\n----- Appointment Details -----")

        print("Patient:", self.patient.name)

        print("Doctor:", self.doctor.name)

        print("Specialization:", self.doctor.specialization)

        print("Appointment Status:", self.status)

    # Bill Generation
    def generate_bill(self):

        print("\n----- Hospital Bill -----")

        print("Patient:", self.patient.name)

        print("Doctor Fees: ₹", self.fees)

    # Appointment Complete
    def complete_appointment(self):

        self.status = "Completed"

        print("\nAppointment Completed Successfully")


# Patient Object
p1 = Patient(1, "Shashi", 22)

# Doctor Object
d1 = Doctor(101, "Dr. Rahul", "Cardiologist")

# Appointment Booking
a1 = Appointment(p1, d1, 500)

# Show Patient
p1.show_patient()

# Show Doctor
d1.show_doctor()

# Show Appointment
a1.show_appointment()

# Generate Bill
a1.generate_bill()

# Complete Appointment
a1.complete_appointment()

# Show Updated Appointment
a1.show_appointment()