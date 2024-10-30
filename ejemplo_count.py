# -*- coding: utf-8 -*-
"""EJEMPLO_COUNT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kz5xdqWhYTq50ZgEbu104L18pz8M9TQn
"""

from pyspark import SparkContext

sc = SparkContext("local", "Count_ejemplo")

datos = [5, 2, 3, 1, 2]

rdd = sc.parallelize(datos)

cantidad = rdd.count()

print("La cantidad de elementos en el RDD es:", cantidad)