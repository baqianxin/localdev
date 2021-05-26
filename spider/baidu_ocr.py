from aip import AipOcr

APP_ID = '23090930'
API_KEY = 'huGU5p0QbqSkMI5SxNjOcH11'
SECRET_KEY = '3BFpkzDjo3fvNB7BfbALEmjAG1oIUb1i'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
data  = client.basicGeneral(image);
print(data)

# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"

# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)

# url = "https//www.x.com/sample.jpg"

# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);

# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"

# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)