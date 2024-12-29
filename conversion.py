# -*- coding: utf-8 -*-

def convert_to_japanese_era(
    w_calender: str, 
    start_year: int, 
    era_name: str
) -> str:
    """
    西暦を和暦に変換する

    Args:
        w_calender (str): YYYYMMDD形式の西暦
        start_year (int): 年号の開始年（例 平成は1989年）
        era_name (str): 元号名

    Returns:
        result: 和暦
    """
    # 判定処理で使えるよう、年と月日を分離
    year: int = int(w_calender[0:4])
    month_day: str = w_calender[4:]
    
    temp_yy: int = year - start_year + 1
        
    # 変換処理（西暦 -> 和暦）
    if temp_yy == 1:
        era_year: str = "元"
    else:
        era_year = str(temp_yy)
    
    result = f'{era_name}{era_year}年{month_day[0:2]}月{month_day[2:4]}日'

    return result
