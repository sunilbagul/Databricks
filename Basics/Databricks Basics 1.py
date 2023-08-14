# Databricks notebook source
print("hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "hello databricks"

# COMMAND ----------

# MAGIC %md
# MAGIC #title
# MAGIC ## tile2
# MAGIC

# COMMAND ----------

# MAGIC %run /DBTraining/DBB2

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls dbfs:/databricks-datasets

# COMMAND ----------

files = dbutils.fs.ls('dbfs:/databricks-datasets')
print(files)

# COMMAND ----------

display(files)
