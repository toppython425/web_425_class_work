import re

# reg_1 = re.compile('course.topic.part.a')
# string_1 = """course/topic/part/a"""
# string_1_1 = """course$topic$part$a"""
# print(bool(reg_1.match(string_1)))
# print(bool(reg_1.match(string_1_1)))
#
# reg_2 = re.compile(r'course\d\d')
# string_2 = """course12"""
# print(bool(reg_2.match(string_2)))
#
# reg_3 = re.compile(r'part\D001')
# string_3 = """part@001"""
# print(bool(reg_3.match(string_3)))
#
# reg_4 = re.compile(r'user\s24')
# string_4 = """user\n24"""
# print(bool(reg_4.match(string_4)))
#
# reg_5 = re.compile(r'Bond\S007')
# string_5 = """Bond-007 agent"""
# print(bool(reg_5.match(string_5)))
#
# reg_6 = re.compile(r'\w\w555')
# # reg_6 = re.compile('\\w\\w555')
# string_6 = 'a_555'
# print(bool(reg_6.match(string_6)))
#
# reg_7 = re.compile(r'Python\W')
# string_7 = 'Python!'
# print(bool(reg_7.match(string_7)))
#

# reg_8 = re.compile(r'[0-5][A-Ca-c]')
# reg_8 = re.compile(r'[0-5A-Ca-c]')
# reg_8 = re.compile(r'[0-5,A-Ca-c]')
# string_8 = '012345CBAcba'
# print(bool(reg_8.match(string_8)))
#
# reg_9 = re.compile(r'\([^B-Db-d]\)')
# string_9 = """(G)"""
# print(bool(reg_9.match(string_9)))

# reg_10 = re.compile(r'student\d{5}')
# string_10 = """student67890"""
# print(bool(reg_10.match(string_10)))
#
# reg_11 = re.compile(r'student\d{3,5}')
# string_11 = """student12345678"""
# print(bool(reg_11.match(string_11)))
#
# reg_12 = re.compile(r'student\d{3,}')
# string_12 = """student123456"""
# print(bool(reg_12.match(string_12)))
#
# reg_13 = re.compile(r'student\d{,2}')
# string_13 = """student12"""
# print(bool(reg_13.match(string_13)))
#
# reg_14 = re.compile('come?')
# string_14 = 'coming'
# print(bool(reg_14.match(string_14)))
#
# reg_15 = re.compile(r'user\d+')
# string_15 = 'user112346'
# print(bool(reg_15.match(string_15)))
