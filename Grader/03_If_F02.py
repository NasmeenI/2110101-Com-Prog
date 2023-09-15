def choose(stu1, stu2):
    id_1 = stu1[0]
    GPAX_1 = stu1[1]
    comprog_1 = stu1[2]
    cal1_1 = stu1[3]
    cal2_1 = stu1[4]

    id_2 = stu2[0]
    GPAX_2 = stu2[1]
    comprog_2 = stu2[2]
    cal1_2 = stu2[3]
    cal2_2 = stu2[4]

    if (comprog_1 == 'A' and ('A' <= cal1_1 <= 'C') and ('A' <= cal2_1 <= 'C')) and (comprog_2 == 'A' and ('A' <= cal1_2 <= 'C') and ('A' <= cal2_2 <= 'C')):
        if(GPAX_1 == GPAX_2):
            if cal1_1 == cal1_2:
                if cal2_1 == cal2_2:
                    return [id_1 ,id_2]
                elif cal2_1 > cal2_2:
                    return [id_2]
                elif cal2_1 < cal2_2:
                    return [id_1]

            elif cal1_1 > cal1_2:
                return [id_2]
            elif cal1_1 < cal1_2:
                return [id_1]
        elif (GPAX_1 > GPAX_2):
            return [id_1]
        elif (GPAX_2 > GPAX_1):
            return [id_2]
    elif (comprog_1 == 'A' and ('A' <= cal1_1 <= 'C') and ('A' <= cal2_1 <= 'C')):
        return [id_1]
    elif (comprog_2 == 'A' and ('A' <= cal1_2 <= 'C') and ('A' <= cal2_2 <= 'C')):
        return [id_2]
    else:
        return []
    # stu1 และ stu2 เป็นลิสต์[ ID, GPAX, compprog, cal1, cal2 ]
    # ID เป็นสตริงเก็บเลขประจ ำตัว
    # GPAX เป็น float
    # comprog, cal1, cal2 เป็นสตริงเก็บเกรดของสำมวิชำ (เกรดเป็นแบบไม่มีประจุ A,B,C,D,F)
    # ฟังกช์ ันนี้คนื
    # - ถ้ำไม่ผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ว่ำง
    # - ถ้ำผ่ำนเกณฑ์ข้อ 1 คนเดียว คืนลิสต์ที่เก็บเลขประจ ำตัวของคนที่ผ่ำนเกณฑ์ข้อ 1
    # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ ที่มีข้อ 2 ที่ดีกว่ำ
    # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ และมีข้อ 2 เท่ำกัน คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ คนแรก ตำมด้วยของคนที่สอง

exec(input()) # DON'T remove this line