# -*- coding: utf-8 -*-
"""ejemploMAP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jYqDc8ZRSTY3QBREdN-ciZI9CQ0GKtSz
"""

from pyspark import SparkContext

sc = SparkContext ("local","Reduce_ejemplo")

datos = [2,3,4,5,6]

rdd = sc.parallelize(datos)

suma_resultado = rdd.reduce(lambda x, y: x + y)

print ("la suma es: ", suma_resultado)