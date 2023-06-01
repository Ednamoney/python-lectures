# Given criteria for competition

# Using a functional approach that computes the total salary of an individual
def individual_salary():
    
# Declaring the required Variable

    minimum_wage=400 # declaring minimum per month
    yearly_increment=20
    child_bonus=30

    # prompting the user to input the number of years employed and number of children as integer
    number_of_years=int(input('Enter the number of years emplyed:'))
    number_of_children=int(input('Enter the number of children that you have:'))

    # computing the salary
    total_salary=minimum_wage+(yearly_increment*number_of_years)+(child_bonus*number_of_children)
    return total_salary