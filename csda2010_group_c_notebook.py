import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neural_network import MLPClassifier
import scipy.stats as st
from mlxtend.frequent_patterns import apriori, association_rules


from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split



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

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

file_id = '1ZmcgqcQZh_t9Sfiy8DkG9kAsZzRCP1Gj'
downloaded = drive.CreateFile({'id': file_id})

downloaded.GetContentFile('file.csv')

mbadf = pd.read_csv('file.csv', delimiter=';')


mbadf.head()

mbadf.keys()


mbadf.info()


mbadf.Date = pd.to_datetime(mbadf.Date)
mbadf.info()

mbadf.shape



mbadf.describe()



mbadf.isna().sum()

mbadf.dropna(inplace=True)


mbadf = mbadf[mbadf['Quantity'] > 0]

mbadf['Price'] = pd.to_numeric(mbadf['Price'], errors='coerce')
mbadf = mbadf[mbadf['Price'] > 0]

mbadf.shape

mbadf.isna().sum()

mbadf.dtypes




mbadf['Itemname'].value_counts().head(15)

color = plt.cm.rainbow(np.linspace(0, 1, 40))
mbadf['Itemname'].value_counts().head(15).plot.bar(color = color, figsize=(13,5))
plt.title('Frequency of most popular items', fontsize = 20)
plt.xticks(rotation = 90 )
plt.grid()
plt.show()



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

sales_per_customer = sales.groupby(['CustomerID', 'Country']).agg({"Total_Price": "sum"})
sales_per_customer.head(10)

sales_per_Itemname = sales.groupby(['Itemname', 'Country']).agg({"Total_Price": "sum"})
sales_per_Itemname.head(10)
sales_per_Itemname.sort_values("Total_Price", ascending=False)





df_invoice_product_matrix = mbadf.groupby(['BillNo', 'Itemname']) \
  ['Quantity'].sum().unstack().fillna(0). \
  applymap(lambda x: 1 if x > 0 else 0)

df_invoice_product_matrix.head(10)

frequent_itemsets = apriori(df_invoice_product_matrix, min_support=0.001, max_len=2, use_colnames=True) 
frequent_itemsets.sort_values("support", ascending=False)

frequent_itemsets.shape

rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.001)
rules.sort_values("support", ascending=False).head(10)

rules.shape


rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
rules.sort_values("confidence", ascending=False).head(10)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=400)
rules.sort_values("lift", ascending=False).head(10)

rules.shape





sorted_rules = rules.sort_values("lift", ascending=False)
rules.sort_values("lift", ascending=False)

rules.shape




recommendation_list = []

for i, product in sorted_rules['antecedents'].items():
    for j in list(product):
        if j == ('DOORMAT HOME SWEET HOME BLUE'):
            recommendation_list.append(list(sorted_rules.iloc[i]['consequents']))

recommendation_list

