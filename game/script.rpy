# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define gui.text_font = "font/NotoSansSC-VariableFont_wght.ttf"
style sus is text:
    size 80
    font "font/LongCang-Regular.ttf"
    color "#f00"
    textalign 0

style zhuyin_red is text:
    size 20
    color "#f00"

init python:
    def zhuyin_red_text(base_text, zhuyin_red):
        return "{=zhuyin_red}%s{/=zhuyin_red}{fast}\n%s" % (zhuyin_red, base_text)

screen nvl_shake_text(text):
    add Text(text) at shake_text xpos 0.5 ypos 0.5

# The game starts here.
define s = Character('Sylvie', kind=nvl, color="#c8ffc8")
define m = Character('Me', kind=nvl, color="#c8c8ff")

image bg black = im.Scale("images/black.jpg", 3840, 2160)
image bg hospice = im.Scale("images/hospice.jpg", 3840, 2160)
image bg string = im.Scale("images/string.jpg", 3840, 2160)
image bg fitbit = im.Scale("images/smartwatch.jpg", 3840, 2160)
define narrator = nvl_narrator

label start:

    scene bg string

    narrator """
    细线
    """
    scene bg black
    
    narrator"""

    火楼。

    密密麻麻地拼凑成肉山地尸体。

    {clear}

    军旗。

    腐烂的水果。

    崩解的通讯点播。

    {clear}

    一个像伤口版的微笑。

    一个滑腻的手。

    一具似乎永不腐坏的尸体。

    {clear}

    {=sus}……{/sus}

    {=sus}尸体睁开眼睛。{/sus}
    """

    scene bg hospice

    narrator"""
    许都第一医院。

    像一座深不见底的迷宫，罗列着以上的一切。

    曹操被封在水银一样的病房里。

    清醒的时候，他知道他永远都走不出去了。

    {clear}

    外面已经是，外面又是大汉的天下。

    如果现在走出病房门，说不定门牌上就写着“逆贼”二字。

    这么想着，他觉得干脆走出去看看好了。

    尽管他知道他永远走不出去。

    {clear}

    {=sus}又下雨了……{/sus}

    梅子酒的香气，好像是从大脑皮层散发出来的。

    试着挪动脚步。

    把自己想象成机器。

    就这样一点一点的……尽量不要留下痕迹。

    {clear}

    —“曹操”正在死去。

    {=sus}门开了。{/sus}

    “大人⋯？”

    {clear}

    “怎么起来了？”

    啊，天啊。这脑中的香气开始痛不欲生的蔓延。

    这家伙…一直都站在门口吗？

    {clear}

    “该吃饭了，您回到病床上去吧。”

    {=sus}现在是几点钟……{/sus}

    时间好像变成了异样的概念。

    曹操默不作声。默不作声。

    踩着瓷砖里自己失真的影子倒退。

    如果这样能回到无需忏悔的治世……

    {clear}

    “早饭都是您爱吃的。”

    一个盛放着瘟疫和灾难的器皿端到了他的眼前。

    一只似乎持着凶器的手托着它。

    向上看去，又是那张被谎言腐蚀的脸。

    {clear}

    “昨晚睡得好吗？”

    “我看看……”

    曹操的手被刘备拖进了他的怀里，好像陷入蜘蛛巢。
    """

    scene bg fitbit

    narrator """

    这时他才注意到手腕上一个鸣叫着的镣铐。

    数字化的生命体征在屏幕上{=sus}抽动抽动抽动抽动抽动……{/sus}

    {clear}

    """

    scene bg string

    narrator"""
    “睡得这么不稳，您做梦了吗？”

    “还是因为做了梦，但却是个无人可杀的梦呢？”

    {=sus}……{/sus}

    “你的手不沾血就受不了吧？”

    {=sus}[zhuyin_red_text('既视感，既视感……', 'Deja vu')]{/sus}

    {clear}

    {=sus}“刘公啊，昨晚睡得还好吗？”{/sus}

    {=sus}"在梦里逮住了一条{/sus}

    {=sus}[zhuyin_red_text('偷肉吃的狗', '伪装成皇亲')],{/sus}

    {=sus}仔细一看居然和你有着同一种型号的眼球。”{/sus}

    {=sus}“好吃吗？让我闻闻你的嘴里有没有肉的味道？”{/sus}

    {clear}
    """

    scene bg hospice
    narrator"""
    “滚！滚开！”

    餐盘打碎了。肢体飞溅了。眼球跌落了。

    好像这样一切都结束了，解脱了。
    """
    scene bg black

    narrator"""

    那个温柔地狞笑着的影子被放大，拉长，解离，碾碎……

    {clear}

    曹操跪了下来，双手抱头，名副其实的痛不欲生。

    一心向死，是阶下囚能做到的唯一的反抗。

    {clear}

    {=sus}“曹操连我一分钟之内呼吸的次数都要过问……”{/sus}

    {=sus}“弟弟啊……我不能死。”{/sus}

    {=sus}“死在许都，曹操还是会把我埋在这里。”{/sus}
    
    {fast}

    {=sus}“那样我们最后的逃脱手段也要宣告失败了。”{/sus}

    {clear}

    报应！

    {clear}

    锋利的言词切割切割着他的感官，碎屑填满了意识。

    许都的两个人沿着时间的链条被分解，切成薄片。

    原来记忆是可燃物……记忆的碎屑以脑浆作为燃料在燃烧。

    火，快要化成血，从身上的每一个孔洞流出来了……

    {clear}
    """

    scene bg hospice

    narrator"""

    “没事了，没事了。”

    痛苦好像渐渐烧尽了。

    猛烈的头痛，成为了一种安详的窒息感。

    好像把大脑沉入了一池地狱一样的春水。

    {clear}

    ——曹操发现自己被刘备抱在怀里。

    {clear}

    已经不知道多少次被这种令人作呕的拥抱安抚着平静下来，甚至形成了条件反射。

    但不安的最初也是因为刘备的阴影。

    这样一来就好像刘备在控制着他的癔症一样。

    {fast}

    什么时候开始的，大概是从汉中那次落荒而逃吧。

    {clear}

    “您看您出的汗，这么讨厌这个话题吗？”

    “我可是每天都在想我们初遇的事情，一起讨董的事情，还有在许都的事情……”

    “也没这么激动不是吗？”
    """




