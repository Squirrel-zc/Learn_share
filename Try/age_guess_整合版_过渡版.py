# -*- coding: utf-8 -*-
import re

def guess_age(true=29,n=5,c=0): # true是正确年龄，n为可猜次数，c为已猜次数

    #设置年龄范围
    range_begin=true-10
    if range_begin<=0:
        range_begin=1

    range_over=true+10
    if range_over<10:
        range_over=10

    age_range=range(range_begin,range_over+1)

    print('我的年龄范围是：',range_begin,'~',range_over,'\n您有{}次机会'.format(n))

    age_guess_over="\n年龄不是问题，重要的是我们有没有共同语言。\n"\
                 "快面试我吧！见到我,您一定会说:看起来好小,哈哈!!\n"\

    guesslist=[]

    while True:

        def Input_control(age_range):

            while True:   #输入控制模块
                num=input('猜一猜:' )
                try:
                    a=re.compile(r'(^-?\d+\.?\d*|\d*\.\d+)+([+\-*/](\d+\.?\d*|\d*\.\d+))*') #包含‘+-*/’的正则表达式
                    b=re.search(a,num)
                    c=b.group()
                    result=round(eval(c)) # eval简单计算后取整

                    if result in age_range:
                        guess=result
                        return (guess)

                    else:
                        print('很遗憾，您的猜测值为{}，它超出了年龄范围，请重新输入！'.format(result))

                except Exception as e:
                    print('您的输入超界，可以输入数字或者包含‘+-*/’的表达式，但不能是文字，谢谢！')
                    while True:  # 输入超界后的循环
                        num=input('请重猜:' )
                        try:
                            a=re.compile(r'(^-?\d+\.?\d*|\d*\.\d+)+([+\-*/](\d+\.?\d*|\d*\.\d+))*')
                            b=re.search(a,num)
                            c=b.group()
                            result=round(eval(c))

                            if result in age_range:
                                guess=result
                                return (guess)

                            else:
                                print('您的输入超出了年龄范围！')

                        except Exception as e:
                            print('您的输入超界，可以输入数字或者包含‘+-*/’的表达式，但不能是文字，谢谢！')

        guess=Input_control(age_range)

        print('您的猜测为:',guess)

        guesslist.append(guess) #加入猜测列表

        x=guess-true  #猜测值与真实值的差

        if guess==true:
            if c==0: # 注意此处c未-1，所以一次猜中时c=0
                print('快去买彩票吧，居然一次就猜中了，但我还是要说:',age_guess_over)
            else:
                print('恭喜您猜中了，但我还是要说:',age_guess_over)
            break

        if guess<true:
            if abs(x)<=2:
                print('我比您猜的年龄大一点点\n')
            else:
                print('我比您猜的要大一些\n')

            n=n-1
            c=c+1

        else:
            if abs(x)<=2:
                print('我比您猜的年龄小一点点\n')
            else:
                print('我比您猜的年龄小得多\n')
            n=n-1
            c=c+1

        if n!=0:
            print('您已经猜了{}次,您还有{}次机会。'.format(c,n))

        if n==0:
            print('非常遗憾，{}次机会已经用完！'.format(c))
            print('您的{}次猜测依次为：'.format(c),guesslist)
            print("'松果'虽然不能直接告诉您我的年龄，但是通过您的{}次猜测，"\
                  "'松果'帮您算出了新的年龄范围:".format(c))
            
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
        
            print(new_guesslist[0],'~',new_guesslist[1])  #根据猜测值给出新的年龄范围

            print('我想说：',age_guess_over)
            break #可猜次数用完结束循环

guess_age()
