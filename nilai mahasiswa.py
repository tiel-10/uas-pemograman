class StudentData:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        self.students.append({'name': name, 'score': score})

    def get_students(self):
        return self.students


class StudentView:
    def display_students(self, students):
        print("\nDaftar Siswa:")
        print("{:<20} {:<10}".format("Nama Siswa", "Nilai"))
        print("-" * 30)
        for student in students:
            print("{:<20} {:<10}".format(student['name'], student['score']))


class StudentProcess:
    def __init__(self):
        self.data = StudentData()
        self.view = StudentView()

    def get_student_input(self):
        while True:
            try:
                name = input("Masukkan nama siswa: ")
                score = float(input("Masukkan nilai siswa: "))
                if score < 0 or score > 100:
                    raise ValueError("Nilai harus antara 0 dan 100.")
                self.data.add_student(name, score)
                break 
            except ValueError as e:
                print(f"Input tidak valid: {e}. Silakan coba lagi.")

    def run(self):
        while True:
            self.get_student_input()
            another = input("Apakah Anda ingin menambahkan siswa lain? (y/n): ")
            if another.lower() != 'y':
                break
        self.view.display_students(self.data.get_students())


if __name__ == "__main__":
    process = StudentProcess()
    process.run()
