# AC-BKG-02 (FR-BKG-02)
# Given มีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน
# When จองคิวใหม่ในวันเดียวกัน
# Then ปฏิเสธ และแสดงหมายเลขคิวเดิม
from tests.conftest import AUTH


def test_AC_BKG_02(client, db, make_slot):
    slot = make_slot(start="09:00", remaining=2)

    first = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)
    assert first.status_code == 201

    duplicate = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    assert duplicate.status_code == 409
    payload = duplicate.json()
    assert payload["detail"]["message"] == "มีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน"
    assert payload["detail"]["queue_no"] == "A001"
