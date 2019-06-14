import csv
from random import randrange

with open("datasets.csv", "r") as datasets_file:
	datasets = datasets_file.readlines()
	num_datasets = len(datasets)
	random_int = randrange()
