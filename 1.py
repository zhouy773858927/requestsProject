import requests

url = "http://www.baidu.com/"

def use_simple_requests():
    response = requests.get(url)
    print(">>>>Response Headers:")
    print(response.headers)
    print(">>>>Response Body:")
    print(response.text.encode(response.encoding).decode("utf8"))
def use_parmas_requests():#构建请求参数
    parmas = {'class':'hello'}
    response = requests.get(url,params=parmas)#发送请求
    #处理响应
    print(">>>>Response Headers:")
    print(response.headers)
    print(">>>>Status Code:")
    print(response.status_code)
    print(response.reason)
    print(">>>>Response Body:")
    print(response.text.encode(response.encoding).decode("utf8"))
    #response.json()

if __name__ == '__main__':
    print(">>>>use simple requests:")
    use_simple_requests()
    print("———————————————————分割线—————————————————————")
    print(">>>>use params requests:")
    use_parmas_requests()
# {'Content-Type': 'text/html', 'Connection': 'Keep-Alive', 'Date': 'Thu, 30 Mar 2017 07:15:03 GMT',
#  'Last-Modified': 'Mon, 23 Jan 2017 13:28:17 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18',
#  'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Content-Encoding': 'gzip',
#  'Transfer-Encoding': 'chunked', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/'}
#{'Content-Type': 'text/html', 'Connection': 'Keep-Alive', 'Date': 'Thu, 30 Mar 2017 07:15:03 GMT',
# 'Last-Modified': 'Mon, 23 Jan 2017 13:28:25 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18',
#  'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Content-Encoding': 'gzip',
#  'Transfer-Encoding': 'chunked', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/'}
