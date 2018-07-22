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
