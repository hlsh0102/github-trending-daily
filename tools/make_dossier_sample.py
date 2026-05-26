from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random

ROOT = Path.cwd()
OUT = ROOT / 'vault' / 'Inno' / 'GithubTrending' / '2026-05-26' / 'douyin' / 'dossier-sample-01.png'
W,H = 1080,1920
FONT_BOLD='C:/Windows/Fonts/msyhbd.ttc'
FONT_REG='C:/Windows/Fonts/msyh.ttc'

def ft(path,size): return ImageFont.truetype(path,size=size)
F={
 'tiny':ft(FONT_REG,24),'small':ft(FONT_REG,30),'body':ft(FONT_REG,36),
 'h':ft(FONT_BOLD,46),'title':ft(FONT_BOLD,96),'title2':ft(FONT_BOLD,88),
 'mega':ft(FONT_BOLD,122),'stamp':ft(FONT_BOLD,40)
}

# Background: warm dark editorial desk
img=Image.new('RGB',(W,H),'#100d0b')
px=img.load()
for y in range(H):
    for x in range(W):
        dx=x/W; dy=y/H
        r=int(16+32*dy+12*math.sin(dx*math.pi))
        g=int(13+18*dy)
        b=int(11+13*(1-dy))
        px[x,y]=(r,g,b)
img=img.convert('RGBA')
d=ImageDraw.Draw(img,'RGBA')

# subtle paper grain
random.seed(8)
for _ in range(9000):
    x=random.randrange(W); y=random.randrange(H)
    a=random.randrange(8,22)
    col=(255,245,220,a) if random.random()<0.5 else (0,0,0,a)
    d.point((x,y),fill=col)

# table spotlight
def glow(cx,cy,rx,ry,color,alpha,blur):
    lay=Image.new('RGBA',(W,H),(0,0,0,0)); dd=ImageDraw.Draw(lay,'RGBA')
    dd.ellipse([cx-rx,cy-ry,cx+rx,cy+ry],fill=color+f'{alpha:02x}')
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(blur)))

glow(510,760,520,480,'#b8894b',55,130)
glow(900,350,320,280,'#d84d2f',45,120)

# dossier sheet rotated-ish polygon shadow and sheet
shadow=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(shadow,'RGBA')
sheet=[(86,248),(820,156),(994,1398),(224,1498)]
sd.polygon([(x+18,y+20) for x,y in sheet], fill='#00000090')
img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
d.polygon(sheet, fill='#eee1c8', outline='#ffffff88')
# sheet lines
for i in range(0,17):
    y=330+i*58
    d.line([(150,y),(885,y-88)], fill='#4a332022', width=2)

# red file tab and stamps
d.rounded_rectangle([92,200,418,282], radius=12, fill='#e4362d', outline='#ffddd7', width=2)
d.text((116,220),'今日 TOP 01',font=F['stamp'],fill='#fff3ed')
d.rounded_rectangle([650,178,930,250], radius=10, fill='#1c1712', outline='#d9c5a1', width=2)
d.text((678,195),'GitHub Trending',font=F['small'],fill='#e8d8bd')

# Main headline on sheet
def stroke(x,y,text,font,fill,sw=3):
    d.text((x,y),text,font=font,fill=fill,stroke_width=sw,stroke_fill='#2a140f')

stroke(132,350,'这个工具',F['title'],'#17110d',2)
stroke(132,462,'能读懂',F['title'],'#17110d',2)
stroke(132,574,'整个代码库',F['title2'],'#c82118',2)

# subtitle highlight
d.rounded_rectangle([132,704,766,780], radius=8, fill='#ffe36b')
d.text((154,720),'把源码变成可提问知识地图',font=F['h'],fill='#20150e')

# evidence photos / code map board area
d.rounded_rectangle([134,840,872,1274], radius=18, fill='#171717', outline='#eadbbd', width=4)
d.text((166,872),'CASE BOARD: Understand-Anything',font=F['small'],fill='#f3e9d2')
# code map nodes
nodes=[(250,1010),(390,934),(520,1038),(690,942),(760,1130),(550,1195),(330,1160)]
for i,(x1,y1) in enumerate(nodes):
    for j,(x2,y2) in enumerate(nodes):
        if j>i and (j-i in (1,2,4) or random.random()<0.2):
            d.line([x1,y1,x2,y2], fill='#f0c34e99', width=4)
for i,(x,y) in enumerate(nodes):
    c='#e4362d' if i in (0,4) else '#f2d46b'
    d.ellipse([x-26,y-26,x+26,y+26], fill=c, outline='#fff4cb', width=3)
    d.text((x+34,y-16), ['入口','函数','依赖','模块','调用链','文件','问题'][i], font=F['tiny'], fill='#f3e9d2')
# pins/string
for x,y in nodes[:4]:
    d.line([x,y,835,894], fill='#e4362d66', width=2)
d.ellipse([821,880,849,908], fill='#e4362d', outline='#fff4cb', width=2)

# Evidence sticky notes
stickies=[(118,1332, '+5,604', '今日新增 stars', '#fff0a3'), (398,1376, '33,820', '总 Star', '#f7d4c4'), (674,1328, 'TS', 'TypeScript', '#cceeff')]
for x,y,big,small,col in stickies:
    d.rounded_rectangle([x,y,x+244,y+164], radius=10, fill=col, outline='#4b3324', width=2)
    d.text((x+26,y+26),big,font=F['h'],fill='#20150e')
    d.text((x+28,y+92),small,font=F['small'],fill='#5c4230')

# Torn black caption bar
d.rounded_rectangle([64,1590,1016,1748], radius=30, fill='#16120fee', outline='#d8c095', width=2)
d.text((104,1626),'不用一行行读代码，',font=F['h'],fill='#fff4df')
d.text((104,1684),'直接问它。',font=F['h'],fill='#ffe36b')

# bottom info
d.text((72,1812),'适合：接手旧项目 / AI 代码审查 / 技术讲解',font=F['small'],fill='#f3e9d2')
d.text((72,1852),'Lum1104 / Understand-Anything',font=F['tiny'],fill='#d6b98a')

OUT.parent.mkdir(parents=True,exist_ok=True)
img.convert('RGB').save(OUT,quality=95)
print(OUT)
