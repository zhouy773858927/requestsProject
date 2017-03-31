import requests

url = "http://www.baidu.com"
def head():
    response = requests.get(url)
    return response.headers

if __name__ == '__main__':
    res = head()
    for i in res:
        print(i+':'+res[i])#是个字典，字典{键：值}所以输出得输出两个，一个键，一个值
