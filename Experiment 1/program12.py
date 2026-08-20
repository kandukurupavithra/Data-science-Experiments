import pandas as pd
excel_data = pd.read_excel(
    "College_data.xlsx",
    sheet_name = None
)
print("Available sheets:")
print(excel_data.keys())
print("\nStudent sheet:")
print(excel_data["Students"])
print("\nCourse sheet:")
print(excel_data["Courses"])