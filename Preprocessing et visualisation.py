#!/usr/bin/env python
# coding: utf-8

# # Importation des bibiothèques

# In[94]:


import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px


# # importation de la data

# In[96]:


data=pd.read_csv("data.csv", sep=';',decimal=",")


# # Exploration de la data

# In[97]:


data.shape


# In[98]:


data.head()


# In[99]:


data.describe(include='all')


# In[100]:


#détection des valeurs manquantes au niveau de la matrice des données 
sns.heatmap(data.isna())


# In[101]:


#nombre de valeur manquantes par colonne
data.isnull().sum()


# In[146]:


#affichage des ligne dont la valeur du pays est manquante
nul=data[data["Libellé du pays"].isnull()]
nul


# # traitement des valeurs manquantes

# In[104]:


data=data.drop("Unnamed: 14",axis=1)
data=data.dropna(axis=0)


# In[105]:


#pour afficher la taille de la matrice de données
data.shape


# # 1. Comparaison entre Exportations/importations et leurs évolution en fonction du temps 

# In[107]:


df1=data.groupby(["Libellé du flux"]).sum()
df1=df1.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
df1=df1.transpose()
dates=[2016,2017,2018,2019,2020,2021]
df1["Date"]=dates
df2=df1
df1


# In[108]:


px.scatter(df1,x=df1["Importations CAF"],y=df1["Exportations FAB"],size="Importations CAF",color=df1.index,hover_name="Date",title="Comparaison entre les exportations et les importations par année")


# In[109]:


px.bar(df2,x=df2["Date"],y=df2["Exportations FAB"],color=df2.index,title="l'évolution des exportations ")


# In[110]:


px.bar(df2,x=df2["Date"],y=df2["Importations CAF"],color="Date",title="l'évolution des importation")


# # 2. L’évolution de la valeur des échanges du Maroc par continent

# In[111]:


#préparation de la dataframe pour le traçage du premier graphe
df4=data.groupby("Continent").sum()
df4=df4.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
df4=df4.transpose()
df4["Date"]=dates
df6=df4
df6


# In[112]:


px.line(df6,x="Date",y=["EUROPE","AFRIQUE", "AMERIQUE", "ASIE", "AUSTRALIE","AUTRE"],title="l'évolution de la valeur des échanges par continent ")


# In[113]:


dt1=data[data["Libellé du flux"]=="Exportations FAB"].groupby(data["Continent"]).sum()
dt1=dt1.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
dt1=dt1.transpose()
dt1["Date"]=dates
dt1


# In[114]:


px.line(dt1,x="Date",y=["AFRIQUE","AMERIQUE","ASIE","AUSTRALIE","AUTRE","EUROPE"],title="l'évolution de la valeur exportée par contient")


# In[115]:


dt3=data[data["Libellé du flux"]=="Importations CAF"].groupby(data["Continent"]).sum()
dt3=dt3.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
dt3=dt3.transpose()
dt3["Date"]=dates
dt3


# In[116]:


fig2=px.line(dt3,x="Date",y=["AFRIQUE","AMERIQUE","ASIE","AUSTRALIE","AUTRE","EUROPE"],title="l'évolution de la valeur importée par continent")
fig2.show()


# # 3. L’évolution des échanges par pays 

# In[117]:


dp=data.groupby("Libellé du pays").sum()
dp=dp.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
dp=dp.transpose()
dp["Date"]=dates
dp


# In[118]:


px.line(dp,x="Date",y=[i for i in dp.columns],title="l'évolution de la valeur echangée par pays en DHS")


# In[119]:


dp=data[data["Libellé du flux"]=="Exportations FAB"].groupby("Libellé du pays").sum()
dp=dp.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
dp=dp.transpose()
dp["Date"]=dates


# In[120]:


fig2=px.line(dp,x="Date",y=[i for i in dp.columns],title="l'évolution de la valeur éxportée par pays en DHS")
fig2.show()


# In[121]:


dp=data[data["Libellé du flux"]=="Importations CAF"].groupby("Libellé du pays").sum()
dp=dp.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
dp=dp.transpose()
dp["Date"]=dates

fig2=px.line(dp,x="Date",y=[i for i in dp.columns],title="l'évolution de la valeur importée par pays en DHS")
fig2.show()


# # 4. L’analyse des échanges de 2020 par Continent, pays et type de flux

# In[122]:


dp=data.groupby(["Continent","Libellé du pays"],as_index=False).sum()
dp


# In[123]:


#les exportations et les importations par continent
dc=data.groupby(["Continent","Libellé du flux"],as_index=False).sum()
c={"Importations CAF": "red","Exportations FAB": "green"}
px.bar(dc,x="Continent",y="Valeur DHS 2021",color="Libellé du flux",barmode="group",color_discrete_map=c, title="les exportations et les importations du Maroc par continent en 2021")


# In[124]:


dd=data.groupby(["Libellé du pays","Continent","Libellé du flux"],as_index=False).sum()
px.bar(dd[dd["Valeur DHS 2021"]>5*10**9],y="Valeur DHS 2021",x="Libellé du pays",title="la valeur échangée avec les principaux partenaires en 2021",color="Libellé du flux",barmode='group',color_discrete_sequence=px.colors.qualitative.G10_r)


# In[125]:


dt_n=data.groupby(["Continent","Libellé du pays","Libellé du flux"],as_index=False).sum()
px.bar(dt_n,x="Libellé du pays",y="Valeur DHS 2021",color="Libellé du flux",barmode="group",title="la valeur des exportations/importations par pays",color_discrete_sequence=px.colors.qualitative.G10)


# In[126]:


dr=data[data["Libellé du flux"]=="Exportations FAB"].groupby(["Continent","Libellé du groupement d'utilisation"],as_index=False).sum()
px.bar(dr,y="Valeur DHS 2021",x="Continent",title="les exportations du Maroc par Continent et par groupement d'utilisation en 2021",color="Libellé du groupement d'utilisation",barmode='group',color_discrete_sequence=px.colors.qualitative.G10_r)


# In[127]:


dm=data[data["Libellé du flux"]=="Importations CAF"].groupby(["Continent","Libellé du groupement d'utilisation"],as_index=False).sum()
px.bar(dm,y="Valeur DHS 2021",x="Continent",title="les importations du Maroc par Continent et par groupement d'utilisation en 2021",color="Libellé du groupement d'utilisation",barmode='group',color_discrete_sequence=px.colors.qualitative.Vivid)


# In[128]:


# analyse des données en fonctions du continent et pays 
fig = px.icicle(dp, path=[px.Constant('world'), 'Continent', 'Libellé du pays'], values='Valeur DHS 2021',color="Continent", )
fig.show()


# In[129]:


px.pie(data,values="Valeur DHS 2020",names="Continent",title="la valeur échangée en 2020 par Continent",color_discrete_sequence=px.colors.qualitative.Alphabet)


# In[130]:


dpp=data.groupby(["Continent","Libellé du pays","Libellé du flux"],as_index=False).sum()


# In[131]:


dpp


# In[132]:


couleur={ "EUROPE" : "red", "ASIE" : "blue", "AMERIQUE": "purple","AFRIQUE": "gold","AUSTRALIE" :"brown","AUTRE" : "lime"}
fig = px.sunburst(dpp, path=["Continent","Libellé du pays","Libellé du flux"],color="Continent", values='Valeur DHS 2021',title="les échanges de 2021 en fonction du continent, pays et type de flux",color_discrete_map=couleur)
fig.show()


# In[133]:


fig = px.treemap(data, path=[px.Constant('world'), 'Continent', 'Libellé du pays',"Libellé du flux"], values='Valeur DHS 2021',
                  color="Continent", hover_data=['Code du pays'], title="les échanges de 2021 en fonction du continent, pays et type de flux")
fig.show()


# # 5. Analyse des données en fonction du type de flux et groupement d’utilisation.

# In[134]:


# préparation de la data pour les graphes
d=data.groupby(["Libellé du groupement d'utilisation","Libellé du flux"],as_index=False).sum()
d=d.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
d


# In[135]:


px.pie(data,values="Valeur DHS 2021",names="Libellé du groupement d'utilisation",title="la valeur échangée en 2021 en fonction des groupement d'étulisation",color_discrete_sequence=px.colors.qualitative.G10)


# In[149]:


c={"Importations CAF": "crimson","Exportations FAB": "navy"}
px.bar(d,x="Libellé du groupement d'utilisation",y="Valeur DHS 2021",color="Libellé du flux",barmode="group",color_discrete_map=c, title="les échanges du Maroc du 2021 en fonction du type de flux et groupement d'utilisation")


# In[151]:


fig = px.funnel(d, x='Valeur DHS 2021', y="Libellé du groupement d'utilisation",color="Libellé du flux",color_discrete_map={"Importations CAF": "crimson","Exportations FAB": "navy"},title="la valeur des exportations et des importations en fonction des groupement d'utilisation")
fig.show()


# # 6.Les exportations et les importations du Maroc par produit remarquable

# In[138]:


#préparation de la data 

dta=data.groupby(["Libellé du nouveau produits remarquables","Libellé du flux"],as_index=False).sum()
dta


# In[139]:


px.pie(dta.loc[dta["Valeur DHS 2020"]>5*10**9],names="Libellé du nouveau produits remarquables",values="Valeur DHS 2020",title="les produits les plus échangés en 2020",color_discrete_sequence=px.colors.qualitative.G10)


# In[140]:


da=dt[dt["Libellé du flux"]=="Exportations FAB"].groupby("Libellé du nouveau produits remarquables",as_index=False).sum()
da


# In[141]:


px.pie(da[da["Valeur DHS 2020"]>5*10**9],names="Libellé du nouveau produits remarquables",values="Valeur DHS 2020",title="Exportations par produits",color_discrete_sequence=px.colors.qualitative.D3)


# In[152]:


da=dt[dt["Libellé du flux"]=="Importations CAF"].groupby("Libellé du nouveau produits remarquables",as_index=False).sum()
px.pie(da[da["Valeur DHS 2020"]>5*10**9],names="Libellé du nouveau produits remarquables",values="Valeur DHS 2020",title="Importations par produit",color_discrete_sequence=px.colors.qualitative.D3)


# # 7. la balance commercial du Maroc durant les 6 dernières années

# In[143]:


#préparation de la data
bl=data.groupby("Libellé du flux").sum()
bl=bl.drop(["Code du nouveau produits remarquables","Code du flux"],axis=1)
bl=bl.transpose()
bl["déficit"]=bl["Importations CAF"]-bl["Exportations FAB"]
bl["Date"]=dates


# In[144]:


bl


# In[145]:


px.bar(bl,x="Date",y="déficit",color="déficit",title="le déficit commercial du Maroc durant les 6 dernières années")


# In[ ]:




