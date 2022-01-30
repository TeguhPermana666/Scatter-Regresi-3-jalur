#BMI adalah sebuah metode untuk menghitung body max index dengan cara :
#berat badan/(tinggi badan)^2
#jika hasil dari bmi di sekitaran rasio 18.5-24.9

#setup notebook
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#load data
data_file="Visualisasi_data\insurance.csv"
data=pd.read_csv(data_file)
print(data)
#plot data by scatter 
print(data['smoker'].dtypes)
"""
x=>untuk horizontal
y=>untuk vertical

scatter_plot digunakan untuk memetakan sebuah data di setiap nilainya menjadi scatter
sehingga memudahkan kita untuk melakukan sebuah analisis data pada pemusatan data dan penyebaran data pada aspek tetentu 
"""
plt.figure(figsize=(10,6))
sns.scatterplot(x=data['bmi'], y=data['charges'])
plt.show()
"""
dilihat pada data menyatakan bahwa bmi dengan charges /pembayaran insuranse
memiliki relasi positif, yang mana dapat diartikan bahwa
semakin besar BMI maka semakin tinggi taraf pembayarn / insuranse dikarenakan jika semakin
tinggi berat badan yang di iringi semakin rendah tinggi badan maka semakin berisiko untuk terkena penyakit yang tentunya
sangat membebani pada perawatan yang mana kami melihatnya hanya pada analisis penyebaran datanya antara kedua variabel

untuk melihat hubungan antara variabel antar komponen pada nilai di setiap column dapat dilakukan dengan melakukan pengujian
regresion line ->sns.regplot()
"""
plt.figure(figsize=(10,6))
sns.regplot(x=data['bmi'],y=data['charges'])
plt.show()



#color coded scetter plot
"""
salah satu untuk mengetahui sebuah relationship antara variabel 2,3 dan sebelihnya dapat dilakukan dengan scatterplot namun ada salah satu
cara yang dapat diterapkan yakni dengan penyebaran data dituangkan dalam warna yang berbeda di setiap elemen yang berkaitan

mengetahui hubungan bmi dengan biaya tadi sudah namun untuk hubungan bmi,biaya dengan orng yg merokok(smoker) dapat dilakukan dengan color dalam 
scetter plot 
"""
plt.figure(figsize=(10,6))
sns.scatterplot(x=data['bmi'],y=data['charges'],hue=data['smoker'])
plt.show()
"""
pada hasil disana ketiga komponenn tersebut smoker,bmi,charges berelasi regresi positif yg mana orng yg merokok memiliki charges yang lebih besar ketimbang orng yg tidak merokok
dan tentunya rata rata orng yang tidak merokok memiliki bmi yang rendah yang berarti sgt baik namun orng yg merokok justru memiliki bmi yang jauh lebih besar yang mana
bmi berelasi positif dengan charges.
untuk mengetahui kuat lemahnya relasi dengan regresi dua atau lebuh dapat dilakukan dengan menggunakan lmplot
"""
sns.lmplot(x='bmi',y='charges',hue='smoker',data=data,size=5)
#lmplot => secara otomatis dataframe pada data analisis di kalkulasi.semua sudah include di dalam lmplot tinggal di berikan argument berdasarkan konfigurasi yang diinginkan
"""
data['bmi']=>digunakan untuk mengakses sebuah nilai pada column bmi, sedangkan
'bmi'=>digunakan untuk menselect sebuah nama column

adapun sebuah refer plot categorical scatter plot dapat menggunakan swarmplot
"""
plt.show()

sns.swarmplot(x=data['smoker'],y=data['charges'])
plt.show()