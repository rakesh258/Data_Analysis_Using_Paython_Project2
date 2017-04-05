################################################################################################################################
#          Assignment 3: Author-Vaishali Lambe, NUID-001286444                            #
################################################################################################################################
#**Q1 Part2**

#Use ‘vehicle_collisions’ data set.
#* For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present)
#* Display a few rows of the output use df.head().
#* Generate a CSV output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')
################################################################################################################################

# Import libraries we use.
import pandas as pd

raw_df = pd.read_csv("./Data/vehicle_collisions.csv")
#print(raw_df.info())
#raw_df.head(10)

import math

# Create a data frame that contains just the data we want.
collisions_df = raw_df.filter(items=['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE',
                                     'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE', 'VEHICLE 5 TYPE'])
collisions_df.head(10)

# Get the list of boroughs, since it'll be useful.
borough_list = collisions_df['BOROUGH'].unique()
#print(borough_list)

# Strip out the NaN value, and add 'OTHER' instead.
borough_list = [b for b in borough_list if not pd.isnull(b)]
borough_list.append('OTHER')
#print(borough_list)

# Find the scale of the collisions in each district.

# Initialise the results, organised as a list in month order.
result_dict = {}
for b in borough_list:
        result_dict[b] = {'BOROUGH':b, 'ONE_VEHICLE_INVOLVED':0, 'TWO_VEHICLES_INVOLVED':0,
                            'THREE_VEHICLES_INVOLVED':0, 'FOUR_VEHICLES_INVOLVED':0, 'FIVE_VEHICLES_INVOLVED':0 }

# Iterate over the data and extract the collision data.
for i, row in collisions_df.iterrows():

    # Find the borough, replacing NaN with 'OTHER'.
    if pd.isnull(row['BOROUGH']):
        b = 'OTHER'
    else:
        b = row['BOROUGH']

    # Determine how many vehicles were involved.
    if not pd.isnull(row['VEHICLE 5 TYPE']):
        result_dict[b]['FIVE_VEHICLES_INVOLVED'] += 1

    elif not pd.isnull(row['VEHICLE 4 TYPE']):
        result_dict[b]['FOUR_VEHICLES_INVOLVED'] += 1

    elif not pd.isnull(row['VEHICLE 3 TYPE']):
        result_dict[b]['THREE_VEHICLES_INVOLVED'] += 1

    elif not pd.isnull(row['VEHICLE 2 TYPE']):
        result_dict[b]['TWO_VEHICLES_INVOLVED'] += 1

    elif not pd.isnull(row['VEHICLE 1 TYPE']):
        result_dict[b]['ONE_VEHICLE_INVOLVED'] += 1

#print(result_dict)

# Put the data into a data frame, in order.
final_df = pd.DataFrame(list(result_dict.values()))

# Rearrange the columns.
final_df = final_df[['BOROUGH', 'ONE_VEHICLE_INVOLVED', 'TWO_VEHICLES_INVOLVED', 'THREE_VEHICLES_INVOLVED',
                     'FOUR_VEHICLES_INVOLVED', 'FIVE_VEHICLES_INVOLVED']]
#print(final_df)

# Add the four-vehicle and five-vehicle columns to get the 'more' vehicles column.
final_df['MORE_VEHICLES_INVOLVED'] = final_df['FOUR_VEHICLES_INVOLVED'] + final_df['FIVE_VEHICLES_INVOLVED']
#print(final_df)

# Drop the four-vehicle and five-vehicle columns.
final_df = final_df[['BOROUGH', 'ONE_VEHICLE_INVOLVED', 'TWO_VEHICLES_INVOLVED', 'THREE_VEHICLES_INVOLVED',
                     'MORE_VEHICLES_INVOLVED']]
print(final_df.head(5))

# Export to CSV.
final_df.to_csv("./Output/Q1_Part_2.csv", index=False)
