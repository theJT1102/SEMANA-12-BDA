# -*- coding: utf-8 -*-
"""max, min.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DeOUXDeCvJ6hqzoLyvrWNk9YsrXswuuZ
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Ejemplo RDD").getOrCreate()

sc = spark.sparkContext

numeros = [1, 5, 3, 9, 2, 8, 4, 10, 7, 6]

rdd_numeros = sc.parallelize(numeros)

valor_maximo = rdd_numeros.max()

valor_minimo = rdd_numeros.min()

print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)