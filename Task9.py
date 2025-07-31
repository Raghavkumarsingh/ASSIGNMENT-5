dict1 = {'Raghav':70, 'Akash':80,'Alam':90,'Sai':99,'Pritam':88}
Name = input("Enter the student's name: ")
if Name in dict1.keys():
    print(f'{Name} maks: {dict1[Name]}')
else:
    print("Student not found.")