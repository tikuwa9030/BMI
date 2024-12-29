from conversion import convert_to_japanese_era
from validation import validate_date


def main():
    print("西暦年月日を和暦年月日に変換します。")
    calender = input("和暦にしたい西暦年月日を入力してください。(半角数字YYYYMMDDで入力):")

    if not validate_date(calender):
        print("日付が正しくありません")
        return

    year = int(calender[0:4])
    if year >= 2019:
        result = convert_to_japanese_era(calender, 2019, "令和")
    elif year >= 1989:
        result = convert_to_japanese_era(calender, 1989, "平成")
    else:
        result = "昭和より古い西暦は変換対象外です。"

    print(f"年号表記：{result}")


if __name__ == "__main__":
    main()