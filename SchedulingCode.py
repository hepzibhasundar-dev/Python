# new joining employee create the email 
import sys

if len(sys.argv) == 2:
    print("Usage: python email_generator.py 'Full name and last name'")
    sys.exit()

full_name = sys.argv[1]
last_name = sys.argv[2]

# full_name = sys.argv[1:]
# full_name = "".join(sys.argv[1:])

#format the name 
#email=full_name.lower().replace(__old: " ", __new: ".")+last_name + "@company.com" # type: ignore
email=full_name.lower().replace(" ", ".")+last_name + "@company.com" 
#output
print("\n--- Your Profile ---")
print("Full Name : ", full_name+last_name)
print("Generated Email : ", email)