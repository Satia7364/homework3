class Student:
    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major

s1 = Student("4a1g0199", "林財生", "資工二丁")
s2 = Student("4a1g0015", "陳永祥", "資工三甲")
s3 = Student("4a1g0176", "蕭永順", "資工四丙")
print("學生 : " + s1.name + " ,學號 = " + s1.id + " ,班級 = " + s1.major)
print("學生 : " + s2.name + " ,學號 = " + s2.id + " ,班級 = " + s2.major)
print("學生 : " + s3.name + " ,學號 = " + s3.id + " ,班級 = " + s3.major)
