#Static method can't change class level or object level - individu
class Employee:
    company = "OpenAI"  # 💡class-level data

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name # ✅ Accessing class variable

    @staticmethod
    def try_change_company(new_name):
        company = new_name

#Call both methods
Employee.change_company("Google")
print("After classmethod : ", Employee.company)

Employee.try_change_company("Meta")
print("After static method : ", Employee.company)