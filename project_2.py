"""
[Selin]Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.
[Selin]2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
[Fatih] İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
[Selin]'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?
[Önder]'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
[Beyza] Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
[Fatih] IMDB puanı en yüksek olan ilk 10 film hangileridir?
[Fatih] IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
[Beyza] IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
[Fatih] 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
[Önder]Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
[Beyza] Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
[Önder]Hangi yılın toplam "runtime" süresi en fazladır?
[Aydın] Her bir dilin en fazla kullanıldığı "Genre" nedir?
[Aydın] Veri setinde outlier veri var mıdır? Açıklayınız.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

df = pd.read_csv('./NetflixOriginals.csv',encoding="ISO-8859-1")

# Sütunlardaki boşlukları alt tire ile değiştirdim.
df.columns = df.columns.str.replace(" ","_")

 
# IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
def correlation(df):
    corra= df['IMDB_Score'].corr(df['Runtime'])
    print(corra)
    sns.regplot(x=df['IMDB_Score'], y=df['Runtime'])
    plt.show()

# IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
def topScoreGenre(df):
    df.groupby("Genre").agg({"IMDB_Score": "max"}).sort_values(by="IMDB_Score", ascending=False)[0:10].reset_index()
    genrescore_on = df.groupby("Genre").agg({"IMDB_Score": "max"}).sort_values(by="IMDB_Score", ascending=False)[0:10].reset_index()
    print (df.groupby("Genre").agg({"IMDB_Score": "max"}).sort_values(by="IMDB_Score", ascending=False)[0:10])
    sns.lineplot(y=genrescore_on["Genre"], x=genrescore_on["IMDB_Score"])
    plt.show()

#Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
def mostUsedLang(df):
    df['Language'].value_counts().head(3) 

# Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
def lowScoreLangs(df):
    imdb_most_low = df.groupby(["Language"])["IMDB_Score"].mean().sort_values(ascending=True).reset_index().head(5)
    print(f"En düşük IMDB ortalamasına sahip 5 dil; \n{imdb_most_low}")

    sns.barplot(x='Language', y='IMDB_Score', data = imdb_most_low)
    plt.show() 


# IMDP Puanı yüksek olan 10 film.
def topIMDB(df):
    df.sort_values(by="IMDB_Score", ascending = False, inplace = True)
    df = df.reset_index()
    print(f" IMDB puanı en yüksek ilk 10 film; \n  {df.loc[:10]}")

# 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
def topRuntime(df):
    df.sort_values(by="Runtime", ascending = False, inplace = True)
    data = df.reset_index().head(10)
    print(data) 
    sns.violinplot(x='Runtime',y='Title',data =df.nlargest(10, 'Runtime'))
    plt.show() 
    
    
#Hangi yılın toplam runtime süresi en fazladır?
df.groupby("Premiere").agg({"Runtime": "sum"}).sort_values(by="Runtime", ascending=False)[0:1]


# 'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
def visualCategPlot(df):
    df['Genre']=df['Genre'].str.replace(" /","/")
    df['Genre']=df['Genre'].str.replace("/ ","/")
    df['Genre']=df['Genre'].str.replace(" / ","/")

    df3 = df['Genre'].str.split("/", expand=True)
    df3.columns = ['Genre_ID{}'.format(x+1) for x in df3.columns]
    df = df.join(df3)
    

    
    
    value=df["Genre_ID1"].value_counts().to_frame("counts")
    value.reset_index(inplace=True)
    value.rename(columns={"index": "Categories", "counts": "Counts"}, inplace=True)
    value2=df["Genre_ID2"].value_counts().to_frame("counts")
    value2.reset_index(inplace=True)
    value2.rename(columns={"index": "Categories", "counts": "Counts"}, inplace=True)
    value3=df["Genre_ID3"].value_counts().to_frame("counts")
    value3.reset_index(inplace=True)
    value3.rename(columns={"index": "Categories", "counts": "Counts"}, inplace=True)
    value4=df["Genre_ID4"].value_counts().to_frame("counts")
    value4.reset_index(inplace=True)
    value4.rename(columns={"index": "Categories", "counts": "Counts"}, inplace=True)
    

    merged_value= pd.concat([value, value2, value3, value4]).groupby(['Categories']).sum().sort_values("Counts", ascending=False).reset_index()
    
    
    

     
    
    
    plt.plot( merged_value["Counts"], merged_value["Categories"])
    plt.show()  


def categReport(df):
    strippted = df['Genre'].str.split("/")
    categories_array = np.unique(np.char.strip(np.array([x for xs in strippted for x in xs])))  
    print(f"'Genre' Sütunu {np.size(categories_array)} kategoriye sahiptir ve bu kategoriler şunlardır; \n {categories_array}")






 
# İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
def highestEngMovie(df):
    engMovies = df[df["Language"] == "English"]
    df_eng_gen = engMovies.groupby(["Genre"])["IMDB_Score"].mean().sort_values(ascending=False).head(5)
    plt.pie(df_eng_gen, labels=df_eng_gen.index,autopct='%1.1f%%', explode=[0.1,0,0,0,0], shadow=True, startangle=90)
    plt.show()
    print(df_eng_gen) 




 
# Her bir dilin en fazla kullanıldığı "Genre" nedir? (A)
def topGenreFromLang(df):
    ax=df.groupby('Language')['Genre'].value_counts().reset_index(name='Countx')
    ax=ax.sort_values(['Countx','Language','Genre'], ascending=False).reset_index(drop=True,inplace=False)
    bx=ax.groupby('Language').max('Countx').reset_index()
    cx=pd.merge(ax, bx, how='inner', on=['Language', 'Countx'])
    print(cx)


#Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.
def q1(data):
    full_length = data[data["Runtime"] > 90]
    full_language = full_length.Language.value_counts()
    fig = px.pie(full_language, names=full_language.index, values=full_language.values, title='Feature-length Movies')
    fig.show() 



#2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
def q2(data):
    type(data['Premiere'])
    data['Premiere'] = pd.to_datetime(data.Premiere)
    docIMDB = data[("2018-12-31" < data['Premiere']) & (data['Premiere'] < "2020-7-1")]
    docIMDB=docIMDB.query("Genre == 'Documentary'")
    docIMDB.plot.scatter("Premiere","IMDB Score",color = {"red"})
    plt.xlabel("Premiere")
    plt.ylabel("IMDB Score")
    plt.title("Documentary")
    plt.show()


#'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?
def q4(data):
    HindRun = data.query("Language == 'Hindi'")
    HindRun = HindRun["Runtime"].mean()
    print(HindRun) 

correlation(df)
topScoreGenre(df)
mostUsedLang(df)
lowScoreLangs(df)
topIMDB(df)
topRuntime(df)
visualCategPlot(df)
categReport(df)
highestEngMovie(df)
topGenreFromLang(df) 

q1(df)
q2(df)
q4(df)