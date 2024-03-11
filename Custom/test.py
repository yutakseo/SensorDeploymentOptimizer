import pandas as pd

def excel_to_list(file_path):
    try:
        df = pd.read_excel(file_path, header=None)  # 헤더 없이 엑셀 파일 읽기
        data_list = df.values.tolist()  # 데이터프레임을 2차원 리스트로 변환
        return data_list
    except Exception as e:
        print("Error:", e)
        return None

# 엑셀 파일 경로 설정
excel_file_path = "your_excel_file.xlsx"

# 엑셀 파일을 파이썬 리스트로 변환
result_list = excel_to_list(excel_file_path)

if result_list:
    print("Excel file successfully converted to Python list:")
    for row in result_list:
        print(row)
else:
    print("Failed to convert Excel file to Python list.")
