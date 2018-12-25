import aiohttp
import asyncio
import logging
import requests


def post():
    data = 'UserName={}&UserPwd={}&remember=1'.format(
        '1392798578@qq.com', '111aaa')
    headers = {'content-type': 'text/html; charset=utf-8',
               'Cookie': 'email=1392798578@qq.com',
               'DNT': '1',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Origin': 'http://www.mgqr.com',
               'Referer': 'http://www.mgqr.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/'
               '537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36 '
               'Avast/65.0.411.162'}

    resp = requests.post(
        'http://www.mgqr.com/control/checklogin.ashx', data, headers=headers)
    print(resp.content)


async def fetch():
    session: aiohttp.client.ClientSession = None
    data = 'UserName={}&UserPwd={}&remember=1'.format(
        '1392798578@qq.com', '111aaa')
    headers = {'content-type': 'text/html; charset=utf-8',
               'Cookie': 'email=1392798578@qq.com',
               'DNT': '1',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Origin': 'http://www.mgqr.com',
               'Referer': 'http://www.mgqr.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36 Avast/65.0.411.162'}

    async with aiohttp.ClientSession() as session:
        async with session.post('http://www.mgqr.com/control/checklogin.ashx',
                                data=data.encode('gbk'), headers=headers) as \
                resposne:
            text = await resposne.text()
            logging.debug(text)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch())
post()
