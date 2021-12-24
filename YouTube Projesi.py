from pytube import YouTube
import time

baglantiAdresi = input("Indirilecek Baglanti Adresi : ")

baglanti = YouTube(baglantiAdresi)
baslik = baglanti.title
uzunluk = time.strftime('%H:%M:%S', time.gmtime(baglanti.length))
izlenmeSayisi = baglanti.views
rating=baglanti.rating
ct=baglanti.publish_date

print(f"\nVideonun Basligi: {baslik}")
print(f"Videonun Uzunlugu: {uzunluk}")
print(f"Videonun İzlenme Sayisi: {izlenmeSayisi}")
print(f"videonun raiting sayısı: {rating}")
print(f"videonun yayınlanma tarihi {ct}")

if(baglanti.length>120):
    onay = input("\nVidyo süresi 2 dakikanın üzerinde yine de indirmek istiyor musunuz?: ")
    if(onay=='Evet' or onay=='evet' or onay =="EVET" or onay == 'evt'):
        aktarma = baglanti.streams.get_highest_resolution()
        print('İndirme islemi baslatildi...')
        aktarma.download()
        print('\nİndirme islemi tamamlandi.')
    else:
        print("İndirme islemi iptal edildi.")
else:
    print("Video süresi 2 dakikanın altında olduğu icin indirme islemi baslatilmadi")