from datetime import datetime

def validate_date(date_str: str) -> str:
    """YYYYMMDD形式の日付が正しいかどうか判定する

    Args:
        date_str (str):検証対象の文字列 

    Returns:
        bool:有効な日付であればTrue、そうでなければFlase 
    """
    try:
        datetime.strptime(date_str, '%Y%m%d')
        return True
    except ValueError:
        return False