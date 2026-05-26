from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, math

ROOT = Path.cwd()
OUT = ROOT / 'vault' / 'Inno' / 'GithubTrending' / '2026-05-26' / 'douyin' / 'study-note-sample-01.png'
W,H = 1080,1440
FONT_BOLD='C:/Windows/Fonts/msyhbd.ttc'
FONT_REG='C:/Windows/Fonts/msyh.ttc'

def ft(path,size): return ImageFont.truetype(path,size=size)
F={
 'title':ft(FONT_BOLD,58), 'subtitle':ft(FONT_REG,26), 'h':ft(FONT_BOLD,31),
 'body':ft(FONT_REG,27), 'small':ft(FONT_REG,22), 'tiny':ft(FONT_REG,18),
 'repo':ft(FONT_BOLD,30)
}

BG='#F5F0E6'; PAPER='#EFE1C9'; INK='#51463D'; SOFT='#756A5F'
SAGE='#BAC7A7'; TERRA='#C98265'; MUSTARD='#DDBE64'; TAUPE='#C9B8A5'; BRICK='#B86657'; CORAL='#E88D67'; SKY='#BDD7D6'

img=Image.new('RGB',(W,H),BG).convert('RGBA')
d=ImageDraw.Draw(img,'RGBA')
random.seed(4)
# paper grain
for _ in range(5500):
    x=random.randrange(W); y=random.randrange(H); a=random.randrange(8,22)
    col=(120,92,60,a) if random.random()<0.45 else (255,250,235,a)
    d.point((x,y),fill=col)

# left kraft layer + tape
d.rounded_rectangle([-38,70,126,H-70], radius=34, fill=PAPER, outline='#D9C9AD')
d.polygon([(42,40),(205,54),(190,112),(34,98)], fill='#D9C79A88', outline='#B8A47C55')
d.polygon([(848,42),(1006,28),(1020,92),(858,106)], fill='#D9C79A88', outline='#B8A47C55')

# helper functions
def wobble_line(points, fill=INK, width=3, jitter=2):
    pts=[]
    for x,y in points:
        pts.append((x+random.randint(-jitter,jitter), y+random.randint(-jitter,jitter)))
    d.line(pts, fill=fill, width=width, joint='curve')

def round_poly(points, fill, outline=INK, width=3):
    d.polygon(points, fill=fill)
    pts=points+[points[0]]
    for a,b in zip(pts,pts[1:]): wobble_line([a,b], outline, width, 2)

def cloud(x,y,w,h,fill,outline=INK):
    d.rounded_rectangle([x,y,x+w,y+h], radius=38, fill=fill)
    # bumpy outline
    steps=16; pts=[]
    for i in range(steps+1): pts.append((x+i*w/steps, y+random.randint(-4,4)))
    for i in range(steps+1): pts.append((x+w+random.randint(-4,4), y+i*h/steps))
    for i in range(steps+1): pts.append((x+w-i*w/steps, y+h+random.randint(-4,4)))
    for i in range(steps+1): pts.append((x+random.randint(-4,4), y+h-i*h/steps))
    d.line(pts+[pts[0]], fill=outline, width=3)

def capsule(x,y,w,h,fill,outline=INK):
    d.rounded_rectangle([x,y,x+w,y+h], radius=h//2, fill=fill)
    for off in [0,2]: d.rounded_rectangle([x+off,y+off,x+w-off,y+h-off], radius=h//2, outline=outline, width=2)

def stamp(x,y,w,h,fill,outline=INK):
    d.rounded_rectangle([x,y,x+w,y+h], radius=20, fill=fill)
    # perforated edge
    for i in range(12):
        xx=x+12+i*(w-24)/11
        d.ellipse([xx-3,y-3,xx+3,y+3], fill=BG)
        d.ellipse([xx-3,y+h-3,xx+3,y+h+3], fill=BG)
    d.rounded_rectangle([x,y,x+w,y+h], radius=20, outline=outline, width=3)

def write_wrap(x,y,text,font,chars,line_h,fill=INK,max_lines=4):
    lines=[]; cur=''
    for ch in text:
        cur+=ch
        if len(cur)>=chars and ch not in '，。、 /':
            lines.append(cur); cur=''
    if cur: lines.append(cur)
    lines=lines[:max_lines]
    for line in lines:
        d.text((x,y),line,font=font,fill=fill); y+=line_h
    return y

# Title tag
label=[(106,92),(724,66),(782,144),(718,226),(128,238),(84,158)]
round_poly(label, '#E9C978', BRICK, 4)
d.ellipse([704,112,724,132], fill=BG, outline=BRICK, width=2)
d.text((138,116),'开源项目小抄',font=F['title'],fill='#5B352E')
d.text((142,184),'Understand-Anything — codebase knowledge map',font=F['subtitle'],fill='#6D5C50')
# tiny code graph doodle near title
for cx,cy in [(874,120),(930,96),(966,160),(900,184)]:
    d.ellipse([cx-12,cy-12,cx+12,cy+12], outline=SAGE, width=3, fill='#F8F2E9')
for a,b in [((874,120),(930,96)),((930,96),(966,160)),((874,120),(900,184)),((900,184),(966,160))]:
    d.line([a,b], fill=SAGE, width=2)

# Wide top card
cloud(118,306,844,252,'#F8E7D8')
d.text((156,340),'它是什么？',font=F['h'],fill=BRICK)
d.text((156,388),'把代码仓库解析成一张可交互的知识图谱，',font=F['body'],fill=INK)
d.text((156,430),'让你能搜索函数、追问依赖、理解模块关系。',font=F['body'],fill=INK)
# coral circles max twice
for box in [(150,384,642,423),(150,425,604,464)]:
    d.rounded_rectangle(box, radius=18, outline=CORAL, width=4)
# mini graph doodle inside card
base_x,base_y=710,386
nodes=[(base_x,base_y),(base_x+90,base_y-30),(base_x+140,base_y+60),(base_x+38,base_y+98)]
for a,b in [(0,1),(1,2),(0,3),(3,2),(0,2)]: d.line([nodes[a],nodes[b]], fill=TAUPE, width=3)
for x,y in nodes: d.ellipse([x-14,y-14,x+14,y+14], fill=SAGE, outline=INK, width=2)

# Cards layout
cards=[
 (112,620,390,250,'cloud',SAGE,'主要用途','接手旧项目、看陌生仓库、做 AI 代码审查时，先看全局关系。'),
 (580,620,378,250,'capsule',MUSTARD,'核心能力','自然语言提问：例如「登录逻辑在哪？」系统按图谱找线索。'),
 (112,910,390,250,'stamp',SKY,'为什么值得看','AI 生成代码越来越多，理解上下文比复制答案更重要。'),
 (580,910,378,250,'cloud',TAUPE,'怎么用','先分析仓库，再打开交互图谱；适合配合 Claude Code / Codex。'),
 (190,1210,700,124,'capsule','#E8D7C2','适量原则','别只收藏：挑 1 个项目跑起来，写下它解决的真实问题。'),
]
for x,y,w,h,kind,color,head,body in cards:
    if kind=='cloud': cloud(x,y,w,h,color)
    elif kind=='capsule': capsule(x,y,w,h,color)
    else: stamp(x,y,w,h,color)
    d.text((x+30,y+28),head,font=F['h'],fill='#5B352E')
    write_wrap(x+30,y+82,body,F['body'],15 if w<500 else 28,38,INK,3)

# Doodles: arrows, hearts, fake underlines
for x,y in [(90,590),(492,620),(940,588),(508,1180),(910,1188)]:
    d.ellipse([x-5,y-5,x+5,y+5], fill=BRICK)
    d.ellipse([x+10,y-5,x+20,y+5], fill=CORAL+'aa')
wobble_line([(338,594),(454,574),(500,608)], BRICK, 3, 3)
d.polygon([(500,608),(484,600),(490,620)], fill=BRICK)
wobble_line([(312,1338),(780,1328)], CORAL, 4, 3)
# loose chemical-ish doodle but code-ish
cx,cy=910,1328
for i in range(6):
    ang=math.pi*2*i/6
    x=cx+36*math.cos(ang); y=cy+26*math.sin(ang)
    x2=cx+36*math.cos(ang+math.pi/3); y2=cy+26*math.sin(ang+math.pi/3)
    d.line([(x,y),(x2,y2)], fill=TAUPE, width=2)
d.text((862,1362),'repo graph',font=F['tiny'],fill=SOFT)

# mascot: tiny smiling folder/tomato-ish repo mascot
mx,my=860,1170
d.rounded_rectangle([mx,my,mx+92,my+76], radius=20, fill='#F0C46A', outline=INK, width=3)
d.rectangle([mx+12,my-14,mx+52,my+12], fill='#F0C46A', outline=INK, width=2)
d.arc([mx+26,my+25,mx+66,my+58], 0, 180, fill=INK, width=2)
d.ellipse([mx+28,my+28,mx+34,my+34], fill=INK); d.ellipse([mx+60,my+28,mx+66,my+34], fill=INK)

# footer
d.text((138,1374),'信息来自 daily.md 与对应文章；仅供开源项目发现参考，不构成技术选型承诺。',font=F['small'],fill=SOFT)

OUT.parent.mkdir(parents=True,exist_ok=True)
img.convert('RGB').save(OUT,quality=95)
print(OUT)
