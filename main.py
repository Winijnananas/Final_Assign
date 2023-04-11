from calculate_palm import validate_weight
from calculate_palm import calculate_price
from calculate_palm import display_price

while True:
    weight_with_palm_oil = float(input("ใส่น้ำหนักของน้ำมันปาล์มกับยานพาหนะเป็นกิโลกรัม:" ))
    weight_empty = float(input("ใส่น้ำหนักของรถเปล่าเป็นกิโลกรัม: "))
    price_per_kg=float(input("ป้อนราคาน้ำมันปาล์มต่อกิโลกรัม: "))
    if weight_with_palm_oil >=0 and weight_empty >=0 and price_per_kg >=0:
        break
    print("กรุณากรอกเลขที่ไม่ติดลบ")



result = display_price(weight_with_palm_oil,weight_empty,price_per_kg)
if validate_weight(weight_with_palm_oil,weight_empty):
    price = calculate_price(weight_with_palm_oil,weight_empty,price_per_kg)
    print(f"น้ำหนักรวมของน้ำมันปาล์มคือ {weight_with_palm_oil - weight_empty} กก.และมีราคา {price} บาท")
else:
    print("น้ำหนักเกินกำหนด น้ำหนักสูงสุดที่อนุญาตคือ 3000 กก.")
    print(result)