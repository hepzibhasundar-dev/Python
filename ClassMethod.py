#Class method
#class level data we can override
class Employee:
    company_name = "OpenAI" #class-level data

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

Employee.change_company("Google")
print(Employee.company_name) # output : Google

