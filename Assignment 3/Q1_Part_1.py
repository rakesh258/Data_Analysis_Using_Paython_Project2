################################################################################################################################
#          Assignment 3: Author-Vaishali Lambe, NUID-001286444                            #
################################################################################################################################
#**Q1 Part1**

#* Use ‘vehicle_collisions’ data set.
#* For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City.
#* Display a few rows of the output use df.head().
#* Generate a CSV output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)
################################################################################################################################

# Import libraries we use.
import pandas as pd

raw_df = pd.read_csv("./Data/vehicle_collisions.csv")
#print(raw_df.info())
#raw_df.head(10)

# Create a data frame that contains just the data we want.
collisions_df = raw_df.filter(items=['DATE', 'BOROUGH'])
#collisions_df.head(10)

# This will come in handy a couple of times.
months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Initialise the results, organised as a list in month order.
result_list = []
for m in months_list:
    result_list.append({'MONTH':m, 'MANHATTAN':0, 'NYC':0})

for i, row in collisions_df.iterrows():
    # Skip data that isn't for 2016.
    if not row['DATE'].endswith('16'):
        continue

    month_number = int(row['DATE'].split('/')[0]) - 1

    # Add 1 to all NYC accidents.
    result_list[month_number]['NYC'] += 1

    # Check whether this is a Manhattan accident too.
    if row['BOROUGH'] == 'MANHATTAN':
        result_list[month_number]['MANHATTAN'] += 1

#print(result_list)

# Put the data into a data frame, in order.
final_df = pd.DataFrame(result_list)
final_df['PERCENTAGE'] = final_df['MANHATTAN'] / final_df['NYC']

# Rearrange the columns.
final_df = final_df[['MONTH', 'MANHATTAN', 'NYC', 'PERCENTAGE']]
print(final_df.head(12))

# Export to CSV.
final_df.to_csv("./Output/Q1_Part_1.csv", index=False)

