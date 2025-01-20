# import pandas library
import pandas as pd
import numpy as np

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

file_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

#To obtain the dataset, utilize the download() function as defined above:
await download(file_path, "auto.csv")
file_name="auto.csv"

#Utilize the Pandas method read_csv() to load the data into a dataframe.
df = pd.read_csv(file_name)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
df.head(5)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

#Replace headers and recheck our data frame:
df.columns = headers
df.columns

#Now, we need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df1=df.replace('?',np.NaN)

#You can drop missing values along the column "price" as follows:
df=df1.dropna(subset=["price"], axis=0)
df.head(20)
    #Here, axis=0 means that the contents along the entire row will be dropped wherever the entity 'price' is found to be NaN
    #Now, you have successfully read the raw data set and added the correct headers into the data frame.

#Save Dataset
df.to_csv("automobile.csv", index=False)
