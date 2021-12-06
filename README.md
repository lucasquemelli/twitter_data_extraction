# twitter_data_extraction

<code><img width="100%" src="https://user-images.githubusercontent.com/81119854/144729803-43d738ab-fc1a-4dcb-8c6f-fa085cff82fd.png"></code>

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

Firstly, we must certify that the data source is accessible. To do that, initially, I accessed the [Twitter Developer Platform](https://developer.twitter.com/en) and registered a developer account associated to my personal account (@LucasQuemelli).

Then, we extracted the data using an API free version made available by Twitter. We made some changes to the API and its final version is in *recent_search.py* file. 

The final result may be seen in the screenshot below. Thus, we certified that the data source is accessible. 

![image](https://user-images.githubusercontent.com/81119854/144726941-83933b14-4b3d-4433-8ed3-5ef47210aa25.png)

# 3. Creating a connection

Airflow allows us to interact with data sources and external tools such as Twitter API, databases and cloud services. For each interaction, we need a safe storage local for the data that comes from the connection. It may be user and password for a database or also a token for an API. 

The connection data are saved in the Airflow database. Below, we may see step by step of how to create a connection using Airflow. 

![image](https://user-images.githubusercontent.com/81119854/144848381-47b1035c-a8dc-4eec-a20b-f1b9218ce23e.png)

Notice that the box containing 'token' is not fully displayed. The other part of the box is filled with the bearer token provided by Twitter Developer. 

Next step is to use this connection by a hook.

# 4. Creating a hook

A hook is an interface to communicate DAGs with external sources/tools, such as Twitter API. We use hooks to create methods to interact with a source/tool and also to use connections for authentication. 

The hook created is in the file *twitter_hook.py*. The next step is to use this hook in the operators. 
