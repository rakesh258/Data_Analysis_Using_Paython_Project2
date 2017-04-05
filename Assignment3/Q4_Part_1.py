################################################################################################################################
#          Assignment 3: Author-Vaishali Lambe, NUID-001286444                            #
################################################################################################################################

#**Q4 Part1**

#Movie Awards Analysis
#Use ‘movies_awards’ data set.
#* You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below.
#* The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
#* You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award.
#* If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated).
#* Create two separate columns for each award category (won and nominated).
#* Write your output to a csv file.
################################################################################################################################

# Import libraries we use.
import pandas as pd
import re

# Load the data.
raw_df = pd.read_csv("./Data/movies_awards.csv")
#raw_df.head(10)

# Create a data frame that contains just the title and the awards.
awards_df = raw_df.filter(items=['Title', 'Awards'])
#awards_df.head(10)

# Replace NaNs with 'None'.
awards_df = awards_df.fillna(value="None.", method=None)
#awards_df.head(20)

# Let's have a look at what is in the Awards column.
awards_df['Awards'].unique()

# Extract the awards from the string value of the Awards column.
# Returns a dictionary of award wins and nominations.
def find_awards(t, s):
    #print("{title}: {awards}".format(title=t, awards=s))
    result = { 'Title':t, 'Awards':s, 'Awards_won':0, 'Awards_nominated':0, 'Oscars_Awards_won':0, 'Oscars_Awards_nominated':0,
              'Golden_Globe_Awards_won':0, 'Golden_Globe_Awards_nominated':0,
              'Prime_Awards_won':0, 'Prime_Awards_nominated':0,
              'BAFTA_Awards_won':0, 'BAFTA_Awards_nominated':0,
              'Other_wins':0, 'Other_nominations':0 }

    # No awards.
    if s == 'None':
        return result

    # Start with simple generic wins OR nominations.
    p = re.compile("^(\d+) win[s]?[.]$")
    m = p.match(s)
    if m:
        #print("Wins: " + m.group(1))
        result['Other_wins'] = result["Other_wins"] + int(m.group(1))

    p = re.compile("^(\d+) nomination[s]?[.]$")
    m = p.match(s)
    if m:
        #print("Nominations: " + m.group(1))
        result['Other_nominations'] = result["Other_nominations"] + int(m.group(1))

    # General wins AND nominations.
    p = re.compile("^(\d+) win[s]? & (\d+) nomination[s]?[.]$")
    m = p.match(s)
    if m:
        #print("Wins: " + m.group(1))
        #print("Nominations: " + m.group(2))
        result['Other_wins'] = result["Other_wins"] + int(m.group(1))
        result['Other_nominations'] = result["Other_nominations"] + int(m.group(2))


    # Specific awards - Oscars
    p = re.compile("Won (\d+) Oscar[s]?")
    m = p.search(s)
    if m:
        #print("Oscar wins: " + m.group(1))
        result['Oscars_Awards_won'] = result["Oscars_Awards_won"] + int(m.group(1))

    p = re.compile("[Nn]ominated for (\d+) Oscar[s]?")
    m = p.search(s)
    if m:
        #print("Oscar nominations: " + m.group(1))
        result['Oscars_Awards_nominated'] = result["Oscars_Awards_nominated"] + int(m.group(1))


    # Specific awards - Golden Globes
    p = re.compile("Won (\d+) Golden Globe[s]?")
    m = p.search(s)
    if m:
        #print("Golden Globe wins: " + m.group(1))
        result['Golden_Globe_Awards_won'] = result["Golden_Globe_Awards_won"] + int(m.group(1))

    p = re.compile("[Nn]ominated for (\d+) Golden Globe[s]?")
    m = p.search(s)
    if m:
        #print("Golden Globe nominations: " + m.group(1))
        result['Golden_Globe_Awards_nominated'] = result["Golden_Globe_Awards_nominated"] + int(m.group(1))


    # Specific awards - Primetime Emmys
    p = re.compile("Won (\d+) Primetime Emmy[s]?")
    m = p.search(s)
    if m:
        #print("Primetime Emmy wins: " + m.group(1))
        result['Prime_Awards_won'] = result["Prime_Awards_won"] + int(m.group(1))

    p = re.compile("[Nn]ominated for (\d+) Primetime Emmy[s]?")
    m = p.search(s)
    if m:
        #print("Primetime Emmy nominations: " + m.group(1))
        result['Prime_Awards_nominated'] = result["Prime_Awards_nominated"] + int(m.group(1))


    # Specific awards - BAFTA Awards
    p = re.compile("Won (\d+) BAFTA Film Award[s]?")
    m = p.search(s)
    if m:
        #print("BAFTA wins: " + m.group(1))
        result['BAFTA_Awards_won'] = result["BAFTA_Awards_won"] + int(m.group(1))

    p = re.compile("[Nn]ominated for (\d+) BAFTA Film Award[s]?")
    m = p.search(s)
    if m:
        #print("BAFTA nominations: " + m.group(1))
        result['BAFTA_Awards_nominated'] = result["BAFTA_Awards_nominated"] + int(m.group(1))


    # Additional wins AND nominations.
    p = re.compile("Another (\d+) win[s]?[.]$")
    m = p.search(s)
    if m:
        #print("Wins: " + m.group(1))
        result['Other_wins'] = result["Other_wins"] + int(m.group(1))

    p = re.compile("Another (\d+) nomination[s]?[.]$")
    m = p.search(s)
    if m:
        #print("Nominations: " + m.group(1))
        result['Other_nominations'] = result["Other_nominations"] + int(m.group(1))

    p = re.compile("Another (\d+) win[s]? & (\d+) nomination[s]?[.]$")
    m = p.search(s)
    if m:
        #print("Wins: " + m.group(1))
        #print("Nominations: " + m.group(2))
        result['Other_wins'] = result["Other_wins"] + int(m.group(1))
        result['Other_nominations'] = result["Other_nominations"] + int(m.group(2))

    result['Awards_won'] = result['Oscars_Awards_won'] + result['Golden_Globe_Awards_won'] + result['Prime_Awards_won'] + result['BAFTA_Awards_won'] + result['Other_wins']
    result['Awards_nominated'] = result['Oscars_Awards_nominated'] + result['Golden_Globe_Awards_nominated'] + result['Prime_Awards_nominated'] + result['BAFTA_Awards_nominated'] + result['Other_nominations']

    return result;

if (False):
    test_list = []

    # Unit tests (kind of).
    test_list.append(find_awards('Test 1', 'None.'))
    test_list.append(find_awards('Test 2a', '1 win.'))
    test_list.append(find_awards('Test 2b', '3 wins.'))

    test_list.append(find_awards('Test 3a', '1 nomination.'))
    test_list.append(find_awards('Test 3b', '2 nominations.'))

    test_list.append(find_awards('Test 4a', '1 win & 4 nominations.'))
    test_list.append(find_awards('Test 4b', '5 wins & 1 nomination.'))
    test_list.append(find_awards('Test 4c', '1 win & 1 nomination.'))
    test_list.append(find_awards('Test 4d', '2 wins & 3 nominations.'))

    test_list.append(find_awards('Test 5a', 'Nominated for 1 Oscar. Another 1 win & 13 nominations.'))
    test_list.append(find_awards('Test 5b', 'Nominated for 2 Oscars. Another 13 wins & 1 nomination.'))
    test_list.append(find_awards('Test 5c', 'Nominated for 1 Oscar. Another 13 wins & 17 nominations.'))

    test_list.append(find_awards('Test 6a', 'Nominated for 3 Oscars.'))
    test_list.append(find_awards('Test 6b', 'Won 1 Oscar.'))
    test_list.append(find_awards('Test 6c', 'Won 2 Oscars, nominated for 1 Oscar.'))

    test_list.append(find_awards('Test 7a', 'Nominated for 3 Golden Globes.'))
    test_list.append(find_awards('Test 7b', 'Won 1 Golden Globe.'))
    test_list.append(find_awards('Test 7c', 'Won 2 Golden Globes, nominated for 1 Golden Globe.'))

    test_list.append(find_awards('Test 8a', 'Won 1 Primetime Emmy. Another 1 win & 6 nominations.'))
    test_list.append(find_awards('Test 8b', 'Nominated for 3 BAFTA Film Awards. Another 11 wins & 39 nominations.'))

    #print(test_list)

# Apply the awards-extracting function to the Awards value of each row.
result_list = []
for index, row in awards_df.iterrows():
    #print("{i}".format(i=index))
    result_list.append(find_awards(row['Title'], row['Awards']))

#print(result_list)

# Turn the result list into a dataframe.
final_df = pd.DataFrame(result_list)

# Reorder the columns.
final_df = final_df[['Title', 'Awards', 'Awards_won', 'Awards_nominated', 'Prime_Awards_nominated','Oscars_Awards_nominated',
					'Golden_Globe_Awards_nominated','BAFTA_Awards_nominated','Prime_Awards_won','Oscars_Awards_won','Golden_Globe_Awards_won',  
					'BAFTA_Awards_won', 'Other_nominations','Other_wins']]            
               

# Display the first 10 rows.
print(final_df.head(10))

# Export to CSV.
final_df.to_csv("./Output/Q4_Part_1.csv", index=False)

