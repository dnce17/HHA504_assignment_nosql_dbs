# Working with Managed No-SQL Databases

## 1. Database Creation and Configuration
### BigQuery
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