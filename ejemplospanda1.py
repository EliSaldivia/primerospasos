#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[ ]:





# In[2]:


s = pd.Series([1, 3, 5, np.nan, 6, 8]) # crea una serie de datos pasando una lista de valores, permitiendo q cree un índice entero predeterminado
s


# In[15]:


dates = pd.date_range("20221002", periods=10) #crea un dataframe pasando una arreglo numpy con un seriado temporal
dates


# In[16]:


df = pd.DataFrame(np.random.randn(10, 3), index=dates, columns=list("cat"))
df


# In[17]:


df2 = pd.DataFrame(

    {

        "A": 1.0,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

) #asigna a cada columna un tipo de objeto difrente

df2


# In[18]:


df2.dtypes


# In[19]:


df.dtypes # reconoce que tipo de objeto hay en cada columna


# In[21]:


df.head(2) #muestra los () primeros renglones del frame


# In[22]:


df.tail(5) #muestra los () ultimos renglones del frame


# In[23]:


df.index #muestra los indices del frame


# In[24]:


df.columns #muestra las columnas del frame


# In[25]:


df.to_numpy()


# In[26]:


df2.to_numpy()


# In[27]:


df.describe() #muestra las estadisticas rapidas de los datos


# In[28]:


df.T


# In[30]:


df.sort_index(axis=1, ascending=False)


# In[33]:


df.sort_values(by="a")


# In[34]:


df.sort_values(by="t") #ordena los elemntos dela columna ""


# In[36]:


df["a"] ##selecciona la columna ""


# In[37]:


df[0:5] #muestra los renglones dentro de las llaves


# In[38]:


df["20221006":"20221009"]


# In[41]:


df.loc[dates[2]]# selecciona el renglon [dates] de la tabla


# In[42]:


df.loc[:, ["t", "a"]]


# In[44]:


df.loc["20221002":"20221004", ["c", "t"]]


# In[45]:


df.loc["20221003", ["c", "t"]]


# In[46]:


df.loc[dates[0], "a"] #me arroja el escalar ubicado en la columna a renglon 0


# In[47]:


df.iloc[3] #muestra los valores del renglon 3


# In[48]:


df.iloc[3:5, 0:2]


# In[61]:


df.iloc[[0,6], [0,1]] #me muestra los datos de los renglones [*,*], de las columnas en el intervalo de 0 al 2


# In[56]:


arr = np.array(df) #me da el tamaño del arreglo 

print(np.shape(arr))


# In[62]:


df.iloc[1:3, :] #me muestra los renglones 1 y3 de todas las columnas


# In[63]:


df.iloc[1, 1] # me arroja el elmento 1,1 del arreglo


# In[64]:


df[df["c"] > 0] #me muestra los valores mayores que cero de la columna c y las demas los deja igual


# In[67]:


df[df > 0] #muestra solo los valores mayores que cero 


# In[68]:


df2=df.copy()
df2["a"]=["cat1", "cocosas", "jose", "Antonia", "nené", "pilla", "teresito", "princesa", "sandro", "silvio"]
df2 #sustituye los valores de lla columna "a"


# In[72]:


df2[df2["a"].isin(["nené", "sandro"])] #devuelve la serie booleana q coincide con los elemntos nombrados


# In[90]:


s1= pd.Series(["cat1", "cocosas", "jose", "Antonia", "nené", "pilla", "teresito", "princesa", "sandro", "silvio"], index=pd.date_range("20220102", periods=10))
s1 # coloca una nueva columna y aliena los datos  por indices
df["s"]=s1
df


# In[85]:


df


# In[86]:


df.at[dates[0], "a"] = 0 # cambia las entradas por etiqueta


# In[87]:


df.iat[0, 1] = 0 # cambia la entrada por posicion


# In[100]:


df.loc[:, "D"] = np.array([20] * len(df))


# In[101]:


df


# In[45]:


df4=pd.read_csv(r"http://www2.ssn.unam.mx:8080/catalogo/csv/20221115160620HIRPN.csv", skiprows=4, skipfooter=7,parse_dates=["Fecha"],engine='python')
df4


# In[9]:


df4.describe()


# In[10]:


df4.min()


# In[11]:


df4.max()


# In[12]:


import matplotlib.pyplot as plt


# In[13]:


df4.columns


# In[14]:


plt.bar(df4['Fecha'], df4['Magnitud'])


# In[40]:


pd.to_datetime(df4['Fecha'])


# In[35]:


#hacer un filtro de fechas
filtered_df4 = df4.loc[(df4['Fecha'] >= '2022-01-01')
                     & (df4['Fecha'] <= '2022-12-31')]

print(len(filtered_df4))
filtered_df4


# In[72]:


df4['Fecha']
f2022 = df4.loc[df4['Fecha'].dt.year == 2022]
f2021 = df4.loc[df4['Fecha'].dt.year == 2021]
f2020 = df4.loc[df4['Fecha'].dt.year == 2020]
f2019 = df4.loc[df4['Fecha'].dt.year == 2019]
f2018 = df4.loc[df4['Fecha'].dt.year == 2018]
len(f2022), len(f2021), len(f2020), len(f2019), len(f2018)


# In[73]:


f2020.max()


# In[ ]:




