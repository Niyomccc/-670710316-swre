# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 12:00 | test: 6 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | backend/tests/test_AC_BKG_05.py: test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 | backend/app/booking/service.py: create_booking, get_active_booking_same_day; backend/app/booking/router.py: create_booking | backend/tests/test_AC_BKG_02.py: test_AC_BKG_02 (ผ่าน) | ครบ |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่พบการแจ้ง "ช่วงเวลาเต็ม" พร้อมตัวเลือก 3 ช่วงและไม่สร้างรายการจอง | ไม่มี | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/service.py: next_queue_no, create_booking; backend/app/booking/router.py: create_booking | backend/tests/test_AC_BKG_01.py: test_AC_BKG_01 (ผ่าน) | รอ Q-xx |
| FR-BKG-05 | AC-BKG-04 | T-07 | ไม่พบรายการค้างส่ง / retry queue / audit ของการส่งซ้ำ | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-02, T-10 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | backend/tests/test_AC_BKG_05.py: test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | backend/tests/test_AC_BKG_05.py: test_AC_BKG_05 (ผ่าน) | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มีการตั้งค่า HTTPS/TLS หรือ secure transport ในโค้ด | ไม่มี | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | ไม่พบ loop ของการส่งซ้ำภายใน 5 นาที | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มีการทดสอบผู้ใช้ใหม่ 8 ใน 10 คน | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL | ไม่มี | ครบ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | ไม่พบ audit middleware หรือการบันทึก audit log | ไม่มี | ช่องโหว่ |
| IF-IDP-01 | ไม่มี AC | T-03 | backend/app/auth/idp.py: get_verified_hn | backend/tests/test_AC_BKG_01.py: test_AC_BKG_01 (ผ่าน) | ครบ |
| IF-HIS-01 | ไม่มี AC | T-09 | backend/app/db/models.py: Booking เก็บเฉพาะ hn แต่ไม่มีการค้นจาก HIS / no client | ไม่มี | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 | ไม่พบคิวส่งข้อความ หรือ retry queue ตาม ASM-03 | ไม่มี | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/router.py: get_slots | FR-BKG-01, FR-BKG-06 | บางส่วน | ใช้ package_code และ date_from ได้ดี แต่กำหนดช่วงเวลาล่วงหน้า 14 วัน ไม่ตรงกับ "ภายใน 30 วันข้างหน้า" ใน FR-BKG-01 |
| backend/app/booking/router.py: create_booking | FR-BKG-02, FR-BKG-04 | ใช่ (บางส่วน) | ปฏิเสธการจองซ้ำวันเดียวกันแล้ว แต่หมายเลขคิวยังใช้รูปแบบ A001 ที่ยังไม่ผ่าน Q-02 |
| backend/app/booking/router.py: cancel_booking | Out of scope | ไม่ | เป็นฟีเจอร์ยกเลิก/เลื่อนคิว ซึ่งอยู่ใน Out of scope ของ spec |
| backend/app/auth/idp.py: get_verified_hn | IF-IDP-01 | ใช่ | ตรวจ Authorization header และ 401 ถ้ายังไม่ยืนยันตัวตนตาม requirement |
| backend/app/config.py: DATABASE_URL | CON-TECH-01 | ใช่ | ตั้งค่าเป็น PostgreSQL ในระบบจริง และโค้ดให้สลับค่าได้ด้วย env var |
| backend/app/booking/service.py: next_queue_no | Q-02, FR-BKG-04 | ไม่ | กำหนด A001 และรีเซ็ตทุกวัน เป็นการเดาใน Open Question Q-02 โดยไม่รอคำตอบจากเจ้าหน้าที่เวชระเบียน |
| backend/app/db/models.py: Booking | IF-HIS-01 | บางส่วน | เก็บ hn อย่างเดียว แต่ไม่มีการค้นข้อมูลจาก HIS หรือการเชื่อมกับเลขบัตรประชาชน |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-01 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py: list_available_slots | FR-BKG-01 | โค้ดใช้ DAYS_AHEAD = 14 แต่ spec ระบุภายใน 30 วันข้างหน้า | แก้โค้ด |
| F-02 | เดา Q-xx | backend/app/booking/service.py: next_queue_no | Q-02, FR-BKG-04 | โค้ดกำหนด A001 และรีเซ็ตทุกวัน แม้ Q-02 ยังไม่ได้คำตอบจากเจ้าหน้าที่เวชระเบียน | เพิ่ม Q-xx |
| F-03 | FR ไม่มี AC | backend/app/slots/router.py: get_slots | FR-BKG-06 | FR-BKG-06 มี requirement แต่ไม่มี AC เพื่อตรวจความถูกต้องของการเปลี่ยนแพ็กเกจ | แก้ spec |
| F-04 | โค้ดไม่มี FR | backend/app/booking/router.py: cancel_booking | Out of scope | DELETE /bookings/{booking_id} เป็นฟีเจอร์ยกเลิก/เลื่อนคิว ซึ่งอยู่ใน Out of scope | ไม่ใช่ปัญหา |
| F-05 | ละเมิด Constraint | backend/app/main.py, backend/app/booking/router.py | DOM-PDPA-01 | ไม่มี audit middleware หรือบันทึก audit log ในทุกการเข้าถึงข้อมูลการจอง แม้ requirement ระบุชัด | แก้โค้ด |
| F-06 | AC ไม่มี test | backend/tests/test_AC_BKG_01.py | AC-BKG-01 | Test ปัจจุบัน assert 201 อย่างเดียว ไม่ตรวจว่า "แสดงหมายเลขคิว" และ "ที่นั่งว่างของช่วงนั้นเป็น 0" ตาม Then ของ AC | แก้โค้ด |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| - | ไม่มีข้อค้นพบเดิมจากรอบก่อนที่ถูกแก้แล้วในเวอร์ชันนี้ | ทดสอบผิวเผินยังไม่มีข้อค้นพบที่จบแล้วในโค้ดปัจจุบัน |
