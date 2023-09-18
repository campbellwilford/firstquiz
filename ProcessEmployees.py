'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

#open the file

with open('employee_data.csv', mode='r') as file:
    reader = csv.DictReader(file)


#create an empty dictionary
    report = {}

#use a loop to iterate through the csv file
    for row in reader:
        old = float(row['Salary'])
        new = old * 1.1

    #check if the employee fits the search criteria
        emp_name = f"{row['First Name']} {row['Last Name']}"
        report[emp_name] = new

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per image


for name,new in report.items():
    print(f"Employee Name: {name} Current Salary: ${old:.2f}")
    print()
    print('=========================================')
    print()
    print(f"Employee Name: {name} New Salary: ${new:.2f}")

          

print()
print('=========================================')
print()

#print out the total difference between the old salary and the new salary as per image.

difference = (new - old)
print(f"Total Increase in Salary: ${difference:.2f}")