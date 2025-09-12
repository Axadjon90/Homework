1) import os
import subprocess
import sys
venv_name = "venv"
packages = ["tabulate", "colorama"]
print(f"[1] Virtual muhit yaratilmoqda: ./{venv_name}")
subprocess.run([sys.executable, "-m", "venv", venv_name])
pip_path = os.path.join(venv_name, "Scripts", "pip.exe") if os.name == "nt" else os.path.join(venv_name, "bin", "pip")
print(f"[2] Paketlar ornatilmoqda: {', '.join(packages)}")
subprocess.run([pip_path, "install"] + packages)
print("[3] requirements.txt yaratilmoqda...")
with open("requirements.txt", "w") as f:
    subprocess.run([pip_path, "freeze"], stdout=f)
print("\n✅ Tayyor! Virtual muhit yaratildi va paketlar ornatildi.")
print(f"➡️ Faollashtirish uchun terminalda quyidagini yozing:")
if os.name == "nt":
    print(f"   {venv_name}\\Scripts\\activate")
else:
    print(f"   source {venv_name}/bin/activate")
[1] Virtual muhit yaratilmoqda: ./venv
[2] Paketlar ornatilmoqda: tabulate, colorama
[3] requirements.txt yaratilmoqda...

✅ Tayyor! Virtual muhit yaratildi va paketlar ornatildi.
➡️ Faollashtirish uchun terminalda quyidagini yozing:
   venv\Scripts\activate

2)def qoshish(a, b):
    return a + b
def ayirish(a, b):
    return a - b
def bolish(a, b):
    if b == 0:
        return "Xatolik: Nolga bolish mumkin emas!"
    return a / b
def teskari_string(s):
    return s[::-1]
def scrub_vowels(s):
    vowels = "qwertyuiopasdfghjklzxcvbnm"
    return ''.join(char for char in s if char not in vowels)
from math_pere_operatsiyalari import qoshish, ayirish, bolish
from string_util import teskari_string, scrub_vowels
print("5 + 3 =", qoshish(5, 3))
print("10 - 4 =", ayirish(10, 4))
print("8 / 2 =", bolish(8, 2))
print("8 / 0 =", bolish(8, 0))
s = "Salom Dunyo"
print("Teskari:", teskari_string(s))
print("Unlilarsiz:", scrub_vowels(s))

3)import math

def hisoblash_area(radius):
    """Aylananing yuzasini hisoblaydi"""
    return math.pi
  
