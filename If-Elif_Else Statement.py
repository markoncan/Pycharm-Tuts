min_salary=30000.0
min_years=2
def main():
    salary=float(input("Enter your annual Income: "))
    years_on_job=int(input("Enter years of experience: "))
    if salary>=min_salary:
        if years_on_job>=min_years:
            print("You qualify for the loan")
        else:
            print("You must employed at least ", min_years," years to qualify for the loan")
    else:
        print("You should have at least $", min_salary," to qualify for the loan")
main()
