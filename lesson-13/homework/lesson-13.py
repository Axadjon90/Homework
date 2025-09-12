1)from datetime import datetime
from dateutil.relativedelta import relativedelta
def yoshni_hisobla(tugilgan_sana_str):
    try:
        tugilgan_sana = datetime.strptime(tugilgan_sana_str, "%Y-%m-%d")
        bugun = datetime.today()
        if tugilgan_sana > bugun:
            print("❌ Tug‘ilgan sana kelajakda bo'lishi mumkin emas.")
            return
        farq = relativedelta(bugun, tugilgan_sana)
        print(f"\n🧮 Sizning yoshingiz: {farq.years} yil, {farq.months} oy, {farq.days} kun.")
    except ValueError:
        print("❌ Noto‘g‘ri sana formati! Iltimos, yyyy-mm-dd formatida kiriting.")
if __name__ == "__main__":
    sana = input("Tug‘ilgan sanangizni kiriting (yyyy-mm-dd): ")
    yoshni_hisobla(sana)
   Sizning yoshingiz: 35 yil, 3 oy, 11 kun.

2)from datetime import datetime, timedelta
def kunlargacha_tugilgan_kun(tugilgan_sana_str):
    try:
        tugilgan_sana = datetime.strptime(tugilgan_sana_str, "%Y-%m-%d")
        bugun = datetime.today()
        this_year_birthday = tugilgan_sana.replace(year=bugun.year)
        if this_year_birthday < bugun:
            next_birthday = this_year_birthday.replace(year=bugun.year + 1)
        else:
            next_birthday = this_year_birthday
        farq = next_birthday - bugun
        kunlar_qoldi = farq.days
        print(f"\n📅 Keyingi tug‘ilgan kuningizgacha {kunlar_qoldi} kun qoldi.")
    except ValueError:
        print("❌ Noto‘g‘ri sana formati! Iltimos, yyyy-mm-dd formatida kiriting.")
if __name__ == "__main__":
    sana = input("Tug‘ilgan sanangizni kiriting (yyyy-mm-dd): ")
    kunlargacha_tugilgan_kun(sana)
  Keyingi tug‘ilgan kuningizgacha 261 kun qoldi.

3)from datetime import datetime, timedelta
def uchrashuv_rejalashtiruvchi():
    try:
        boshlanish_str = input("Joriy sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
        boshlanish_vaqti = datetime.strptime(boshlanish_str, "%Y-%m-%d %H:%M")
        soat = int(input("Uchrashuv davomiyligi (soat): "))
        daqiqa = int(input("Uchrashuv davomiyligi (daqiqa): "))
        davomiylik = timedelta(hours=soat, minutes=daqiqa)
        tugash_vaqti = boshlanish_vaqti + davomiylik
        print(f"\n🕒 Uchrashuv tugash vaqti: {tugash_vaqti.strftime('%Y-%m-%d %H:%M')}")
    except ValueError:
        print("❌ Noto‘g‘ri format! Iltimos, sanani 'YYYY-MM-DD HH:MM' formatida kiriting.")
if __name__ == "__main__":
    uchrashuv_rejalashtiruvchi()
  ❌ Noto‘g‘ri format! Iltimos, sanani 'YYYY-MM-DD HH:MM' formatida kiriting.

4)from datetime import datetime
def vaqt_mintaqasi_konvertori():
    try:
        sana_vaqt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
        kirilgan_vaqt = datetime.strptime(sana_vaqt_str, "%Y-%m-%d %H:%M")
        joriy_mintaqa_str = input("Joriy vaqt mintaqasini kiriting (masalan, Asia/Tashkent): ")
        maqsad_mintaqa_str = input("Maqsadli vaqt mintaqasini kiriting (masalan, Europe/London): ")
        joriy_mintaqa = pytz.timezone(joriy_mintaqa_str)
        maqsad_mintaqa = pytz.timezone(maqsad_mintaqa_str)
        local_vaqt = joriy_mintaqa.localize(kirilgan_vaqt)
        konvert_qilingan_vaqt = local_vaqt.astimezone(maqsad_mintaqa)
        print(f"\n🕓 Konvertatsiya qilingan vaqt:")
        print(f"{joriy_mintaqa_str}: {local_vaqt.strftime('%Y-%m-%d %H:%M')} → "
              f"{maqsad_mintaqa_str}: {konvert_qilingan_vaqt.strftime('%Y-%m-%d %H:%M')}")
    except Exception as e:
        print(f"❌ Xatolik: {e}")
        print("Iltimos, sana formatini va vaqt mintaqalarini togri kiriting.")
if __name__ == "__main__":
    vaqt_mintaqasi_konvertori()
❌ Xatolik: name 'pytz' is not defined
Iltimos, sana formatini va vaqt mintaqalarini togri kiriting.

5)import time
from datetime import datetime
def ortga_hisoblash_taymeri():
    try:
        sana_vaqt_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
        kelajak_vaqt = datetime.strptime(sana_vaqt_str, "%Y-%m-%d %H:%M:%S")
        hozir = datetime.now()
        if kelajak_vaqt <= hozir:
            print("❌ Tugash vaqti hozirgi vaqtdan keyin bo‘lishi kerak.")
            return
        print("\n⏳ Ortga hisoblash boshlandi...\n")
        while True:
            hozir = datetime.now()
            farq = kelajak_vaqt - hozir
            if farq.total_seconds() <= 0:
                print("\n⏰ Vaqt tugadi!")
                break
            kunlar = farq.days
            soat, qoldiq = divmod(farq.seconds, 3600)
            daqiqa, soniya = divmod(qoldiq, 60)
            vaqt_formatda = f"{kunlar} kun, {soat:02d}:{daqiqa:02d}:{soniya:02d}"
            print(f"\r🕒 Qolgan vaqt: {vaqt_formatda}", end="", flush=True)
            time.sleep(1)
    except ValueError:
        print("❌ Noto‘g‘ri format! Iltimos, YYYY-MM-DD HH:MM:SS formatida kiriting.")
if __name__ == "__main__":
    ortga_hisoblash_taymeri()
⏳ Ortga hisoblash boshlandi...
🕒 Qolgan vaqt: 12871 kun, 16:45:06

6)import re
def emailni_tekshir(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
def email_validator():
    email = input("📧 Email manzilini kiriting: ")
    if emailni_tekshir(email):
        print("✅ Email manzili to‘g‘ri!")
    else:
        print("❌ Email manzili noto‘g‘ri formatda.")
if __name__ == "__main__":
    email_validator()
  ✅ Email manzili to‘g‘ri!

7)def format_telefon_raqami(raqam):
    faqat_raqamlar = ''.join(filter(str.isdigit, raqam))
    if len(faqat_raqamlar) == 10:
        return f"({faqat_raqamlar[:3]}) {faqat_raqamlar[3:6]}-{faqat_raqamlar[6:]}"
    else:
        return None
def telefon_format_dasturi():
    raqam = input("📱 Telefon raqamingizni kiriting (faqat raqamlar yoki formatli bo‘lishi mumkin): ")
    natija = format_telefon_raqami(raqam)
    if natija:
        print(f"✅ Formatlangan raqam: {natija}")
    else:
        print("❌ Telefon raqami noto‘g‘ri. Iltimos, 10 xonali raqam kiriting (masalan, 1234567890).")
if __name__ == "__main__":
    telefon_format_dasturi()
  ✅ Formatlangan raqam: (897) 470-5779

8)import re
def parol_kuchini_tekshir(parol):
    mezonlar = {
        'uzunlik': len(parol) >= 8,
        'kichik_harf': re.search(r"[a-z]", parol) is not None,
        'katta_harf': re.search(r"[A-Z]", parol) is not None,
        'raqam': re.search(r"[0-9]", parol) is not None,
        'maxsus_belgi': re.search(r"[!@#$%^&*(),.?\":{}|<>]", parol) is not None
    }
    barcha_majburiy = all([mezonlar['uzunlik'], mezonlar['kichik_harf'], mezonlar['katta_harf'], mezonlar['raqam']])
    if barcha_majburiy:
        kuch = "Kuchli" if mezonlar['maxsus_belgi'] else "O'rtacha"
    else:
        kuch = "Kuchsiz"
    return kuch, mezonlar
def parol_kiritish():
    parol = input("🔐 Parolingizni kiriting: ")
    kuch, mezonlar = parol_kuchini_tekshir(parol)
    print(f"\n📊 Parol kuchi: {kuch}")
    print("🔍 Mezonlar tekshiruvi:")
    print(f"  - ✅ Uzunligi >= 8 ta belgi: {'Ha' if mezonlar['uzunlik'] else 'Yo‘q'}")
    print(f"  - ✅ Kichik harf mavjud: {'Ha' if mezonlar['kichik_harf'] else 'Yo‘q'}")
    print(f"  - ✅ Katta harf mavjud: {'Ha' if mezonlar['katta_harf'] else 'Yo‘q'}")
    print(f"  - ✅ Raqam mavjud: {'Ha' if mezonlar['raqam'] else 'Yo‘q'}")
    print(f"  - ✅ Maxsus belgi mavjud: {'Ha' if mezonlar['maxsus_belgi'] else 'Yo‘q'}")
if __name__ == "__main__":
    parol_kiritish()
  📊 Parol kuchi: Kuchli
🔍 Mezonlar tekshiruvi:
  - ✅ Uzunligi >= 8 ta belgi: Ha
  - ✅ Kichik harf mavjud: Ha
  - ✅ Katta harf mavjud: Ha
  - ✅ Raqam mavjud: Ha
  - ✅ Maxsus belgi mavjud: Ha

9)import re
def word_finder():
    print("📘 Matnni kiriting (ko'p qatorda tugatish uchun Enter + Enter bosing):")
    matn_qatorlar = []
    while True:
        qator = input()
        if qator == "":
            break
        matn_qatorlar.append(qator)
    matn = "\n".join(matn_qatorlar)
    soz = input("\n🔍 Qidiriladigan so‘zni kiriting: ").strip()
    if not soz:
        print("❌ So‘z kiritilmadi.")
        return
    pattern = r'\b' + re.escape(soz) + r'\b'
    natijalar = re.findall(pattern, matn, flags=re.IGNORECASE)
    soni = len(natijalar)
    if soni > 0:
        print(f"\n✅ So‘z '{soz}' matnda {soni} marta topildi.")
    else:
        print(f"\n❌ So‘z '{soz}' matnda topilmadi.")
if __name__ == "__main__":
    word_finder()
        📘 Matnni kiriting (ko'p qatorda tugatish uchun Enter + Enter bosing):
10)import re
def sana_extractor():
    print("📄 Matnni kiriting (tugash uchun Enter + Enter):")
    qatorlar = []
    while True:
        qator = input()
        if qator == "":
            break
        qatorlar.append(qator)
    matn = "\n".join(qatorlar)

    sana_patternlar = [
        r'\b\d{2}[./-]\d{2}[./-]\d{4}\b',
        r'\b\d{4}[./-]\d{2}[./-]\d{2}\b',
        r'\b\d{1,2}(st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b',
    ]
    topilgan_sanalar = []
    for pattern in sana_patternlar:
        natijalar = re.findall(pattern, matn, flags=re.IGNORECASE)
        if natijalar and isinstance(natijalar[0], tuple):
            topilgan_sanalar.extend(["".join(x) for x in natijalar])
        else:
            topilgan_sanalar.extend(natijalar)
    if topilgan_sanalar:
        print(f"\n📆 Topilgan sanalar ({len(topilgan_sanalar)} ta):")
        for sana in topilgan_sanalar:
            print(f" - {sana}")
    else:
        print("\n❌ Hech qanday sana topilmadi.")
if __name__ == "__main__":
    sana_extractor()
                
                           
