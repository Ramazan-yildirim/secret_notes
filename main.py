import base64
import os


def encode(key, clear):
    clear = "##MSG##" + clear  # Belirteç ekle
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    result = "".join(dec)

    # Belirteç kontrolü
    if not result.startswith("##MSG##"):
        raise ValueError("Anahtar hatalı veya veri bozulmuş.")

    return result[len("##MSG##"):]


def save_notes():
    title = input("Başlık girin: ").strip()
    message = input("Mesaj girin: ").strip()
    secret = input("Anahtar (şifre) girin: ").strip()

    if not title or not message or not secret:
        print("❌ Hata: Tüm alanları doldurmalısınız.")
        return

    encrypted = encode(secret, message)

    with open("mysecret.txt", "a") as file:
        file.write(f"\n{title}\n{encrypted}")
    
    print("✅ Not şifrelendi ve kaydedildi.")


def list_and_decrypt():
    if not os.path.exists("mysecret.txt"):
        print("📂 Henüz kayıtlı not yok.")
        return

    with open("mysecret.txt", "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    if not lines:
        print("📂 Dosya boş.")
        return

    notes = [(lines[i], lines[i+1]) for i in range(0, len(lines)-1, 2)]

    print("\n📋 Kayıtlı Başlıklar:")
    for idx, (title, _) in enumerate(notes, start=1):
        print(f"{idx}. {title}")

    try:
        choice = int(input("\nÇözmek istediğiniz notun numarasını girin: ").strip())
        if 1 <= choice <= len(notes):
            _, encrypted = notes[choice - 1]
            key = input("Anahtar (şifre) girin: ").strip()
            try:
                decrypted = decode(key, encrypted)
                print("\n🔓 Çözülen Mesaj:")
                print(decrypted)
            except Exception:
                print("❌ Şifre çözme başarısız. Anahtar yanlış veya veri bozuk.")
        else:
            print("❗ Geçersiz seçim.")
    except ValueError:
        print("❗ Sayı girmeniz gerekiyor.")


def menu():
    while True:
        print("\n📒 Şifreli Notlar Uygulaması")
        print("1. Yeni not ekle ve şifrele")
        print("2. Kaydedilen notlardan çöz")
        print("3. Çıkış")
        choice = input("Seçiminiz (1/2/3): ").strip()

        if choice == '1':
            save_notes()
        elif choice == '2':
            list_and_decrypt()
        elif choice == '3':
            print("Çıkılıyor...")
            break
        else:
            print("❗ Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    menu()
