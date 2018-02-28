import random

from PIL import Image, ImageDraw, ImageFont


class VertifyCode():
    def __init__(self):
        self.codes = 'ABCDEFGHJKLMNPQRSTWXYZ23456789'

    #生成验证码(返回值是一个列表)
    def randChars(self):

        return random.sample(self.codes,4)

    #创建一副图片
    def create_pic(self):
        #画布
        img = Image.new('RGB',(80,20),(0,0,0))
        #画笔
        paint = ImageDraw.Draw(img)
        #利用画笔在画布上绘制
        codes = self.randChars()

        #以下代码在ｗｉｎｄｏｗｓ下通过，在ｕｂｕｎｔｕ下不行
        #font = ImageFont.truetype('calibri.ttf',size=36)

        for idx in range(4):

            #paint.text((idx*20,5),codes[idx],fill=(255,255,255),font=font)
            paint.text((idx*20,5),codes[idx],fill=(255,255,255))


        #把绘制好的画布返回
        return img,''.join(codes)

