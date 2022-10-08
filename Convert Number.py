# Convert Binary to Decimal and vice versa
import math


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(binary1,"in decimal = ",decimal)

# nhập vào số thập phân
def decimalToBinary(decimal):
    print(decimal,"in binary = ",bin(decimal).replace("0b", ""))
# nhập vào số thập phân
def decimalToOctal(decimal):
    print(decimal,"in octal = ",oct(decimal).replace("0o", ""))
# nhập vào số thập phân
def decimalToHexadecimal(decimal):
    print(decimal,"in hexadecimal = ",hex(decimal).replace("0x", ""))
# nhập vào số thập lục phân
def hexadecimalToDecimal(hexadecimal):
    print(hexadecimal,"in decimal = ",int(hexadecimal, 16))
# nhập vào số thập lục phân
def hexadecimalToBinary(hexadecimal):
    print(hexadecimal,"in binary = ",bin(int(hexadecimal, 16)).replace("0b", ""))
# nhập vào số thập lục phân
def hexadecimalToOctal(hexadecimal):
    print(hexadecimal,"in octal = ",oct(int(hexadecimal, 16)).replace("0o", ""))
# nhập vào số bát phân
def octalToDecimal(octal):
    print(octal,"in decimal = ",int(octal, 8))
# nhập vào số bát phân
def octalToBinary(octal):
    print(octal,"in binary = ",bin(int(octal, 8)).replace("0b", ""))
# nhập vào số bát phân
def octalToHexadecimal(octal):
    print(octal,"in hexadecimal = ",hex(int(octal, 8)).replace("0x", ""))

# chương trình chính
print("Chọn chuyển đổi:")
print("1. Nhị phân sang thập phân")
print("2. Thập phân sang nhị phân")
print("3. Thập phân sang bát phân")
print("4. Thập phân sang thập lục phân")
print("5. Thập lục phân sang thập phân")
print("6. Thập lục phân sang nhị phân")
print("7. Thập lục phân sang bát phân")
print("8. Bát phân sang thập phân")
print("9. Bát phân sang nhị phân")
print("10. Bát phân sang thập lục phân")
choice = input("Nhập lựa chọn của bạn (1/2/3/4/5/6/7/8/9/10): ")

if choice == '1':
    binaryToDecimal(int(input("Nhập số nhị phân: ")))
elif choice == '2':
    decimalToBinary(int(input("Nhập số thập phân: ")))
elif choice == '3':
    decimalToOctal(int(input("Nhập số thập phân: ")))
elif choice == '4':
    decimalToHexadecimal(int(input("Nhập số thập phân: ")))
elif choice == '5':
    hexadecimalToDecimal(input("Nhập số thập lục phân: "))
elif choice == '6':
    hexadecimalToBinary(input("Nhập số thập lục phân: "))
elif choice == '7':
    hexadecimalToOctal(input("Nhập số thập lục phân: "))
elif choice == '8':
    octalToDecimal(input("Nhập số bát phân: "))
elif choice == '9':
    octalToBinary(input("Nhập số bát phân: "))
elif choice == '10':
    octalToHexadecimal(input("Nhập số bát phân: "))
else:
    print("Lựa chọn không hợp lệ")

# End of file