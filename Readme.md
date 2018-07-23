词云是最近比较流行的一个玩法，javascript, python, R 等语言都有库可以实现。

简单介绍一下python的wordcloud。

github:
https://github.com/amueller/word_cloud

示例代码地址： 

### 1. 安装
```
pip install wordcloud
```

### 2. 入门例子
- constitution.py
```
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文本内容
text = open('../text/constitution.txt').read()

# 生成词云图片数据
wordcloud = WordCloud().generate(text)
image = wordcloud.to_image()
image.show()
wordcloud.to_file("../word_image/constitution.png")

# 使用 matplotlib 展示数据
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
```
![这里写图片描述](https://img-blog.csdn.net/20180722221715882?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heG1hbzEwMjQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
```
# 使用 matplotlib 遇到的问题
RuntimeError: Python is not installed as a framework
> 解决方法：
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
> 详细可参考：
https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python/21789908#21789908
```

### 3. 常用参数配置
- love.py
```
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

# 读取文本内容
text = open('../text/love.txt').read()
wc = WordCloud(font_path='../font/simhei.ttf',  # 设置字体
               background_color="black",  # 背景颜色
               max_words=100,  # 词云显示的最大词数
               mask=imread("../background_image/love.jpg"),  # 设置背景图片
               stopwords=set(STOPWORDS),  # 使用内置单词集合过滤
               max_font_size=100,  # 字体最大值
               random_state=42,  # random.Random的种子，用来生成随机颜色
               # width=1000,
               # height=860,
               )
wordcloud = wc.generate(text)
image = wordcloud.to_image()
image.show()
wordcloud.to_file("../word_image/love.png")
```
![这里写图片描述](https://img-blog.csdn.net/20180722221656645?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heG1hbzEwMjQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

[全部参数说明](https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud)

### 3. 中文分词
- talk.py
```
from wordcloud import WordCloud
from scipy.misc import imread
import jieba


# 使用自定义的中文屏蔽词组
def stop_words():
    f = open('../text/stopwords.txt', 'r', encoding='utf-8')
    word_list = [' ']
    while True:
        line = f.readline().rstrip()
        word_list.append(line)
        if not line:
            break
    f.close()
    return word_list


text = open('../text/talk.txt').read()
word_generator = jieba.cut(text)  # 使用结巴分词，获得生成器
text = ' '.join([word for word in word_generator])

wc = WordCloud(font_path='../font/simhei.ttf',  # 设置字体
               background_color="black",  # 背景颜色
               max_words=100,  # 词云显示的最大词数
               mask=imread("../background_image/love.jpg"),  # 设置背景图片
               stopwords=set(stop_words()),  # 使用内置单词集合过滤
               max_font_size=100,  # 字体最大值
               random_state=42,  # random.Random的种子，用来生成随机颜色
               # width=1000,
               # height=860,
               )


wc_text = wc.generate(text)
image = wc_text.to_image()
image.show()
wc_text.to_file("../word_image/talk.png")
```

![这里写图片描述](https://img-blog.csdn.net/20180722221632239?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21heG1hbzEwMjQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
