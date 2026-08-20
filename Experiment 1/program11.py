import pandas as pd
Student_data = {
    "Roll-No": [101, 102, 103],
    "Name": ["Anusha", "Babitha", "charitha"],
    "Department": ["IT", "IT", "CSE"],
    "Percentage": [89, 92, 88]
}
course_data = {
    "Course-ID": ["c101","c102","c103"],
    "Instructor": ["Anusha", "Babitha", "charitha"],
    "Department": ["IT", "IT", "CSE"],
    "Credits": [4, 3,4]
}
Students_df = pd.DataFrame(Student_data)
Courses_df = pd.DataFrame(course_data)
with pd.ExcelWriter("College_data.xlsx",engine="openpyxl") as writer:
    Students_df.to_excel(writer,
                         sheet_name = "Students",
                         index = False
                         )
    Courses_df.to_excel(writer,
                        sheet_name = "Courses",
                        index = False
                        )
    print("Multiple sheets successfully written to College_data.xlsx")