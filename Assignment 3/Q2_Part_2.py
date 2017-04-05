################################################################################################################################
#          Assignment 3: Author-Vaishali Lambe, NUID-001286444                            #
################################################################################################################################
# Question 2 Part 2

#* Use 'employee_compensation' data set.
#* Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
#* Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
#* For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
#* Display the top 5 Job Families according to this percentage value using df.head().
#* Write the output (jobs and percentage value) to a CSV file.
################################################################################################################################

# Load libraries.
import pandas as pd

# Load the data.
raw_df = pd.read_csv("./Data/employee_compensation.csv")
#print(raw_df.head(10))

# Create a data frame that contains just the data we want.

# First include only Calendar year data.
reduced_df = raw_df[raw_df['Year Type'] == 'Calendar']
#reduced_df.info()

# Now keep only employees with overtime more than 5% of their salary.
reduced_df = reduced_df[reduced_df['Overtime'] > (0.05 * reduced_df['Salaries'])]
#reduced_df.info()

#print(reduced_df.head(10))


# Find the job families in the data frame.
job_families = reduced_df['Job Family'].unique()
#print(job_families)


# Calculate the total benefits as a percentage of total compensation for each job family.
result_list = []

for jf in job_families:
    # Filter so only the current Job Family data is retained.
    family_df = reduced_df[reduced_df['Job Family'] == jf]

    # Calculate mean for total benefits and total compensation.
    mean_total_benefits = family_df['Total Benefits'].mean()
    mean_total_compensation = family_df['Total Compensation'].mean()
	#print("{jf} benefits = {mb}, compensation = {mtc}".format(jf=jf,mb=mean_total_benefits, mtc=mean_total_compensation))                                                               
                                                              
    # Calculate mean total benefits as a percentage of mean total compensation.
    percentage = round((100 * mean_total_benefits) / mean_total_compensation, 3)
    result_list.append({'Job Family':jf, 'Mean Total Benefits':mean_total_benefits,
                        'Mean Total Compensation':mean_total_compensation, 'Percent_Total_Benefits': percentage})

#print(result_list)

# Create the final dataframe.
final_df = pd.DataFrame(result_list)

# Order the dataframe's columns.
final_df = final_df[['Job Family', 'Mean Total Benefits', 'Mean Total Compensation', 'Percent_Total_Benefits']]
#print(final_df[['Job Family', 'Percent_Total_Benefits']].head(10))

# Sort the rows by mean total benefits as a percentage of mean total compensation.
final_df.sort_values(by='Percent_Total_Benefits', ascending=False, inplace=True)
print(final_df.head(5))

# Export the dataframe to a CSV file.
final_df.to_csv('./Output/Q2_Part_2.csv', index=False)
