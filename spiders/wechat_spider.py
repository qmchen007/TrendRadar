from wechatsogou import WechatSogouAPI

def crawl_wechat(account_name, max_count=5):
    ws = WechatSogouAPI()
    articles = ws.search_gzh(account_name=account_name, count=max_count)
    results = []
    for a in articles:
        title = a.get('name')
        url = a.get('url')
        time_pub = a.get('datetime')
        results.append({
            'platform': 'wechat_gzh',
            'account': account_name,
            'title': title,
            'url': url,
            'time': time_pub
        })
    return results

if __name__ == '__main__':
    data = crawl_wechat('你的公众号名称', max_count=10)
    for d in data:
        print(d)
