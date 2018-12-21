# Example 2-7. Initializing Spark in Python
# from terminal: bin\spark-submit ..\Documents\python_test_private\test_spark\PythonSpark.py

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")

sc = SparkContext(conf = conf)

lines = sc.textFile("README.md")

print(lines.first())

pythonLines = lines.filter(lambda line: "Python" in line)
print(pythonLines.first())

print(lines.count()) 

sc.stop()
