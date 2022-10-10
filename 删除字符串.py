from gettext import find

words1=input('请输入字符串1：')
words2=input('请输入要删除的字符：')
s = words1
for i in words2:

    s = s.replace(i, '')

print(s)




