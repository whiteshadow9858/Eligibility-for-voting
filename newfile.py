print ('Can you vote , lets check')
name = input('Enter name ')
age = int(input("Enter Age (only numbers): "))

if age>=18:
        status="can"
else:
    status="can not"

print( name,status," Vote.")
