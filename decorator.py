import re

def validate(func):
    """Decorator that validates email IDs before passing to segregate()"""
    def inner(participants_list):
        valid_list = []
        for participant in participants_list:
            email = participant[2]
            # Valid email: must have characters, @, domain, and extension
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                valid_list.append(participant)
        # Call the original segregate function with validated list
        return func(valid_list)
    return inner

@validate
def segregate(participants_list):
    """Counts participants in each age category after email validation."""
    under_10 = 0
    under_15 = 0
    under_20 = 0
    for participant in participants_list:
        age = int(participant[1])
        if age >= 5 and age < 10:
            under_10 += 1
        elif age >= 10 and age < 15:
            under_15 += 1
        elif age >= 15 and age < 20:
            under_20 += 1
    return under_10, under_15, under_20

def main():
    participants_list = []

    # Collect participant details
    while True:
        details = input("Enter the candidate details as (name:age:email): ")
        participant = details.split(":")
        participants_list.append(participant)
        choice = input("Do you want to enter another candidate's details(y/n): ")
        if choice.lower() == 'n':
            break

    # Call segregate (decorator will validate emails first)
    under_10, under_15, under_20 = segregate(participants_list)

    # Display results
    print(f"\nNo. of participants under 10: {under_10}")
    print(f"No. of participants under 15: {under_15}")
    print(f"No. of participants under 20: {under_20}")

if __name__ == "__main__":
    main()