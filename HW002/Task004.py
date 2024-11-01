salary_year = 0 
for month in range (1,13):
    salary_month = int(input ("Enter the employee month salary:"))
    salary_year =+ salary_month
average_salary = salary_year/12
print ("The average salary for a year: ", average_salary)