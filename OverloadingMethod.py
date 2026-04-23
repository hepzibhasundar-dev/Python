from multipledispatch import dispatch

class tournament:

    # Cricket → 3 integers
    @dispatch(int, int, int)
    def calculateScore(sixers, fours, singles):
        score = (sixers * 6) + (fours * 4) + singles
        print("Calculated Score:", score)
        return score

    # Carrom → 2 integers + string
    @dispatch(int, int, str)
    def calculateScore(white, black, red):
        score = (white * 2) + (black * 1)
        if red.lower() == "yes":
            score = score + 5
        print("Calculated Score:", score)
        return score

    # Basketball → 2 integers
    @dispatch(int, int)
    def calculateScore(value1, value2):
        score = value1 - value2
        print("Calculated Score:", score)
        return score


# ---------------------------
# MAIN PROGRAM
# ---------------------------

t = tournament()

print("CRICKET:")
s = int(input("Enter the number of sixers: "))
f = int(input("Enter the number of fours: "))
si = int(input("Enter the number of singles: "))
if type(s) != int:
    print("Invalid")
t.calculateScore(s, f, si)

print("\nCARROM:")
w = int(input("Enter the number of white coins pocket: "))
b = int(input("Enter the number of black coins pocket: "))
r = input("Red Pocket(yes/no): ")
t.calculateScore(w, b, r)

print("\nBASKETBALL:")
g = int(input("Enter the number of goals: "))
fo = int(input("Enter the number of fouls: "))
t.calculateScore(g, fo)
