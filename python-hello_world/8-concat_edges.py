#!/usr/bin/python3

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str.split(", ")[1].split(" language")[0] + str[90:96] + str[:6])
