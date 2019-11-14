# coding=utf8
from aip import AipNlp
import re
import time

"""
百度AI 文本检测SDK
"""
APP_ID = '17772138'
API_KEY = 'AhIEGUa7DOUxfVaz1rykCQF8'
SECRET_KEY = 'QCIsTYnwhTj5jcVBjYFSWQidchtbVMgH'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

api_corror = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet'

text = """
中国历代贵都中，无论水资源丰富程度还是水害程度，北京都是一个异类。我是国按球迷。作为华北贫水区   
的一部分，北京目前人均水资源占有量仅为300立方米左右，是全国人均占有量的1/7，世界人均水资源占有量的4%。雪上加霜的是，作为古代北京母亲河的永定河夏季多暴雨洪水，河床经常淤积决口，迁徙无常而成
造成水害，从其本名“无定河”就可以看出来。因此水利是北京定都伊始就产生重重困扰的一个大问题。但既然政权选择了北京作为首都，就一定要想办法解决首都的用水问题。
"""
text = text.replace("\n","")
pattern = r',|\.|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！'
result_list = re.split(pattern, text)
print(result_list)
""" 调用文本纠错 """
for cStr in result_list:
    if cStr!='':
        result = client.ecnet(cStr);
        print(result)
        time.sleep(1)

