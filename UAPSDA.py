#selamat datang di kode ini
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

# Nama file CSV untuk menyimpan data pasien
FILE_NAME = 'patients.csv'

# Fungsi untuk menambahkan pasien baru ke dalam sistem
def add_patient():
    name = simpledialog.askstring("Input", "Masukkan Nama Pasien:")
    age = simpledialog.askinteger("Input", "Masukkan Umur Pasien:")
    gender = simpledialog.askstring("Input", "Masukkan Jenis Kelamin Pasien (L/P):")
    
    if name and age and gender:
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, gender])
        messagebox.showinfo("Sukses", "Pasien berhasil ditambahkan")
    else:
        messagebox.showerror("Error", "Semua informasi pasien harus diisi")

# Fungsi untuk menampilkan daftar pasien yang terdaftar
def view_patients():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        patients = list(reader)
    
    view_window = tk.Toplevel(root)
    view_window.title("Daftar Pasien")

    for i, patient in enumerate(patients):
        tk.Label(view_window, text=f"{i+1}. Nama: {patient[0]}, Umur: {patient[1]}, Jenis Kelamin: {patient[2]}").pack()

# Fungsi untuk memperbarui informasi pasien yang ada
def update_patient():
    patient_id = simpledialog.askinteger("Input", "Masukkan ID Pasien yang ingin diperbarui:")
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        patients = list(reader)
    
    if 0 < patient_id <= len(patients):
        name = simpledialog.askstring("Input", "Masukkan Nama Baru (kosongkan jika tidak ingin diubah):")
        age = simpledialog.askstring("Input", "Masukkan Umur Baru (kosongkan jika tidak ingin diubah):")
        gender = simpledialog.askstring("Input", "Masukkan Jenis Kelamin Baru (kosongkan jika tidak ingin diubah):")

        if name:
            patients[patient_id - 1][0] = name
        if age:
            patients[patient_id - 1][1] = age
        if gender:
            patients[patient_id - 1][2] = gender
        
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(patients)
        
        messagebox.showinfo("Sukses", "Informasi pasien berhasil diperbarui")
    else:
        messagebox.showerror("Error", "ID Pasien tidak valid")

# Fungsi untuk menghapus data pasien dari sistem
def delete_patient():
    patient_id = simpledialog.askinteger("Input", "Masukkan ID Pasien yang ingin dihapus:")
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        patients = list(reader)
    
    if 0 < patient_id <= len(patients):
        del patients[patient_id - 1]
        
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(patients)
        
        messagebox.showinfo("Sukses", "Pasien berhasil dihapus")
    else:
        messagebox.showerror("Error", "ID Pasien tidak valid")

# Pengaturan antarmuka Tkinter
root = tk.Tk()
root.title("Manajemen Pasien Rumah Sakit")

tk.Button(root, text="Tambah Pasien", command=add_patient).pack(pady=5)
tk.Button(root, text="Lihat Pasien", command=view_patients).pack(pady=5)
tk.Button(root, text="Update Pasien", command=update_patient).pack(pady=5)
tk.Button(root, text="Hapus Pasien", command=delete_patient).pack(pady=5)

root.mainloop()
