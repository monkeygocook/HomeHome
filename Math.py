print("เลือกระบบที่ต้องการใช้ 1 คือ บวก 2 คือ ลบ 3 คือ หาร 4 คือ คูณ")
a = int(input("ใส่ตัวเลขระบบ = "))
print("\n")
if a == 1:
    b = int(input("ใส่ตัวเลขที่ต้องการ = "))
    c = int(input("ใส่ตัวเลขที่ต้องการ = "))
    d = b + c
if a == 2:
    b = int(input("ใส่ตัวเลขที่ต้องการ = "))
    c = int(input("ใส่ตัวเลขที่ต้องการ = "))
    d = b - c    
if a == 3:
    b = int(input("ใส่ตัวเลขที่ต้องการ = "))
    c = int(input("ใส่ตัวเลขที่ต้องการ = "))
    d = b / c
if a ==4:
    b = int(input("ใส่ตัวเลขที่ต้องการ = "))
    c = int(input("ใส่ตัวเลขที่ต้องการ = "))
    d = b * c

print("เลขที่ได้คือ =", d )
print("\n")
e = int(input("ใส่ตัวเลขเพื่อเลือกระบบ 1 เพื่อ หาพื้นที่สี่เหลี่ยม 2 เพื่อหาพื้นที่ สามเหลี่ยม = "))

if e == 1:
    f = int(input("ใส่ตัวเลขที่ต้องการ = "))
    g = int(input("ใส่ตัวเลขที่ต้องการ =  "))
    h = f * g 
    print("ค่าที่ได้คือ = ", h)
if e == 2:
    f = int(input("ใส่ตัวเลขที่ต้องการ =  "))
    g = int(input("ใส่ตัวเลขที่ต้องการ = "))
    h = 0.5*f*g
    print("ค่าที่ได้คือ = ", h)