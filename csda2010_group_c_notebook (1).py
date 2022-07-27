import streamlit as st



# -*- coding: utf-8 -*-
"""CSDA2010 GROUP C Notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_NgrS9gqtFYcwlSoZXMlzcMIw3i0A-lO

# THIS IS OUR <span style="color:red;"> CSDA2010 GROUP C </span>  NOTEBOOK

## For our Project #1 - Market Basket Analysis

**References include:- Example from course notes**

 *We use listing-level data of Airbnb properties that were available on the platform from January to
December 2012. The data was acquired from InsideAirbnb.com, an independent service that provides
data on several cities. Our data consists of London rentals. For each listing, we have data on its price,
days available, number of ratings as well as the text description of the property. We also have data for
each review, including the reviewer, the listing, the review score, and the text of the review. We merged
this data with other social and demographic measures obtained from gov.uk, including quality of
nearby school ratings and local crime rates. See Appendix Table 1 for a list and description of variables
used in our analysis.
We performed some transformation of variables to account for missing and skewed data. First, we
use the natural log of price and number of ratings. Some observations had missing crime data. For
those observations, we substituted the mean crime rate of the neighboring regions.
After dropping 1,425 observations because of missing or erroneous location information, we have
42,195 listings that were used in our analysis. Table 1 presents summary statistics for the variables and
Table 2 presents a correlation matrix. The mean price of a listing in our dataset is 5.05 log pounds and
the mean number of ratings (logged) is 1.56.*.

We can colaborate in this notebook.

# SET UP
"""

!pip install --upgrade gspread

"""## Import Data from Google Sheets"""

# Install the latest version of pandas profiling
!pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

"""## Load required libraries"""

# Commented out IPython magic to ensure Python compatibility.
# Import the required packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
import scipy.stats as st
from mlxtend.frequent_patterns import apriori, association_rules


# From sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
# %matplotlib inline

# additional libraries to analyze text
from IPython.display import display
from bokeh.io import output_notebook
from bokeh.models import Label
from bokeh.plotting import figure, output_file, show
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import linear_kernel
from textblob import TextBlob
from tqdm import tqdm
import ast
import matplotlib.mlab as mlab
import nltk
import numpy as np
import re
import scipy.stats as stats
from scipy.sparse import csr_matrix, csc_matrix
from scipy import sparse
import seaborn as sb
import spacy
import string
output_notebook()
pd.options.mode.chained_assignment = None



"""## Load Dataset

For our study, we used a dataset from Kaggle -----------.
This dataset consists of -------------------------------.

File is located on Google Drive here → 
https://drive.google.com/file/d/1ZmcgqcQZh_t9Sfiy8DkG9kAsZzRCP1Gj/view?usp=sharing

### Source:
https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis


Dr Daqing Chen, Director: Public Analytics group. chend '@' lsbu.ac.uk, School of Engineering, London South Bank University, London SE1 0AA, UK.


### Data Set Information:
This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.The company mainly sells unique all-occasion gifts. 

### Attribute Information:
* BillNo: 6-digit number assigned to each transaction. Nominal.
* Itemname: Product name. Nominal.
* Quantity: The quantities of each product per transaction. Numeric.
* Date: The day and time when each transaction was generated. Numeric.
* Price: Product price. Numeric.
* CustomerID: 5-digit number assigned to each customer. Nominal.
* Country: Name of the country where each customer resides. Nominal.
* Total_Price: Transaction total. Numeric.

**NOTE - To load the dataset. Run code below**
"""

# Import PyDrive and associated libraries.
# This only needs to be done once per notebook.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
# This only needs to be done once per notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# Download a file based on its file ID.
#
# A file ID looks like: laggVyWshwcyP6kEI-y_W3P8D26sz
file_id = '1ZmcgqcQZh_t9Sfiy8DkG9kAsZzRCP1Gj'
downloaded = drive.CreateFile({'id': file_id})
# 
downloaded.GetContentFile('file.csv')

mbadf = pd.read_csv('file.csv', delimiter=';')

"""## Review the Data"""

mbadf.head()

# To find out what sort of detail is provided with this dataset, we can call .keys()
mbadf.keys()

# What info are included in the dataset
mbadf.info()

# convert Date column into correct datatype
mbadf.Date = pd.to_datetime(mbadf.Date)
mbadf.info()

mbadf.shape



mbadf.describe()

"""## For each numerical feature, we can see the **`count`**, or number of data entries, the **`mean`** value, and the **`standard deviation`**, **`min`**, **`max`** and **`quartile`** values. 



"""

# check for blank or missing values
mbadf.isna().sum()

# drop NA values
mbadf.dropna(inplace=True)

# quantity and price should be greater than 0
mbadf = mbadf[mbadf['Quantity'] > 0]

# change the price column datatype as a numeric
mbadf['Price'] = pd.to_numeric(mbadf['Price'], errors='coerce')
mbadf = mbadf[mbadf['Price'] > 0]

mbadf.shape

mbadf.isna().sum()

mbadf.dtypes

"""# EDA & VISUALIZATIONS

## Should we try adding some visualizations? 
**Perhaps a bar chart of the top 10-15 most popular items?**
"""

mbadf['Itemname'].value_counts().head(15)

color = plt.cm.rainbow(np.linspace(0, 1, 40))
mbadf['Itemname'].value_counts().head(15).plot.bar(color = color, figsize=(13,5))
plt.title('Frequency of most popular items', fontsize = 20)
plt.xticks(rotation = 90 )
plt.grid()
plt.show()

"""**"POSTAGE"** seems to be an outlier. We will drop the rows that have the "POSTAGE" item."""

mbadf.drop(mbadf[mbadf.Itemname=='POSTAGE'].index, inplace=True)

mbadf['Itemname'].value_counts().head(15)

mbadf['Itemname'].value_counts()

mbadf.shape

color = plt.cm.rainbow(np.linspace(0, 1, 40))
mbadf['Itemname'].value_counts().head(15).plot.bar(color = color, figsize=(13,5))
plt.title('Top 15 most popular items(POSTAGE removed)', fontsize = 20)
plt.xticks(rotation = 90 )
plt.grid()
plt.show()

sales = mbadf
sales['Total_Price'] = sales['Price'] * sales['Quantity']
# sales.columns
sales_per_customer = sales.groupby(['CustomerID', 'Country']).agg({"Total_Price": "sum"})
sales_per_customer.head(10)

sales_per_Itemname = sales.groupby(['Itemname', 'Country']).agg({"Total_Price": "sum"})
sales_per_Itemname.head(10)
sales_per_Itemname.sort_values("Total_Price", ascending=False)



"""** Filter out the Credit/Cancellation transactions. (BillNo starting with **C**)

** Consider filter by one country's transactions only.

# PREPROCESSING
"""



"""Process our data to make it suitable for the algorithm.

###Do we need to do any further cleaning of the dataset.
* *Remove the rows that have cancelled transactions BillNo that start with letter 'c' indicates a cancellation **
"""



"""## Parse the items in each Basketgroup by Bill Number and encode values.

# Invoice Product Matrix (Basket sets)
"""

df_invoice_product_matrix = mbadf.groupby(['BillNo', 'Itemname']) \
  ['Quantity'].sum().unstack().fillna(0). \
  applymap(lambda x: 1 if x > 0 else 0)

df_invoice_product_matrix.head(10)

"""# ASSOCIATION RULES LEARNING

We should consider setting the minimum support to **0.001%**.
"""

frequent_itemsets = apriori(df_invoice_product_matrix, min_support=0.001, max_len=2, use_colnames=True) 
frequent_itemsets.sort_values("support", ascending=False)

frequent_itemsets.shape

"""From the results above, we have 1077 frequent item combinations

## Generate the Rules for Support, Confidence and Lift
* The **support** metric measures the share of transactions that contain an itemset.
* **Confidence** and **Lift** when suport is misleading.
"""

rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.001)
rules.sort_values("support", ascending=False).head(10)

rules.shape

"""### Get rules from Apriori with confidence of 10%."""

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
rules.sort_values("confidence", ascending=False).head(10)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=400)
rules.sort_values("lift", ascending=False).head(10)

rules.shape

"""##	Lift provides another metric for evaluating the relationship between items.
**Numerator:** Proportion of transactions that contain Xx and Yy.

**Denominator:** Proportion if Xx and Yy are assigned randomly and independently to transactions.

"""

sorted_rules = rules.sort_values("lift", ascending=False)
rules.sort_values("lift", ascending=False)

rules.shape

"""### What pair of items are frequently bought together?
DOOR MAT UNION JACK GUNS AND ROSES and DOORMAT HOME SWEET HOME BLUE

### What recommendations should we suggest for pricing and promotion items?

### We can build a recommendation engine to recomend DOOR MAT UNION JACK GUNS AND ROSES to customers who purchase DOORMAT HOME SWEET HOME BLUE (first rule).
"""

recommendation_list = []

for i, product in sorted_rules['antecedents'].items():
    for j in list(product):
        if j == ('DOORMAT HOME SWEET HOME BLUE'):
            recommendation_list.append(list(sorted_rules.iloc[i]['consequents']))

recommendation_list

