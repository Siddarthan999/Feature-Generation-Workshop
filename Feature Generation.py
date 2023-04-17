import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['CarID']=le.fit_transform(df['car_ID'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['Wheelbase']=le.fit_transform(df['wheelbase'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['Carwidth']=le.fit_transform(df['carwidth'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['Enginesize']=le.fit_transform(df['enginesize'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['Carlength']=le.fit_transform(df['carlength'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['Carheight']=le.fit_transform(df['carheight'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
carbody=['convertible','wagon','hatchback','sedan','hardtop']
enc=OrdinalEncoder(categories=[carbody])
enc.fit_transform(df[['carbody']])
df['Carbody']=enc.fit_transform(df[['carbody']])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
enginetype=['dohc','ohc','ohcv']
enc=OrdinalEncoder(categories=[enginetype])
enc.fit_transform(df[['enginetype']])
df['Enginetype']=enc.fit_transform(df[['enginetype']])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
fuelsystem=['mpfi','mfi','1bbl','2bbl','idi']
enc=OrdinalEncoder(categories=[fuelsystem])
enc.fit_transform(df[['fuelsystem']])
df['Fuelsystem']=enc.fit_transform(df[['fuelsystem']])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['Carname']=le.fit_transform(df['CarName'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
le=LabelEncoder()
df['Carbody']=le.fit_transform(df['carbody'])
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
ohe=OneHotEncoder(sparse=False)
enc=pd.DataFrame(ohe.fit_transform(df[['carbody']]))
df=pd.concat([df,enc],axis=1)
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
ohe=OneHotEncoder(sparse=False)
enc=pd.DataFrame(ohe.fit_transform(df[['fuelsystem']]))
df=pd.concat([df,enc],axis=1)
df

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
ohe=OneHotEncoder(sparse=False)
enc=pd.DataFrame(ohe.fit_transform(df[['enginetype']]))
df=pd.concat([df,enc],axis=1)
df

import pandas as pd
import seaborn as sns
!pip install category_encoders
from category_encoders import BinaryEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
be=BinaryEncoder()
newdata=be.fit_transform(df['fueltype'])
df1=pd.concat([df,newdata],axis=1)
df1

import pandas as pd
import seaborn as sns
!pip install category_encoders
from category_encoders import BinaryEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
be=BinaryEncoder()
newdata=be.fit_transform(df['aspiration'])
df1=pd.concat([df,newdata],axis=1)
df1

import pandas as pd
import seaborn as sns
!pip install category_encoders
from category_encoders import BinaryEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
be=BinaryEncoder()
newdata=be.fit_transform(df['doornumber'])
df1=pd.concat([df,newdata],axis=1)
df1

import pandas as pd
import seaborn as sns
!pip install category_encoders
from category_encoders import BinaryEncoder
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("Workshop_feature Engg.csv.xlsx")
be=BinaryEncoder()
newdata=be.fit_transform(df['drivewheel'])
df1=pd.concat([df,newdata],axis=1)
df1
