""" 

Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.
2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
[Fatih] İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?
'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
[Beyza] Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
[Fatih] IMDB puanı en yüksek olan ilk 10 film hangileridir?
[Fatih] IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
[Beyza] IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
[Fatih] 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
[Şüheda] Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
[Beyza] Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
[Şüheda] Hangi yılın toplam "runtime" süresi en fazladır?
[Aydın] Her bir dilin en fazla kullanıldığı "Genre" nedir?
[Aydın] Veri setinde outlier veri var mıdır? Açıklayınız

"""




import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./NetflixOriginals.csv',encoding="ISO-8859-1")

#Sütunlardaki boşlukları alt tire ile değiştirdim
df.columns = df.columns.str.replace(" ","_")



"""

#IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.

corra= df['IMDB_Score'].corr(df['Runtime'])
print(corra)
#Görselleştirme
sns.regplot(x=df['IMDB_Score'], y=df['Runtime'])
plt.show()

"""







"""

#IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.

df.groupby("Genre").agg({"IMDB_Score": "max"}).sort_values(by="IMDB_Score", ascending=False)[0:10].reset_index()
genrescore_on = df.groupby("Genre").agg({"IMDB_Score": "max"}).sort_values(by="IMDB_Score", ascending=False)[0:10].reset_index()


print (df.groupby("Genre").agg({"IMDB_Score": "max"}).sort_values(by="IMDB_Score", ascending=False)[0:10])
sns.lineplot(y=genrescore_on["Genre"], x=genrescore_on["IMDB_Score"])
plt.show()

#Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
df['Language'].value_counts().head(3)

"""







"""
#Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.(Görselleştirmesinden emin değilim)


#Düzenlemeler yapıldı son hali kod sahibinin insiyatifinde.(Fatih)


imdb_most_low = df[df['IMDB_Score']<5][["Language", "IMDB_Score"] ].sort_values('IMDB_Score', ascending = True)

print(imdb_most_low)


#Plotly kütüphanesi kullanmak amaçlanmış sanırım. (Fatih)
fig = px.bar(imdb_most_low, x='Language', y= 'IMDB_Score', color = 'Title')
fig.show()


#Alternatif olarak. (Fatih)
sns.barplot(x='Language', y='IMDB_Score', data = imdb_most_low)
plt.show()

"""









""" 
#IMDP Puanı yüksek olan 10 film.


df.sort_values(by="IMDB_Score", ascending = False, inplace = True)
df = df.reset_index()
print(df.loc[:10]) 

"""







"""

#'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.

df.sort_values(by="Runtime", ascending = False, inplace = True)
data = df.reset_index().head(10)
print(data) 

sns.violinplot(
    x='Runtime',
    y='Title',
    data =df.nlargest(10, 'Runtime')
)

plt.show()

"""








"""

#'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
(TAMAMLANMADI [BOŞTA])


data = df["Genre"].unique()

print(data)

#set(df.Genre)

"""








"""
İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
(TAMAMLANMADI [Fatih] )

engMovies = df[df["Language"] == "English"]

print(engMovies["IMDB_Score"].idxmax())

#-------------------------------

#print(engMovies["IMDB_Score"].median())   6.4


result = engMovies[engMovies["IMDB_Score"] > 6.4]
print(result["Genre"].mode())



-------------------
BİR TAKIM BİLGİLER


#satır sayısı, sütun sayısı gösterir
print(df.shape)

#sütunların data typlearına bakıyorum
print(df.dtypes)



print(df.info()) 
"""
