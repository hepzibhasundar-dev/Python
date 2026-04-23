#String handling and string functions
# uber use case
driver_name = 'Ganesh'

print(driver_name.lower())
print(driver_name.upper())
print(driver_name.capitalize())

mobile='9879786545'
masked=mobile[:2]
print(masked)
masked1=mobile[-2:]
print(masked1)
masked2=mobile[:2]+"******"+mobile[-2:]
print(masked2)

# use case to song
song = "shape OF you"
artist="Subramanian SB"
formatted=f"{song.title()} - {artist.title()}"
print(formatted)

# uber use case
location="chennai central"
fixed_location=location.replace("chennai central", "Tambaram")
print(fixed_location)

message="Your uber booking id is : UB12345.  Please keep it safe"
booking_id=message.split(":")[1].split(".")[0].strip()
print(booking_id)

#create data set
#split with delimiter
#zomato use case
#only take the coupon code
promo_msg="use zomoto100 to get 100 off on your first order"
if"zomoto100" in promo_msg:
    print("Offer Applied")

feedback="the driver was polite and the ride was smooth"
print("Position is : ", feedback.find("polite"))

name="hepzibha sundararaj"
initials="".join([word[0].upper() for word in name.split()])
print(initials)

#remove the spaces using strip()
dierty_input = "      airport     "
clean=dierty_input.strip()
print(clean)

#count the number of words
word1="the trip was amazing and the car was clean"
word_count=len(word1.split()) #delimiter space
print(word_count)


