#kargs - key value pairs
def create_profile(**kwargs):
    print("User Profile")
    for key,value in kwargs.items():
        print(f"{key} : {value}")

create_profile(name="Hepzibha", age=35, job="Data Engineer")