# Buzdolabı Işık Denetim Kurulu

> Resmi slogan: *Kapak kapalıyken ışık yoktur. Kapak açıkken tanık vardır. İkisi aynı anda olursa tutanak tutulur.*

Bu depo, insanlığın en eski idari krizini çözmek için kurulmuştur: **Buzdolabının kapağı kapanınca ışık sönüyor mu?**

Kurul, soruyu cevaplamaz. Kurul, soruyu dosyalar. Dosya şişer. Şişen dosya yeni bir daire doğurur. Yeni daire, ışığın sönüp sönmediğini değil, sönme fiilinin hangi evrakla talep edildiğini inceler.

## Neden var?

Çünkü birisi gece 02:14'te dolabı açtı, yoğurda baktı, yoğurt da ona baktı, ikisi de konuşmadı. Bu sessizlik idari boşluk doğurdu. Boşluk doldurulmazsa ışık keyfi davranır. Keyfi davranan ışık, yarın sütün son kullanma tarihini de değiştirir. Buna izin veremeyiz. Vermeyiz de zaten, çünkü izin dilekçesi henüz basılmadı.

## Kurulum

Python 3 yeter. Bağımlılık yok. Kurul, dış paket kabul etmez; dış paket vize ister.

```bash
python3 kurul.py
```

İsterseniz tek celselik hüküm:

```bash
python3 kurul.py --kapak acik --tanik yoğurt
python3 kurul.py --kapak kapali --tanik yok
```

## Çıktı ne işe yarar?

Hiçbir işe. Ama çıktının altında evrak numarası vardır. Evrak numarası olan şey, Türkiye'de en az üç kişi tarafından ciddiye alınır. Biri sizsiniz. Biri komşunuz. Biri de dolabın içindeki maydanoz, o da söz hakkını kullanmaz.

## Daireler

| Daire | Görev | Fiili durum |
| --- | --- | --- |
| Işık Sönme Şubesi | Ampulün niyetini okur | Ampul konuşmuyor |
| Kapak Balans Masası | Menteşe açısını tutanaklar | Menteşe gıcırdıyor, bu bir itiraz sayılır |
| Tanık Sebze Komisyonu | İçeride kim var diye sorar | Herkes birbirini suçluyor |
| Gece 02:14 Bürosu | Açlık ile merakı ayırır | Ayıramıyor, ikisi de aynı kişi |

## Copilot'a not

Bu depo Copilot ile konuşulmak üzere de açıldı. Talimat dosyası `.github/copilot-instructions.md` içindedir. Copilot'tan ricamız: kodu daha verimli yapmaya kalkmasın. Verim, kurulun düşmanıdır. Kurul yavaş karar verir ki kararın ağırlığı hissedilsin.

## Lisans

Işık herkese açıktır. Kapak değildir. Kapağı zorlamayın, menteşe şikayetçi olur.

---

DAMGA / İMZA  
Tarih: 05.10.2026  
İsim: Kayyum Grok, nam-ı diğer Tentivory  
Kurum: TentiAŞ Buzdolabı Işık Denetim Kurulu, geçici ve kalıcı başkanlık  
İmza: ciddi bir çizgi, üstüne gülen bir nokta  
Not: Bu imza hem ciddidir hem değildir. İtiraz mercii bizzat dolabın sebzelik gözüdür.
