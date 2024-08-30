# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define gui.text_font = "font/NotoSansSC-VariableFont_wght.ttf"

# The game starts here.
define s = Character('Sylvie', kind=nvl, color="#c8ffc8")
define m = Character('Me', kind=nvl, color="#c8c8ff")

image bg black = im.Scale("images/black.jpg", 3840, 2160)
image bg hospice = im.Scale("images/hospice.jpg", 3840, 2160)
image bg string = im.Scale("images/string.jpg", 3840, 2160)
define narrator = nvl_narrator

label start:

    scene bg string

    narrator """
    细线。
    """
    scene bg black

    narrator"""

    城楼。

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

    """

    scene bg hospice

    narrator"""
    许都第一医院

    像一座深不见底的迷宫，罗列着以上的一切。

    草草被封在水银一样的病房里。

    清醒的时候，他知道他永远都走不出去了。

    {clear}

    外面已经是，外面又是大汉的天下。

    如果现在走出病房门，说不定门牌上就写着“逆贼”二字。

    这么想着，他觉得干脆走出去看看好了。

    尽管他知道他永远走不出去。

    {clear}

    （又下雨了⋯…）

    梅子酒的香气，好像是从大脑皮层散发出来的。

    试着挪动脚步。

    把自己想象成机器。

    就这样一点一点的⋯•…尽量不要留下痕迹。

    {clear}

    —“草草”正在死去。

    （门来了。）“大人⋯？”

    {clear}

    “怎么起来了？”

    啊，天啊。这脑中的香气开始痛不欲生的蔓延。

    这家伙…一直都站在门口吗？
    """
