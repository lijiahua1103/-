sum=0
money=0
count=0
while True:
    count+=1
    money=input('请输入第%d个商品的金额：'%(count))
    sum+=float(money)
    s=input('请问还需要继续输入金额吗？（Y/N）:')
    #if s=='N'or s=='n':
    if s in 'nN':
        break
print('总计：'+str (int(sum)))
print('总计:%d'%int(sum))
