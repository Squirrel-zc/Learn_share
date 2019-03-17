# coding-utf-8:

from cent_screen import *

def guess_age(true=29,n=3,c=0): # true是正确年龄，n为可猜次数，c为已猜次数

    range_begin=true-10
    if range_begin<=0:
        range_begin=1

    range_over=true+10
    if range_over<=10:
        range_over=11

    age_range=[range_begin,range_over]

    print('我的年龄范围是：',range_begin,'~',range_over)

    age_guess_over="PS:年龄不是问题，重要的是我们有没有共同语言。\n"\
                 "   不如见见我吧，见到我您一定会说，‘看起来好小啊！’，哈哈!!\n"\
                 "   快面试我吧！"

    guesslist=[]

    while True:

        guess=int(input('猜一猜(请输入整数）：')) #猜测值取整,如果输入非法还需处理

        guesslist.append(guess)

        x=guess-true  #猜测值与真实值的差

        if guess==true:
            if c==0:
                print('您快去买彩票吧，居然一次就猜中了，但我还是要说:',age_guess_over)
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
            print('您已经猜{}次,您还有{}次机会。'.format(c,n))

        if n==0:
            print('非常遗憾，猜测次数已经用完！')
            print('您的{}次猜测依次为：'.format(c),guesslist)
            print("'松果'虽然不能直接告诉您我的年龄，但是通过您的{}次猜测，""'松果'帮您算出了新的年龄范围:".format(c))
            cent_screen(true,guesslist)
            print(age_guess_over)

            break

guess_age()
