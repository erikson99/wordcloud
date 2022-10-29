from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from io import BytesIO

stopwords = set(STOPWORDS)

def create_wc(text, mask):
	"""
		Creates and saves a wordcloud image(WordCloud.png) from a non-empty 
		input string.
		"""
	cloud = WordCloud(background_color="white", max_words=500,
	                  stopwords=set(STOPWORDS), mask=mask).generate(text)
	cloud.to_file("./static/WordCloud.png")
	return 1