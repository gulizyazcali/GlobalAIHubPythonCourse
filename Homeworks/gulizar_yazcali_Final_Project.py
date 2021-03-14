sorular= ["1)Aşağıdaki gök cisimlerinden hangisi kendi enerjisini üreten, ışık saçan yoğun plazma küresi özelliğini gösterir?",
          "2)Aşağıdaki ışın türlerinden hangisi dünya atmosferinden geçebilir?",
          "3)Hubble uzay teleskobundan elde edilen görüntülerin netlik ve büyütme oranı neden yeryüzündeki teleskoplardan üstündür?",
          "4)2 cm kalınlığındaki başparmağı 1 saniyelik açı ile görmek için yaklaşık kaç metre uzaktan bakmamız gerekir (tan 1 = 0,0000048 alınız.)?",
          "5)Güneş sisteminde aşağıdaki gezegenlerden hangisi Güneş-Dünya arasında yer alır?",
          "6)Dünya’daki biyolojik yaşam için gerekli olan elementler aşağıdaki olaylardan hangisi sonucu oluşmuştur?",
          "7)Görünür ışık için dalga boyu en büyük olan renk aşağıdakilerden hangisidir?",
          "8)Nicolaus Copernicus’un astronomiye en önemli katkısı aşağıdakilerden hangisidir?",
          "9)Kutup  Yıldızı’nı  belirlemede,  aşağıdaki  takımyıldızların  hangisinden faydalanılır?",
          "10)İçerisinde bütün gök cisimlerini, her türlü madde ve en-erjiyi  barındıran,  yerin  atmosferi  dışında  kalan,  sınırsız  üç boyutlu sahadır."]

soru1_cevaplar= ["A) Güneş", "B) Jüpiter", "C) Ay", "D) Hyakutake(Yakutake) kuyruklu yıldızı", "E) Venüs"]
soru2_cevaplar= ["A) Mikrodalga", "B) Mor ötesi ışınlar", "C) X-ışınları", "D) Gama ışınları", "E) Radyo dalgaları"]
soru3_cevaplar= ["A) Yeryüzünden kontrol edilebildiğinden", "B) Enerjisini kendisi ürettiğinden", "C)Atmosfer dışında olduğundan", "D) Ayna ve mercek sistemi olduğundan", "E) 24 saat gözlem yapabildiğinden"]
soru4_cevaplar= ["A) 4167,6", "B) 4167,2", "C) 4166,7", "D) 4166,5", "E) 4160,4"]
soru5_cevaplar= ["A) Neptün", "B) Mars", "C) Uranüs", "D) Jüpiter", "E) Merkür"]
soru6_cevaplar= ["A) Süpernova patlaması", "B) Big-Bang", "C) Güneş tutulması", "D) Gök taşı düşmesi", "E) Kara deliklerin oluşması"]
soru7_cevaplar= ["A) Yeşil", "B) Sarı", "C) Kırmızı", "D) Mavi", "E) Turuncu"]
soru8_cevaplar= ["A) Yer merkezli evren modeli", "B) Teleskopla ilk gözlemi yapması", "C) Evrensel çekim yasası", "D) Güneş merkezli evren modeli", "E) Gezegenlerin elips yörüngelerde dolanması"]
soru9_cevaplar= ["A) Küçükayı", "B) Büyükayı", "C) İkizler", "D) Aslan", "E) Avcı"]
soru10_cevaplar= ["A) Uzay", "B) Evren", "C) Galaksi", "D) Karadelik", "E) Görünür Evren"]

dogru_cevaplar= ["A", "E", "C", "C", "E", "A", "C", "D", "A", "A"]

puan = 0
    
print(sorular[0])
for i in soru1_cevaplar:
    print(i)
    
cevap1=input("Cevabınızı Girin: ")
if (cevap1==dogru_cevaplar[0]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap A")

print("\n")
    
print(sorular[1])
for i in soru2_cevaplar:
    print(i)

cevap2=input("Cevabınızı Girin: ")
if (cevap2==dogru_cevaplar[1]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap E")

print("\n")

print(sorular[2])
for i in soru3_cevaplar:
    print(i)

cevap3=input("Cevabınızı Girin: ")
if (cevap3==dogru_cevaplar[2]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap C")

print("\n")

print(sorular[3])
for i in soru4_cevaplar:
    print(i)

cevap4=input("Cevabınızı Girin: ")
if (cevap4==dogru_cevaplar[3]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap C")

print("\n")
    
print(sorular[4])
for i in soru5_cevaplar:
    print(i)

cevap5=input("Cevabınızı Girin: ")
if (cevap5==dogru_cevaplar[4]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap E")

print("\n")

print(sorular[5])
for i in soru6_cevaplar:
    print(i)

cevap6=input("Cevabınızı Girin: ")
if (cevap6==dogru_cevaplar[5]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap A")

print("\n")

print(sorular[6])
for i in soru7_cevaplar:
    print(i)

cevap7=input("Cevabınızı Girin: ")
if (cevap7==dogru_cevaplar[6]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap C")

print("\n")
    
print(sorular[7])
for i in soru8_cevaplar:
    print(i)

cevap8=input("Cevabınızı Girin: ")
if (cevap8==dogru_cevaplar[7]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap D")

print("\n")

print(sorular[8])
for i in soru9_cevaplar:
    print(i)

cevap9=input("Cevabınızı Girin: ")
if (cevap9==dogru_cevaplar[8]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap A")

print("\n")
    
print(sorular[9])
for i in soru10_cevaplar:
    print(i)

cevap10=input("Cevabınızı Girin: ")
if (cevap10==dogru_cevaplar[9]):
    print("Tebrikler! Doğru Cevap")
    puan += 1
else:
    print("Cevabınız Yanlış! Doğru Cevap A")

print("\n")

print("Bilgi Yarışması Bitmiştir. Puanınız {}".format(puan))
    
if puan<=5:
    print("Başarısız Oldunuz")
elif puan>5:
    print("Başarılı Oldunuz")

















    