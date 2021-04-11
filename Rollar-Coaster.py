#Rollar Coaster Ticket project
print('Welcome to Rollar Coaster ride')
height = float(input('Enter your height in m '))
age = int(input('Enter your age '))
total=0
if height > 120:
    print('You can ride')
    if age<12:
        print('You need to pay $5')
        total=5
    elif age<=18:
        print('You need to pay $7')
        total=7
    else:
        print('You need to pay $12')
        total=12
else:
    print('Grow up baby')

pic = input('Do you want photos? YES or NO ')
if(pic == 'YES'):
    print("You need to pay additional $3")
    total+=3

print(f"Your Total amount is:${total} ")
