from wsgiref.headers import Headers
import requests

def getBdMsg(keyword, page):
    Headers = {"User-Agent": "Mozilla/5.0 (x11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.81      Safari/537.36" ,}

    
    res = requests.get('https://www.google.co.jp/s?wd='+keyword+'&pn='+page+'&oq='+keyword+'&ie=utf-8&usm=4&fenlei=256&rsv_idx=1&rsv_pq=ae5d7fa900019d60&rsv_t=b5b2EjC0Aa%2BFTifA7QJfkk0STXZJROk%2B39dpuxD49IEDV1WSBsrFAGIeJHc&bs='+keyword+'&rsv_jmp=fail', headers=Headers)
    return res 

if __name__ == '__main__':
    print(getBdMsg('python',str(20)))