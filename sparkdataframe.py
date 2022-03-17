
from pyspark import SparkContext
from pyspark.sql import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession.builder.appName('PySpark DataFrame From RDD').getOrCreate()
rdd = sc.parallelize([('C',85,76,87,91), ('B',85,76,87,91), ("A", 85,78,96,92), ("A", 92,76,89,96)], 4)
sub = ['Division','English','Mathematics','Physics','Chemistry']
marks_df = spark.createDataFrame(rdd, schema=sub)
marks_df.printSchema()
marks_df.show()

csv_file = spark.read.csv('Fish.csv', sep = ',', inferSchema = True, header = True)
txt_file = spark.read.text("example.txt")
json_file = spark.read.json("sample.json", multiLine=True)