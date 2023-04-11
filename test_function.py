import pytest
from calculate_palm import validate_weight,calculate_price

@pytest.mark.parametrize("weight,limit,expected_result", [
    (1000,1000, "น้ำหนักรวมน้อยกว่า0"),
    (2000,2000,"น้ำหนักรวมน้อยกว่า0"),
    (0, 1000, "น้ำหนักรวมน้อยกว่า0"),
    (-500, 1000, "น้ำหนักรวมน้อยกว่า0")
])

def test_validate_weight(weight,limit,expected_result):
    actual_result = validate_weight(weight,limit)
    assert actual_result == expected_result

@pytest.mark.parametrize("weight,limit,price_per_kg, expcted_result",[
    (1000, 1000, 10, "ไม่มีมูลค่า"),
    (2000, 2000, 20, "ไม่มีมูลค่า"),
    (1000, 2000, 15, "ราคาติดลบ"),
    (2000, 1000, 15, "15000 bath"),
    (0, 1000, 10, "ราคาติดลบ"),
    (-500, 1000, 10, "ราคาติดลบ"),
    (1000, 0, 10, "10000 bath"),
    (1000, -500, 10, "15000 bath"),
    (2500, 1200, 50, "65000 bath"),
    (5000, 1200, 50, "น้ำหนักเกินกำหนด น้ำหนักสูงสุดที่อนุญาตคือ 3000 กก."),
    (4500, 1200, 40, "น้ำหนักเกินกำหนด น้ำหนักสูงสุดที่อนุญาตคือ 3000 กก."),
])

def test_calculate_price(weight,limit,price_per_kg,expcted_result):
    actual_result = calculate_price(weight,limit,price_per_kg)
    assert actual_result == expcted_result