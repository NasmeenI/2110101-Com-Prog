def sqrt_n_times(x, n):
    # คืนค่าที่เสมือนการน าค่าใน x มากดปุ่ม  เป็นจ านวน n ครั้ง
    return x**(1/2**n)

def cube_root(y):
    # คืนค่าประมาณของรากที่สามของ y โดยใชวิธี ้ ที่เสมือนการกดปุ่มด้วยสูตร
    #
    # ข้อแนะน า: เรียกใชฟ้ ังกช์ ัน sqrt_n_times
    y = sqrt_n_times(y ,2)
    for i in range(1 ,6):
        y *= sqrt_n_times(y ,2**i)
    return y

def main():
    q = float(input())
    print(cube_root(q))

exec(input()) # DON'T remove this line