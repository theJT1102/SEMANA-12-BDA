# -*- coding: utf-8 -*-
"""coalesce .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mJpqVxevOfjZFSn7oUQG7JmaSVRKdWdg
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Ejemplo RDD").getOrCreate()

sc = spark.sparkContext

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rdd_numeros = sc.parallelize(numeros, numSlices=4)

print("Número de particiones antes de coalesce:", rdd_numeros.getNumPartitions())

rdd_coalescido = rdd_numeros.coalesce(2)

print("Número de particiones después de coalesce:", rdd_coalescido.getNumPartitions())