# Working with Managed No-SQL Databases

NOTE: For reflection, talk about what was similar, dissimilar, pain points, did you need to do anything to the data to make it play nicely, etc. That sort of stuff.

## 1. Database Creation and Configuration
### Google BigQuery (GCP):
1. On BigQuery's default page, click "+Add" and then "Local file"
![Navigation to upload dataset file](img/gcp/bigquery/upload_file_link.png)
2. The following were done:
    * Select file: (browse and upload your csv file)
    * File format: CSV
    * Table: (a name related to what the CSV file about)
    * Auto detect: checked
3. Click the "Dataset" box and click "Create New Dataset." These configurations were applied:
    * Dataset ID: (enter some name)
    * Location type: Region
    * Region: (closest region to you)
4. Create the dataset, then create the table
![Table creation process with dataset](img/gcp/bigquery/create_table.png)

### MongoDB Atlas (Cloud):
1. Click your cluster
![Page showing list of cluster](img/mongodb/click_cluster.png)
2. Click the "Collection," then "+ Create Database"
![Specific cluster's page](img/mongodb/create_db.png)
    * Name the database and collection (aka table), then create it
![Create database box](img/mongodb/create_db_config.png)

## 2. Explore BigQuery (GCP)
1. The following query was ran:
```sql
SELECT * 
FROM `danny-chen-hha504.patient_info.patient_info` 
WHERE age > 40 AND hospital = "Stony Brook Hospital";
```
2. Results:
![Query results](img/gcp/bigquery/query_results.png)
3. The usage and cost of a query can be found by either:
    * clicking "Job Information" to view details about the current query
    * opening the job history to view info on all previously run queries.
![Viewing query usage and cost](img/gcp/bigquery/query_usage_cost.png)

## 3. Modify and Explore the Data in MongoDB Atlas and Redis Cloud
### MongoDB Atlas (Cloud):