# twitter_data_extraction

<code><img width="100%" src="https://user-images.githubusercontent.com/81119854/144729803-43d738ab-fc1a-4dcb-8c6f-fa085cff82fd.png"></code>

# 1. Problem Description

In this project, we created a **pipeline** using **Apache Airflow** to extract data from **Twitter** and hence **Apache Spark** to transform the data. The purpose was to analyze Twitter user **interactions**. The chosen pipeline was **ELT** format, since we want to save raw data before transforming them - to avoid errors.

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

Then, we extracted the data using an API free version made available by Twitter. We made some changes to the API and its final version is in [*recent_search.py*](https://github.com/lucasquemelli/twitter_data_extraction/blob/main/recent_search.py) file. 

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

The hook created is in the file [*twitter_hook.py*](https://github.com/lucasquemelli/twitter_data_extraction/blob/main/Airflow/twitter_hook.py). The next step is to use this hook in the operators. 

# 5. Creating operators connected to hooks and exporting them to a Data Lake

Each step in a DAG is executed by an operator. After execute a task by an operator, we must store the data we created. We did not use a database, since to work with big data we have to consider Volume, Velocity and Variety. 

A commom database would not match theses requirements. Therefore, we created a Data Lake. Data Lake is a distributed file system which uses distributed tools to store and process data. 

The [operator](https://github.com/lucasquemelli/twitter_data_extraction/blob/main/Airflow/twitter_operator.py) and the [Data Lake](https://github.com/lucasquemelli/twitter_data_extraction/tree/main/datalake/twitter_aluraonline) - for two days - created may be accessed by the links. 

# 6. Creating plugins

To store the classes we used in this project, we created plugins. All classes we used may be imported from operators. 

The plugins are found in the file [*airflow_plugin.py*](https://github.com/lucasquemelli/twitter_data_extraction/blob/main/Airflow/airflow_plugin.py). In order to test the plugins, we created a [DAG](https://github.com/lucasquemelli/twitter_data_extraction/blob/main/Airflow/twitter_dag.py) and we added the operators into it. 

The DAG was successfully added into Airflow DAGs. It is the last DAG in the image below:

![image](https://user-images.githubusercontent.com/81119854/145033482-61fdf6f1-ad91-4c3d-a67b-5796634dcdbb.png)

The details of the DAG may be seen as follows:

![image](https://user-images.githubusercontent.com/81119854/145033627-59167ab8-926d-4505-8eaf-f555ca7770d2.png)

The next step is to transform the data using Apache Spark. 

# 7. Reading raw data from the Data Lake

Apache Spark is a tool that allows distributed processing in hundreds of computers or also only one. Using Spark, we may access the data lake we created and read the tables as databases.

Dataframe schema may be seen below, where **(1) |-- data:** tweet informations; **(2) |-- includes:** user informations; **(3) |-- meta:** informations about each printed page; **(4) |--** extract_date: extraction dates. 

![image](https://user-images.githubusercontent.com/81119854/145113912-25f90c7c-84c2-4809-8e27-977fbca225e8.png)

Dataframe lines - df.show() - may be seen below:

![image](https://user-images.githubusercontent.com/81119854/145115449-33d97fd9-5100-4c1a-8c16-a11d30b09685.png)

# 8. Transforming and exporting data to the Data Lake

Firstly, we read the path file:

![image](https://user-images.githubusercontent.com/81119854/145580437-eb99163d-c40e-43a8-a099-817d93f6f66e.png)

Thus, we could see that the dataframe is not in the flat format:

![image](https://user-images.githubusercontent.com/81119854/145580671-ed44a0ba-0a6d-4e53-b372-b5b11d46c4a7.png)

Then, we transformed the "data" field to the flat format by exploding it:

![image](https://user-images.githubusercontent.com/81119854/145581540-dd867dc7-5ad1-40cb-81c3-8fde4094b6a7.png)

Finally, we wrote the transformed "data" field (tweet_df) to the Data Lake choosing a csv format and creating a new folder named "export":

![image](https://user-images.githubusercontent.com/81119854/145582846-63624148-37ee-49a6-9868-b00dd44c5da4.png)

We wrote a file without headers. But if we want a file with headers instead, we may do:

![image](https://user-images.githubusercontent.com/81119854/145611826-2f0f9e30-5e39-4b03-b528-cb0c833fcd03.png)

The result of the commands above (up to line 20) is below:

![image](https://user-images.githubusercontent.com/81119854/145612017-70f9c654-5fba-4b43-9e22-67c021b6a67c.png)

2 or more partitions may be done if we export a too large file. To know how many partitions will be done before exporting the file, we may use:

![image](https://user-images.githubusercontent.com/81119854/145612644-4a724e98-827e-468c-af0e-aa1db822fe61.png)

By the image above, we concluded that only 1 file was generated. Yet, if we wish to make repartitions, we may use the *repartition* function and add into it the number of repartitions.

![image](https://user-images.githubusercontent.com/81119854/145619015-9a37660d-2f9e-4d7d-9019-1a5169220757.png)

If we want to join partitions into larger file (s), we may use the *coalesce* function, by doing this:

![image](https://user-images.githubusercontent.com/81119854/145620344-26309b4e-9861-4d13-9aaa-2d74bc042f1b.png)

Exported partitions influence when the files are read once again. To export files with partitions, we need to find the field that will result in a good cardinality - which means low number of groups and low amount of lines for each group.

Because of that, we may not choose the "id" field, since there is a unique id for each tweet. Therefore, we chose the "created_at" field. Thus, to test the group cardinality, we converted timestamp to date, grouped the results by creation date, counted the number of elements per creation date and displayed the selection:

![image](https://user-images.githubusercontent.com/81119854/145626843-5fe15722-2f15-41fd-937c-f96c9acbd384.png)

From the image above, we may notice that the minimum number of lines is 4 and the maximum is 48. That represents a good cardinality. So we must go on and export these files. 

In order to export the files, we created a new dataframe named *export_df*, a new column named *creation_date* using *withColumn* function, and a new file for each partition - which is the number of creation dates. Then, we created one folder for each creation date by using *partitionBy* and saved the files in json:

![image](https://user-images.githubusercontent.com/81119854/145652989-76501f3a-7684-433f-943f-65f248508227.png)

The result of the commands above is:

![image](https://user-images.githubusercontent.com/81119854/145653023-3b03b7a5-c92c-4531-aec6-ca43c37be1e5.png)

To assure that we will have a good reading when read it back, we filtered by partition field and created a excution plan (*explain* function) to spark seek for the data:

![image](https://user-images.githubusercontent.com/81119854/145681322-0baaca26-922a-4872-b078-f0b5c06e797f.png)

In the image above, PartitionFilters displays what Spark will do in order to perform a faster reading. It will use "creation_date" (the partition field we selected) to filter the data that will be read.  

It means Spark will not go through each partition to filter the data, it will just go through the partition we chose. Much less data will be read and the dataframe will be created much faster. 

When we export data, we must assure that we are using partitions that will be able to be filtered in order to meake easier the dataframe reading. 

Finally, we created the *Medallion* to make the reading easier. Bronze is the folder with the raw data, silver contains the transformed data, and gold has the ready-to-use data - those data used to formulate researches. 

![image](https://user-images.githubusercontent.com/81119854/145682128-b87b56c0-045f-4521-9b4a-c2444fee57ec.png)

The next step is to execute our project using Spark and store it on the Airflow. 

# 9. Creating work transformation using Spark

This version of the file [*transformation.py*](https://github.com/lucasquemelli/twitter_data_extraction/blob/main/Spark/transformation.py) may be accessed by the link. The transformation may be confirmed by the creation of the folders required in Spark:

![image](https://user-images.githubusercontent.com/81119854/145690075-57d6e0da-d60a-4114-bd44-d87a603bf3ba.png)

![image](https://user-images.githubusercontent.com/81119854/145690085-683325e9-049e-4cd5-8979-36e7c41b0f7d.png)

# 10. Connecting Spark to Airflow

To insert the transformed data by Spark into Airflow, we used the commands found in [*twitter_dag_second_version.py*](https://github.com/lucasquemelli/twitter_data_extraction/blob/main/Airflow/twitter_dag_second_version.py). A screenshot containing the added operator to the DAG is below:

![image](https://user-images.githubusercontent.com/81119854/145823961-a4ad8ff3-02f6-4ed9-a5e2-f004cd62462e.png)

We also needed to change the Spark connection. In *spark_default*, we did:

![image](https://user-images.githubusercontent.com/81119854/145826306-ecb85a97-181a-4864-85fb-80376dd43898.png)

In the field "Extra" above, we added the Spark folder path. 

Then, we tested the task. Using "airflow dags list" command, we found the list of dags:

![image](https://user-images.githubusercontent.com/81119854/145828678-371d0fdd-5238-42d2-a42f-f97ee07ed725.png)

The last one is *twitter_dag*, the one we used. To know the tasks of *twitter_dag*, we used "airflow tasks list twitter_dag" command:

![image](https://user-images.githubusercontent.com/81119854/145828786-ac894b18-8553-49f3-93ee-19d61d8c016a.png)

We found two tasks: (1) transformation_twitter_aluraonline and (2) twitter_aluraonline. We tested the first task by doing:

![image](https://user-images.githubusercontent.com/81119854/145829565-a23c15e4-fe5d-4e6e-9ed7-3680130cac74.png)

Finally, we obtained in transformed data folder (silver) a new folder with the "process_date" we chose/worked:

![image](https://user-images.githubusercontent.com/81119854/145829680-abc1be74-9b8d-44df-b1b1-2227f6c54313.png)

That means the automation process to transform data was successfully performed. Now, we may conclude our DAG. 

# 11. DAG settings

In this section, we **(1)** connected the operators and **(2)** had set the DAG execution frequency. 

The operators were not connected. This means they only would be executed in parallel. Yet, they must be connected to extract and export the data to the bronze folder and then transforming and exporting the data to the silver folder.

In the twitter dag final version ([*twitter_dag_third_version.py*]()) file, they are already connected. The Graph and the Tree View of the DAG is below:

![image](https://user-images.githubusercontent.com/81119854/145858981-53191b16-eaf7-4e65-934c-d19080fb7347.png)
![image](https://user-images.githubusercontent.com/81119854/145859029-c581dae0-de92-403c-b138-8937b18aa80f.png)




