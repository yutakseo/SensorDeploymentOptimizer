from datetime import datetime
import sys
import os
import pandas as pd

output_directory = os.path.join(os.path.dirname(__file__), "OUTPUT")

def to_xlsx(data):
    df = pd.DataFrame(data)
    current_time = datetime.now()
    formatted_datetime = current_time.strftime('%y%m%d')
    excel_filename = f"{formatted_datetime}_output.xlsx"
    df.to_excel(os.path.join(output_directory, excel_filename), index=False)

    return None
