from wordcloud import WordCloud
from scipy.misc import imread
import jieba


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
word_generator = jieba.cut(text)  # 使用结巴分词
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



