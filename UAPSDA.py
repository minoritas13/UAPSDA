import csv

FILE_NAME = 'patients.csv'

class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Nama: {self.name}, Umur: {self.age}, Jenis Kelamin: {self.gender}"

class HospitalManagement:
    def __init__(self):
        self.patients = self.load_patients()

    def load_patients(self):
        patients = []
        try:
            with open(FILE_NAME, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        patients.append(Patient(row[0], int(row[1]), row[2]))
        except FileNotFoundError:
            pass
        return patients

    def save_patients(self):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            for patient in self.patients:
                writer.writerow([patient.name, patient.age, patient.gender])

    def add_patient(self, patient):
        self.patients.append(patient)
        self.save_patients()

    def get_patients(self):
        return self.patients

    def update_patient(self, index, name=None, age=None, gender=None):
        if 0 <= index < len(self.patients):
            if name:
                self.patients[index].name = name
            if age:
                self.patients[index].age = age
            if gender:
                self.patients[index].gender = gender
            self.save_patients()
            return True
        return False

    def delete_patient(self, index):
        if 0 <= index < len(self.patients):
            del self.patients[index]
            self.save_patients()
            return True
        return False

def main_menu():
    print("\n=== Manajemen Pasien Rumah Sakit ===")
    print("1. Tambah Pasien")
    print("2. Lihat Pasien")
    print("3. Update Pasien")
    print("4. Hapus Pasien")
    print("5. Keluar")

def add_patient_menu(hospital):
    name = input("Masukkan Nama Pasien: ")
    age = input("Masukkan Umur Pasien: ")
    gender = input("Masukkan Jenis Kelamin Pasien (L/P): ")
    
    if name and age.isdigit() and gender in ['L', 'P']:
        patient = Patient(name, int(age), gender)
        hospital.add_patient(patient)
        print("Pasien berhasil ditambahkan.")
    else:
        print("Informasi pasien tidak valid.")

def view_patients_menu(hospital):
    patients = hospital.get_patients()
    if patients:
        for i, patient in enumerate(patients):
            print(f"{i + 1}. {patient}")
    else:
        print("Tidak ada pasien yang terdaftar.")

def update_patient_menu(hospital):
    view_patients_menu(hospital)
    try:
        patient_id = int(input("Masukkan ID Pasien yang ingin diperbarui: ")) - 1
        name = input("Masukkan Nama Baru (kosongkan jika tidak ingin diubah): ")
        age = input("Masukkan Umur Baru (kosongkan jika tidak ingin diubah): ")
        gender = input("Masukkan Jenis Kelamin Baru (kosongkan jika tidak ingin diubah): ")

        if not age.isdigit() and age:
            print("Umur tidak valid.")
            return

        if hospital.update_patient(patient_id, name or None, int(age) if age else None, gender or None):
            print("Informasi pasien berhasil diperbarui.")
        else:
            print("ID Pasien tidak valid.")
    except ValueError:
        print("ID Pasien tidak valid.")

def delete_patient_menu(hospital):
    view_patients_menu(hospital)
    try:
        patient_id = int(input("Masukkan ID Pasien yang ingin dihapus: ")) - 1
        if hospital.delete_patient(patient_id):
            print("Pasien berhasil dihapus.")
        else:
            print("ID Pasien tidak valid.")
    except ValueError:
        print("ID Pasien tidak valid.")

def main():
    hospital = HospitalManagement()
    while True:
        main_menu()
        choice = input("Pilih menu: ")
        if choice == '1':
            add_patient_menu(hospital)
        elif choice == '2':
            view_patients_menu(hospital)
        elif choice == '3':
            update_patient_menu(hospital)
        elif choice == '4':
            delete_patient_menu(hospital)
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
