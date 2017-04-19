Final submissiong : Name- Vaishali Lambe : NUID-001286444
=============================================================================================================================
-----------
Synopsis
------------
This folder contains the the following files for Final submission

> - Data collection and storage script
>  ```final/datacollectionandstorage.ipynb or final/datacollectionandstorage.py```  file to collect data from NYTimes developer portal for analysis 1, 2 and 3 of  movie reviews API 

> - Data storage folder structure
>  ```final/midterm/data/collection/movie_reviews``` This is data storage location
>  ```midterm/question1/ana[1-3]``` *.ipynb* files for analysis 1, 2 and 3 for 

> - Analysis 1 script file location
>  ```final/analysis1.ipynb or final/analysis1.py``` script for analysis 1

> - Analysis 2 script file location
>  ```final/analysis2.ipynb or final/analysis2.py``` script for analysis 2

> - Analysis 3 script file location
>  ```final/analysis3.ipynb or final/analysis3.py``` script for analysis 3

> - Output files
>  ```final/output``` contains all the outputs for analysis 1, analysis 2 and analysis 3

-----------
Collecting Data
------------
Wrote *.ipynb* files to gather article data and remove duplicates. **```request```** module is used to fetch data, **```glob```** is used to read files if they are already present, **```current_dir = os.path.dirname('__file__')```** is used to get current folder's relative path. 
```Midterm_Question2_Data_Gathering.ipynb``` file is used to hit **articlesearch** and **archive** api for *New York Times*.  
This file takes care of removing the duplicate articles. If the article fetched is already preset in output, this file wont add that again. This prevents duplication and false data visualization.
####<i class="icon-file"></i>Midterm_Question2_Data_Gathering.ipynb
> **Logic:**

> - Exported the nytimes developer api key to bash terminal and read as an *environment variable*
> - Used a list to store the api names which will be used to fetch data. I have used **articlesearch** and **archive** apis to fetch data in json format
> - Wrote functions to create folder structure as follows:
		>```data/question2/<api_name>/<api_name>_response_page.json```. Used relative path to create folders and to store json response in json file
> - Wrote a function to get the range of month and year for past 6 months to be used for archives API. Used ```datetime``` module to get today's month and year. Get all months in current year and decrement month count. If month count is less than 0 then change year to previous year and start month count from 12. This will eliminate the need to keep a check on year change.
> - Wrote a function to fetch response from APIs passed as input parameter. This method is  called for both the APIs so parameters for both APIs are sent as input parameters. Using ```if``` condition kept a check on API to fetch response from. Used ```payload``` to pass API key and rest of query string. And returned the ```response``` object.
> - Wrote a method to process the response fetched from both the APIs and write to a json file. Check if the file exists, otherwise create the file. If the file is already present, get its content and compare with the content from response. If any article from response is already present in the file already existing, don't append it to the file. Input parameters are response, api name, path of file to store response, list object tro check if data already exist at the path mentioned. 
> - In a for loop, extract each API's name from its directory name and fetch its response. Send the response to process method mentioned above. Use ```time.sleep``` to make the system wait for some time before sending next request. This lets us fetch multiple responses in a for loop. If the API is archive, call method to get *year* and *month* range and use them as input parameter to fetch response. If the API is articlesearch, use *page* variable to pass as input parameter to fetch response. 
> - The response from each API will be stored in respective data folders in json format. Thing to note here is, I am extracting the articles from response and storing the article list without duplicates. Reduces me processing during analysis period.

```Midterm_Data_Duplication_Removal.ipynb``` file is used to **remove duplicate** articles if fetched by mistake over the period of days. The *articlesearch* API gives latest posts up to 120 pages. If we fetch all 120 pages within a span of 2 hours and append the results in a single file, we will get multiple duplicate articles. This file removes that ambiguity. Previously **Data_Gathering** file was used to store each response as a different file so this file was used to combine all them and remove duplicates. Now there is no need to run this file as it is taken care in the file above.

-----------
### Analysis 2
For Analysis 2, I am finding all people who used some suspected words. I maintained the list of suspected words in stemmed format, which I found out from [this article](http://www.investopedia.com/updates/enron-scandal-summary/) shared by professor. I considered the **sent, received and deleted** folder of all people. If the folder names had *sent*, *delete* or *inbox* mentioned in them, they are considered for this analysis. I collected all such users using suspected words in a dictionary, sorted it by name, as the values had the entire list of emails in them. Saved the output in a *json* format, in **suspected_users_by_email.json** file.
####<i class="icon-file"></i>ana_2.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using ```data_dir = os.path.join(current_dir, '..', 'data','enron')```.
> - Used ```os.walk(data_dir)``` to fetch all emails under *enron* dir.
> - Maintained a list of suspected words in stemmed format. 
> - The folders under considerations were having *sent*, *delete* or *inbox* in their names from all people.
> - First fetched the email body from emails, tokanized them using `nltk.word_tokenize` and then removed punctuations, numbers and blank spaces. 
> - Implemented Porter Stemmer using `porter.stem(word)` and then compared words from this list with words from suspected words. If there was a match of any word, added that email into a dictionary with the originator or person the mailbox belonged as key and the email From, email To, email Dat, email ID and email Body as value in a list. Combined all such emails sent received or deleted by originator in dictionary and sorted it by person name.
> - Wrote a function to write this sorted dictionary  into a json file named **suspected_users_by_email.json**
> - The fie is saved in `midterm/question1/ana_2/suspected_users_by_email.json` file

-----------
### Analysis 3
For Analysis 3, I am finding the top 30 most active email users from enron. I am showing the results in a form of a plot and also saving that plot in `midterm/question1/ana_3/most_active_users.png` file. For this analysis I am using all the folders belonging to a certain user.
####<i class="icon-file"></i>ana_3.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using ```data_dir = os.path.join(current_dir, '..', 'data','enron')```.
> - Used ```os.walk(data_dir)``` to fetch all emails under *enron* dir.
> - Saved all the mails from all users into a list and iterated over this list. Used a dictionary to store the details of users as key as user name and value as their occurrence in the email file. If a file doesn't have the name of person, email id is used to gather information.
> - Sorted this dictionary according to the activity or number of emails belonging to a person in reverse order.
> - Plotted a bar chart using `matplotlib ` library showing most active users vs the number of emails they got. Saved this plot in file `midterm/question1/ana_2/most_active_users.png`

-----------
Analysis
------------
### Analysis 1
Analysis 1 is about finding the number of reporters reported a news or an article or a blog,etc on each date. The recent 50 days were plotted on a plot using **`matplotlib`** library. Removed duplicate reporters who have reported 2 or more articles on a same date. I have used data from both *archive* and *articlesearch* APIs, combined them into a single data file as both have same data structure for their responses. The output is stored in a json file format and also saved as *.png* file. 

####<i class="icon-file"></i>ana_1.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using ```data_dir = os.path.join(current_dir, '..', 'data','question2','*','*.json')```.  This gives response from both the API responses. Combine the responses as both have similar data structure and eliminate the duplicate articles present in final dataset.
> - For each article, get the published date and convert it into a datetime object.
> - Get the list of reporters for each article if present. use `try-except` block to handle the errors if any article doesn't have a reporter. Get the first and last name of reporter and store them in a list. 
> - Store the article published date as key and list of all reporters as value in a dictionary. remove the duplicate reporters on a same day, if anyone has reported twice on a same date, he will still be considered as one reporter.
> - Sort the dictionary by date using datetime object as key in reverse order. 
> - Plot a bar chart of date vs number of reporters reported on that date. Also save the dictionary in a json file format at `midterm/question2/ana_1/dates_VS_no_of_reporters.json` and the graph in a png file at `midterm/question2/ana_1/dates_and_no_of_reporters.png` . Plot for the recent 50 days.

-----------
### Analysis 2
For Analysis 2, I am finding all trending keywords and set of 2 such proper nouns which are used adjacent to each in the lead paragraph as trending keywords. I am using `bigrams` to get set of 2 keywords from leading paragraph and using `pos tagging` to get to know if both the words are proper nouns or not. Adding such keywords and proper nouns in a dictionary and sorting it according to its frequency and plotting on a graph and writing to a json file

####<i class="icon-file"></i>ana_2.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using ```data_dir = os.path.join(current_dir, '..', 'data','question2','*','*.json')```.  This gives response from both the API responses. Combine the responses as both have similar data structure and eliminate the duplicate articles present in final dataset.
> - For each article, get the published date and check if the month of published date is not before the last month, in which case break the loop as the response is already sorted date-wise.
> - Get all the keywords from article if any. Use `try-except` block to handle the errors if articles don't have keywords in them.
> - Get the leading paragraph of each article, tokanize it using `nltk.word_tokenize`, consider two words used adjucent to each other using `nltk.bigrams` and check if adjusent keywords are proper nouns using `nltk.pos_tag`. If such adjucent words are proper noun singular or plural, consider them as keywords and add them to list.
> - Create a dictionary using keywords as keys and their occurrence frequency as values and sort this dictionary according to values using `sorted(item_list.items(), key=operator.itemgetter(1), reverse=True)` in reverse order. If the frequency is same, sort the values alphabetically using `sorted(sorted_items_dict, key=lambda val: (-val[1], val[0]))`
> - Write the output in a json file format in `midterm/question2/ana_2/tending_topics_this_and_last_month.json` and the graph in a png file at `midterm/question2/ana_2/tending_topics_this_and_last_month.png`. Plot the top 25 trending keywords on graph


> **P.S.** As you might  have guessed, President Trump is leading the race!

-----------
### Analysis 3
For Analysis 3, I am finding in which month *Donald Trump* or *President Trump* or *President Donald Trump* was trending for the past 6 months. I am using `trigrams` and `bigrams` to get a set of words used in lead paragraph. If the article has used his reference once, don't consider it again. So avoiding duplication of data. Also looking for *Trump, Donald J* as keyword. Save the references in a dictionary with month and year as key and number of references as value. Sort the dictionary using the value and plot on a graph and save as png file

####<i class="icon-file"></i>ana_3.ipynb
> **Logic:**

> - Used relative path to fetch data from the sibling folder of parent folder of current file using ```data_dir = os.path.join(current_dir, '..', 'data','question2','*','*.json')```.  This gives response from both the API responses. Combine the responses as both have similar data structure and eliminate the duplicate articles present in final dataset.
> - For each article, get the published date and find month and year for each article.
> -  Get all the keywords from article if any. Use `try-except` block to handle the errors if articles don't have keywords in them. Find occurrence of `Trump, Donald J` in each article and its date
> - Get the leading paragraph of each article, tokanize it using `nltk.word_tokenize`, consider three words used adjucent to each other using `nltk.trigrams` and match them with *President, Donal, Trump*
> - If the leading paragraph doesn't have the trigram mentioning president, then use `nltk.bigrams` and match *President, Donal* or *President, Trump* or *Donals, Trump* in lead paragraph.
> - Find all such occurrences and add them to a dictionary with month-year as key and frequency of occurrence as value. Sort the dictionary according to value.
> - Plot the graph using `matplotlib` library. Also save the plot in *.png* format in `midterm/question2/ana_3/president_trending_plot.png`