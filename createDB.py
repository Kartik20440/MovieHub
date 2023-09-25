import pandas as pd
import os

path = "data/imdb/"

# # for all files in data_dir convert to csv
# for file in os.listdir(path):
#     if file.endswith(".xlsx"):
#         df = pd.read_excel(path + file)
#         df.to_csv(path + file[:-5] + ".tsv", index=False, sep="\t")


# for all files in data_dir convert gz file to csv
for file in os.listdir(path):
    if file.endswith(".gz"):
        df = pd.read_csv(path + file, compression='gzip')
        df.to_csv(path + file[:-3] + ".tsv", index=False, sep="\t")
        print("done")

