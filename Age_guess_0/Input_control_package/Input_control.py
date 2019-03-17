# -*- coding: utf-8 -*-
import re

def Input_control(age_range):

    while True:
        num=input('猜一猜:' )
        try:
            a=re.compile(r'(^-?\d+\.?\d*|\d*\.\d+)+([+\-*/](\d+\.?\d*|\d*\.\d+))*') #包含‘+-*/’的正则表达式
            b=re.search(a, num)
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
                    b=re.search(a, num)
                    c=b.group()
                    result=round(eval(c))

                    if result in age_range:
                        guess=result
                        return (guess)
                    else:
                        print('您的输入超出了年龄范围！')

                except Exception as e:
                    print('您的输入超界，可以输入数字或者包含‘+-*/’的表达式，但不能是文字，谢谢！')
