
#import nltk.tokenize.punkt

# Make a new Tokenizer
#tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')

nltk.data.path.append('/home/sslunder0/nltk_data')
tokens = nltk.tokenize.word_tokenize("test")
print(tokens)

# import nltk
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download("punct")







# import nltk
# #nltk.download("popular")
# # nltk_data 경로를 추가합니다.
# # nltk.data.path.append('/home/sslunder0/nltk_data/')
# # from nltk import stopwords
# # 'punkt' 데이터 로드 테스트
# try:
#     nltk.tokenize.word_tokenize("Test sentence.")
#     print("Punkt tokenizer is working.")
# except LookupError:
#     print("Punkt tokenizer is not found. Check the nltk_data path.")