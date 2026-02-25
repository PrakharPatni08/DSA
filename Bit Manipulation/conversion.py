def convert2Binary(num:int) -> str:
    result = ""
    while num > 0:
        if num%2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2
    result = result[::-1]
    return result

def convert2Decimal(x:str) -> int:
    decimal_number = 0
    power = 0
    index = len(x) - 1
    while index >= 0:
        num = int(x[index]) * (2**power)
        decimal_number += num
        index -= 1
        power += 1
    return decimal_number

if __name__ == "__main__":
    decimal = int(input("Enter a Decimal Number to Convert to Binary:"))
    print(convert2Binary(decimal))
    binary = str(input("Enter a Binary Number to Convert to Decimal:"))
    print(convert2Decimal(binary))