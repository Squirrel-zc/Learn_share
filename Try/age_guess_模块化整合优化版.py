# -*- coding: utf-8 -*-
import re

def guess_age(true=29,n=5,m=0): # true是正确年龄，n为可猜次数，m为已猜次数

    # 设置年龄范围
    range_begin=true-10
    if range_begin<=0:
        range_begin=1

    range_over=true+10
    if range_over<10:
        range_over=10

    age_range=range(range_begin,range_over+1)  # rang(a,b)不包括b，所以+1

    print('我的年龄范围是：',range_begin,'~',range_over,'\n您有{}次机会'.format(n))

    age_guess_over="\n年龄不是问题，重要的是我们有没有共同语言。\n"\
                 "快面试我吧！见到我,您一定会说:看起来好小,哈哈!!\n"\

    guesslist=[]

    cyc = '猜一猜:'
    qcc = '请重猜:'

    while True:
        # 输入控制模块
        # cyc 必须写入，因为右面的 cyc=qcc 会导致bug
        # UnboundLocalError: local variable 'cyc' referenced before assignment
        # 即：cyc被定义前未被赋值。
        def Input_control(cyc):

            while True:
                print(cyc,end='')
                num=input('')
                try:
                    # 包含‘+-*/’的浮点计算的正则表达式。
                    # r'[^a-zA-Z\u4e00-\u9fa5\\]+' 可以达到同样的效果，
                    # 而且可以继续添加导致except的元素
                    a=re.compile(r'[+-]?(\d+\.?\d*|\d*\.\d+)([+\-*/](\d+\.?\d*|\d*\.\d+))*')
                    b=re.search(a, num)
                    c=b.group()
                    result=round(eval(c))  # eval简单计算后取整

                    if result in age_range:
                        guess=result
                        return guess

                    else:
                        print('您的猜测值为{}，很遗憾，它超出了范围，请输入{}~{}之间的数。'.format(result,range_begin,range_over))
                        cyc=qcc

                except Exception as e:
                    print('您的输入超界，可以输入数字或者包含‘+-*/’的表达式，但不能是文字，谢谢！')
                    cyc=qcc

        guess=Input_control(cyc)

        print('您的猜测为:',guess)

        guesslist.append(guess)

        x=guess-true

        if guess==true:
            if m==0:            # 注意此处m未-1，所以一次猜中时m=0
                print('快去买彩票吧，居然一次就猜中了，但我还是要说:',age_guess_over)
            else:
                print('恭喜您猜中了，但我还是要说:',age_guess_over)
            break

        if guess<true:
            if abs(x)<=2:
                print('我比您猜的年龄大一点点\n')
            else:
                print('我比您猜的要大一些\n')
            n-=1
            m+=1

        else:
            if abs(x)<=2:
                print('我比您猜的年龄小一点点\n')
            else:
                print('我比您猜的年龄小得多\n')
            n-=1
            m+=1

        if n!=0:
            print('您已经猜了{}次,您还有{}次机会。'.format(m,n))

        if n==0:
            print('非常遗憾，{}次机会已经用完！'.format(m))
            print('您的{}次猜测依次为：'.format(m),guesslist)
            print("'松果'虽然不能直接告诉您我的年龄，但是通过您的{}次猜测，"\
                  "'松果'帮您算出了新的年龄范围:".format(m),end='')

            def Centre_screen():  # 新范围模块
                list_x=[i-true for i in guesslist]
                new_guesslist=[]
                l=[]
                h=[]
                for n in list_x:
                    if n<0:
                        l.append(n)
                    if n>0:
                        h.append(n)
                m=max(l)
                new_guesslist.append(m+true)
                s=min(h)
                new_guesslist.append(s+true)
                print(new_guesslist[0],'~',new_guesslist[1])  # 根据猜测值给出新的年龄范围

            Centre_screen()
            print('我想说：',age_guess_over)
            break  # 可猜次数用完结束循环

guess_age()
