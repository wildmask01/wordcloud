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
