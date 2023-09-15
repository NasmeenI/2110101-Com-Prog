def is_mobile_number(number):
    # number เป็นสตริงเก็บหมายเลข (ภายในสตริงมีแต่ตัวเลขแน่ ๆ)
    # คืน True ถ้า number เป็นหมายเลขโทรศัพท์ถา้ไม่เป็น คืน False
    if len(number) == 10 and (number[0:2]=="06" or number[0:2]=='08' or number[0:2]=='09'):
        return True
    else:
        return False

exec(input()) # DON'T remove this line