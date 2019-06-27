class Student():
	def __init__(self, name, lastname, department, year_of_entrance):
		self.name = name
		self.lastname = lastname
		self.department = department
		self.year_of_entrance = year_of_entrance

	def get_student_info(self):
		s = f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}'
		return s


student = Student('Василий', "Иванов", "Программирование", "2017")

result = student.get_student_info()
print(result)