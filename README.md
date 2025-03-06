# ติดตั้ง Python บน macOS และ Windows

## ติดตั้ง Python บน macOS

### 1. ตรวจสอบว่าเครื่องมี Python หรือไม่
เปิด Terminal และพิมพ์:
```
python3 --version
```
ถ้าแสดงเวอร์ชันของ Python แสดงว่ามีการติดตั้งแล้ว

### 2. ติดตั้ง Python ผ่าน Homebrew (แนะนำ)
- ติดตั้ง Homebrew (ถ้ายังไม่มี)
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
- ติดตั้ง Python
  ```
  brew install python  
  ```
- ตรวจสอบเวอร์ชัน
  ```
  python3 --version
  ```

### 3. ติดตั้ง Python ผ่านตัวติดตั้งจากเว็บไซต์
- ดาวน์โหลดตัวติดตั้งจาก [Python.org](https://www.python.org/downloads/mac-osx/)
- เปิดไฟล์ `.pkg` และทำตามขั้นตอนการติดตั้ง
- ตรวจสอบการติดตั้งด้วย
  ```
  python3 --version
  ```

---

## ติดตั้ง Python บน Windows

### 1. ดาวน์โหลดตัวติดตั้ง
- ไปที่ [Python.org](https://www.python.org/downloads/windows/)
- ดาวน์โหลด **Windows Installer (64-bit)**

### 2. ติดตั้ง Python
- เปิดไฟล์ `.exe` ที่ดาวน์โหลดมา
- **ติ๊กเลือก** `Add Python to PATH` (สำคัญ!)
- คลิก **Install Now** และรอให้ติดตั้งเสร็จ

### 3. ตรวจสอบการติดตั้ง
- เปิด **Command Prompt (cmd)** แล้วพิมพ์
  ```
  python --version
  ```
  หรือ
  ```
  python3 --version
  ```

---

## ติดตั้ง Pip (เครื่องมือจัดการแพ็กเกจของ Python)
Python จะติดตั้ง `pip` มาให้แล้ว สามารถตรวจสอบได้โดย
```
pip --version
```
ถ้ายังไม่มี ให้ติดตั้งด้วย
```
python -m ensurepip --default-pip
```

---

## ติดตั้ง Virtual Environment (แนะนำสำหรับการพัฒนาโปรเจกต์)
สร้าง Virtual Environment ด้วยคำสั่ง
```
python -m venv myenv
```
จากนั้นเปิดใช้งาน:
- **macOS / Linux**
  ```
  source myenv/bin/activate
  ```
- **Windows**
  ```
  myenv\Scripts\activate
  ```

เมื่อเปิดใช้งาน Virtual Environment แล้ว สามารถติดตั้งแพ็กเกจ Python ได้โดยใช้ `pip install <package>`

---

## สรุปคำสั่งหลักที่ต้องใช้

| คำสั่ง | macOS | Windows |
|---------|------------|---------|
| ตรวจสอบเวอร์ชัน Python | `python3 --version` | `python --version` หรือ `python3 --version` |
| ติดตั้งผ่านแพ็กเกจจัดการ | `brew install python` | - |
| ติดตั้งผ่านเว็บไซต์ | ดาวน์โหลด `.pkg` และติดตั้ง | ดาวน์โหลด `.exe` และติดตั้ง |
| ตรวจสอบเวอร์ชัน Pip | `pip --version` | `pip --version` |
| สร้าง Virtual Environment | `python3 -m venv myenv` | `python -m venv myenv` |
| เปิดใช้งาน Virtual Environment | `source myenv/bin/activate` | `myenv\Scripts\activate` |

---

🎯 **ตอนนี้ Python พร้อมใช้งานแล้ว!** สามารถเริ่มพัฒนาโปรเจกต์ Python ได้ทันที 🚀

---

## ติดตั้ง Dependencies จาก `requirements.txt`

หากมีไฟล์ `requirements.txt` ที่ระบุแพ็กเกจที่ต้องการ สามารถติดตั้งได้โดยใช้คำสั่ง:

```
pip install -r requirements.txt
```

คำสั่งนี้จะติดตั้งทุกแพ็กเกจที่ระบุไว้ในไฟล์ `requirements.txt`

---

🎯 **ตอนนี้ Python พร้อมใช้งานแล้ว!** สามารถเริ่มพัฒนาโปรเจกต์ Python ได้ทันที 🚀

#---------------------------------------------------------------------#
#---------------------------------------------------------------------#

# Token Arbitrage Monitor

## 🔍 เกี่ยวกับโปรเจกต์
บอทนี้ใช้ **Odos** และ **Universal Assets (UA)** เพื่อหากำไรจากส่วนต่างราคา (Arbitrage) โดย:

1. **ซื้อโทเค็น** จาก Odos ด้วย 1000 USDC
2. **ขายคืน** ที่ UA เพื่อรับ USDC กลับมา
3. **เปรียบเทียบราคา** หากได้กำไรมากกว่า 1 USDC บอทจะแจ้งเตือนผ่าน Telegram

---

## 🏗 โครงสร้างโค้ด

- `TOKEN_INFO` 🔹 รายละเอียดโทเค็น เช่น Address, Decimals, Threshold
- `DatabaseManager` 🗄 จัดการฐานข้อมูล PostgreSQL
- `send_telegram_message` ✉ ส่งแจ้งเตือนกำไรไปยัง Telegram
- `get_odos_quotes` 📊 ขอราคาซื้อโทเค็นจาก Odos
- `get_universal_quotes` 🔄 ขอราคาขายคืนจาก UA
- `check_opportunities` ✅ ตรวจสอบโอกาสทำกำไร
- `run_monitor` 🔁 ลูปหลักที่ทำงานตลอดเวลา

---

## 🛠 วิธีติดตั้งและใช้งาน

### 1️⃣ ติดตั้ง Python และ Dependencies

ติดตั้ง Python และแพ็กเกจที่จำเป็น

```sh
pip install -r requirements.txt
```

### 2️⃣ ตั้งค่าตัวแปรสำคัญ

- `BOT_TOKEN` -> ใส่ API Token ของ Telegram Bot
- `CHAT_ID` -> ใส่ Chat ID สำหรับรับการแจ้งเตือน

### 3️⃣ รันบอท

```sh
python main.py
```

---

## ⚡ ตัวอย่างการแจ้งเตือน

เมื่อพบโอกาสทำกำไร บอทจะแจ้งเตือนผ่าน Telegram เช่น:

```
🔄 Arbitrage Opportunity!
💱 uSOL (Solana Token):
• Input USDC: 1000
• Output USDC: 1020.50
• Profit: $20.50 (2.05%)
```

---

🎯 **บอทนี้ช่วยให้คุณหาโอกาส Arbitrage ได้อัตโนมัติ! 🚀**
