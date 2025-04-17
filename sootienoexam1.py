 

...     
...     #  gross salary
...     gross_salary = hourly_rate * hours_worked
...     
...     #  tax deduction
...     tax_deduction = gross_salary * tax_rate
...     
...     #  net salary
...     net_salary = gross_salary - tax_deduction
...     
...     return net_salary
... 
... # User with the user and calculate the salary
... def main():
...     # Get user input for hourly rate and hours worked
...     try:
...         hourly_rate = float(input("Enter hourly rate: "))
...         hours_worked = float(input("Enter hours worked: "))
...         
...         # Validate input to ensure no negative values
...         if hourly_rate < 0 or hours_worked < 0:
...             print("Error: Hourly rate and hours worked must be non-negative.")
...             return
...         
...         # Calculate net salary using the calculate_salary function
...         net_salary = calculate_salary(hourly_rate, hours_worked)
...         
...         # Print the formatted net salary
...         print(f"Net Salary: {net_salary:,.2f}")
...     
...     except ValueError:
        print("Error: Please enter valid numeric values.")

# Run the main function
if __name__ == "__main__":
    main()
