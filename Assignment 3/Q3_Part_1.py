################################################################################################################################
#                                       Assignment 3: Author-Vaishali Lambe, NUID-001286444                                    #
################################################################################################################################

#**Q3 Part1**

#Use ‘cricket_matches’ data set.
#* Calculate the average score for each team which host the game and win the game.
#* Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
#* Display a few rows of the output use df.head()
#* Generate a csv output
################################################################################################################################
# Load libraries.
import pandas as pd

raw_df = pd.read_csv("./Data/cricket_matches.csv")
#raw_df.head(10)

# Create a data frame that contains just the data we want.
matches_df = raw_df.filter(items=['home', 'winner', 'win_by_runs', 'innings1_runs', 'innings2_runs'])
#matches_df.info()
#matches_df.head(10)

# Filter down to matches where the home team won.
matches_df = matches_df[matches_df['home'] == matches_df['winner']]
#matches_df.info()
#matches_df.head(10)

# Add a new column for tracking the winning runs.
matches_df['winning_runs'] = 0.0
#matches_df.head(10)

# Consolidate the innings1_runs and innings2_runs columns into winning_runs.
for i in matches_df.index:
    # The winning team is always the team with the highest score.
    # But it could also be done by looking at the win_by_runs column: 
    #     if win_by_runs == NaN use innings2_runs else use innings1_runs
    matches_df.ix[i, 'winning_runs'] = max(matches_df.ix[i, 'innings1_runs'], matches_df.ix[i, 'innings2_runs'])
    
#matches_df.head(10)

mean_winning_score = matches_df['winning_runs'].mean()
#print(mean_winning_score)

teams = matches_df['home'].unique()
#print(teams)

# Calculate the average score for each team's home wins.

result_list = []

for t in teams:
    team_winning_average = matches_df[matches_df['home'] == t]['winning_runs'].mean()
    #print("{team} wins with an average of {score}".format(team=t, score=team_winning_average))
    result_list.append({'Team':t, 'Score':team_winning_average})
    
final_df = pd.DataFrame(result_list)
final_df = final_df[['Team', 'Score']]
print(final_df.head(10))

# Export the results to a CSV file.
final_df.to_csv('./Output/Q3_Part_1.csv', index=False)