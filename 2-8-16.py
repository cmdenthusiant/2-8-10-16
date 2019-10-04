#code by cmdenthusiant
import time
import sys
def main():
    type1 = input("選擇一個模式:\n1.文字轉換\n2.數字轉換\n")
    if type1 == "1":
        type2 = input("選擇一個模式:\n1.文字轉二進制\n2.二進制轉文字\n3.文字轉八進制\n4.八進制轉文字\n5.文字轉十六進制\n6.十六進制轉文字\n")
        if type2 == "1":
            text = input("輸入文字:")
            if text == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_text_to_2(text)
        elif type2 == "2":
            number = input("輸入二進制數字:")
            if number == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_2_to_text(number)
        elif type2 == "3":
            text = input("輸入文字:")
            if text == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_text_to_8(text)
        elif type2 == "4":
            number = input("輸入八進制數字:")
            if number == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_8_to_text(number)
        elif type2 == "5":
            text = input("輸入文字:")
            if text == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_text_to_16(text)
        elif type2 == "6":
            number = input("輸入十六進制數字:")
            if number == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_16_to_text(number)
        else:
            print("[*]你沒有輸入喔...")
            time.sleep(3)
            sys.exit()
    elif type1 == "2":
        type2 = input("選擇一個模式:\n1.十進制轉二進制\n2.二進制轉十進制\n3.十進制轉八進制\n4.八進制轉十進制\n5.十進制轉十六進制\n6.十六進制轉十進制\n")
        if type2 == "1":
            number10 = input("輸入十進制數字:")
            if number10 == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_10_to_2(number10)
        elif type2 == "2":
            number2 = input("輸入二進制數字:")
            if number2 == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_2_to_10(number2)
        elif type2 == "3":
            number10 = input("輸入十進制數字:")
            if number10 == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_10_to_8(number10)
        elif type2 == "4":
            number8 = input("輸入八進制數字:")
            if number8 == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_8_to_10(number8)
        elif type2 == "5":
            number10 = input("輸入十進制數字:")
            if number10 == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_10_to_16(number10)
        elif type2 == "6":
            number16 = input("輸入十六進制數字:")
            if number16 == "":
                print("[*]你沒有輸入喔...")
                time.sleep(3)
                sys.exit()
            change_16_to_10(number16)
        else:
            print("[*]你沒有輸入喔...")
            time.sleep(3)
            sys.exit()
    else:
        print("[*]你沒有輸入喔...")
        time.sleep(3)
        sys.exit()

def change_text_to_2(text):
    """,=分隔"""
    start = 0
    res = ""
    for n in text:
        if start > 0:
            res += ","
        r = bin(ord(n))
        res += r
        start += 1
    print(res)
    repeat()

def change_2_to_text(number):
    """,=分隔"""
    res = ""
    for n in number.split(","):
        r = chr(int(n, 2))
        res += r
    print(res)
    repeat()

def change_text_to_8(text):
    """,=分隔"""
    start = 0
    res = ""
    for n in text:
        if start > 0:
            res += ","
        r = oct(ord(n))
        res += r
        start += 1
    print(res)
    repeat()

def change_8_to_text(number):
    """,=分隔"""
    res = ""
    for n in number.split(","):
        r = chr(int(n, 8))
        res += r
    print(res)
    repeat()

def change_text_to_16(text):
    """,=分隔"""
    start = 0
    res = ""
    for n in text:
        if start > 0:
            res += ","
        r = hex(ord(n))
        res += r
        start += 1
    print(res)
    repeat()

def change_16_to_text(number):
    """,=分隔"""
    res = ""
    for n in number.split(","):
        r = chr(int(n, 16))
        res += r
    print(res)
    repeat()

def change_10_to_2(number10):
    """轉十進制到二進制"""
    res = bin(int(number10))
    print(res)
    repeat()

def change_2_to_10(number2):
    """轉二進制到十進制"""
    res = int(number2, 2)
    print(res)
    repeat()

def change_10_to_8(number10):
    """轉十進制到八進制"""
    res = oct(int(number10))
    print(res)
    repeat()

def change_8_to_10(number8):
    """轉八進制到十進制"""
    res = int(number8, 8)
    print(res)
    repeat()

def change_10_to_16(number10):
    """轉十進制到十六進制"""
    res = hex(int(number10))
    print(res)
    repeat()

def change_16_to_10(number16):
    """轉十六進制到十進制"""
    res = int(number16, 16)
    print(res)
    repeat()

def repeat():
    repeat1 = input("你想繼續換算嗎?\n1.繼續\n2.離開\n")
    if repeat1 == "1":
        main()
    else:
        print("離開中...")
        time.sleep(2)
        sys.exit()

main()