# 🔐 Secret Notes (CLI Tabanlı)

Bu proje, terminal üzerinden çalışan şifreli notlar uygulamasıdır.  
Kullanıcıdan not başlığı, içerik ve şifre alır; içeriği şifreler ve kaydeder.  
Kayıtlı başlıklar listelenebilir ve doğru şifre ile çözülebilir.

## 📦 Özellikler

- Metin tabanlı kullanıcı arayüzü
- Şifrelenmiş mesajlar sadece doğru anahtar ile çözülebilir
- Docker desteği ile platform bağımsız çalıştırılabilir

---

## 🚀 Kullanım

### 1️⃣ Docker Hub'dan Çekme ve Çalıştırma

docker pull ramazan581/secret-notes:latest

docker run -it --rm ramazan581/secret-notes

✍️ Örnek Kullanım

📒 Şifreli Notlar Uygulaması
1. Yeni not ekle ve şifrele
2. Kaydedilen notlardan çöz
3. Çıkış

Seçiminiz (1/2/3): 1
Başlık girin: Banka Bilgileri
Mesaj girin: Şifre: 1234
Anahtar (şifre) girin: gizli123
✅ Not şifrelendi ve kaydedildi.



