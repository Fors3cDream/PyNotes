import re

line = "Fooooooosooos34445c123ccc"

#regex_str = ".*(F.*c).*" # 贪婪匹配，匹配到最后一个
#regex_str = ".*?(F.*?s).*" # 非贪婪匹配，匹配到第一个就停止
regex_str = ".*(s.+?c).*"

match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))

num = '13157002246'
#reg_num = '(1[345789][0-9]{9})'
reg_num = '(1\d{10})'
match_num = re.match(reg_num, num)

if match_num:
    print(match_num.group(1))

# Unicode 编码匹配
# [\u4E00  - \u9FA5]
str_ = "你好"
reg_str = "([\u4E00-\u9FA5]+)"
match_str = re.match(reg_str, str_)
if match_str:
    print(match_str.group(1))

str_1 = "study in 成都理工大学"
reg_str1 = ".*?([\u4E00-\u9FA5]+)大学"
match_str1 = re.match(reg_str1, str_1)
if match_str1:
    print(match_str1.group(1))

test = "XXX出生于1989年6月1日"
test1 = "XXX出生于1989/6/1"
test2 = "XXX出生于1989-6-1"
test3 = "XXX出生于1989-06-01"
test4 = "XXX出生于1989-06"

regx = ".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}(日|$)|[月/-]$|$))"
matchs = re.match(regx, test4)

if matchs:
    print(matchs.group(1))
