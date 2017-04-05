################################################################################################################################
#          Assignment 3: Author-Vaishali Lambe, NUID-001286444                            #
################################################################################################################################
# Question 2 Part One

#* Use 'employee_compensation' data set.
#* Find out the highest paid departments in each organization group by calculating mean of total compensation for every department.
#* Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value.
#* Display a few rows of the output use df.head().
#* Generate a CSV output.
################################################################################################################################

# Load libraries.
import pandas as pd

# Load the data.
raw_df = pd.read_csv("./Data/employee_compensation.csv")
#print(raw_df.head(10))

# Create a data frame that contains just the data we want.
matches_df = raw_df.filter(items=['Organization Group', 'Department', 'Total Compensation'])
matches_df.info()
#print(matches_df.head(10))

# Create the list of departments.
departments = matches_df['Department'].unique()
#print(departments)

# Select employees from each department and calculate the mean of their total compensation.
result_list = []
for d in departments:
    department_mean_total_compensation = matches_df[matches_df['Department'] == d]['Total Compensation'].mean()
    #print("{dept}: {pay}".format(dept=d, pay=department_mean_total_compensation))

    # Find the organisation group that matches the department.
    org_group = matches_df[matches_df['Department'] == d]['Organization Group'].unique()
    if len(org_group) > 1:
        print("*** Department {dept} has multiple organization groups".format(dept=d))

    #print(org_group[0])

    result_list.append({'Organization Group':org_group[0], 'Department':d,
                        'Total Compensation':department_mean_total_compensation})

# Create the final dataframe.
final_df = pd.DataFrame(result_list)

# Order the dataframe's columns.
final_df = final_df[['Organization Group', 'Department', 'Total Compensation']]
#print(final_df[['Organization Group', 'Department', 'Total Compensation']].head(10))

# Sort the rows by Total Compensation (which is actually Mean Total Compensation).
sorted_df = final_df.sort_values(by=['Organization Group', 'Total Compensation'], ascending=[True, False])
print(sorted_df[['Organization Group', 'Department', 'Total Compensation']].head(10))

# Export the dataframe to a CSV file.
sorted_df.to_csv('./Output/Q2_Part_1.csv', index=False)
