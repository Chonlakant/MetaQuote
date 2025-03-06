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
