import requests

proxypool_url = 'http://127.0.0.1:5555/random'
target_url = 'https://antispider5.scrape.center/'


def get_random_proxy():
    """
    get random proxy from proxypool
    :return:
    """
    return requests.get(proxypool_url).text.strip()


def crawl(url, proxy):
    """
    use proxy tp crawl page
    :param url:
    :param proxy:
    :return:
    """
    proxies = {'http': 'http://' + proxy}
    return requests.get(url, proxies=proxies).text


def main():
    """
    main method, entry point
    :return:
    """
    proxy = get_random_proxy()
    print('get random proxy', proxy)
    html = crawl(target_url, proxy)
    print(html)


if __name__ == '__main__':
    main()
