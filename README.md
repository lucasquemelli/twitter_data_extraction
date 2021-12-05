# twitter_data_extraction
# 1. Problem Description

In this project, we created a **pipeline** using **Apache Airflow** to extract data from **Twitter** in order to analyze their **interactions**.

The main idea of this project is to extract data from Twitter, such as tweets, retweets and likes. The purpose of extracting the data is to create an interaction analysis using Machine Learning to evaluate how positive are the tweets involving @AluraOnline on Twitter. 

Alura is a Brazilian educational platform about technology. For further information about Alura, access their website: [Alura.](https://www.alura.com.br
)

As a solution, we proposed:
- Coding in Python.
- Export data to a JSON file. 
- Put the file in a database.

Additionally, as we want to load more and more data, we must match the following requirements:

1. **Scaling up:** addition of more intelligence (processing power) and memory (storage capacity) to deal with big data.
2. **Automation:** a platform which allows the automation of each work.
3. **Monitoring:** work monitoring, logs manegement, and warnings.
4. **Maintenance:** low maintenance need and short period of time spent on tasks. 
5. **Expansion:** ready-to-expand to further data sources such as other Twitter or Facebook accounts, and also other databases or files. 
6. **Integration:** a platform which allows the integration of new members to the data engineers team as it increases. 

In order to match the requirements above, Apache Airflow was chosen to perform the tasks. 

# 2. Connecting to Twitter

Firstly, we must certify that the data source is accessible. Thus, I accessed the [Twitter Developer Platform](https://developer.twitter.com/en) and registered a developer account associated to my personal account (@LucasQuemelli).

Then, we extracted the data using an API free version made available by Twitter. We made some changes to the API and its final version is in *recent_search.py* file. 

![image](https://user-images.githubusercontent.com/81119854/144726941-83933b14-4b3d-4433-8ed3-5ef47210aa25.png)

