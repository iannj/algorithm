#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import requests
from threading import Timer


def _get_quotes(method, symbol):
    """

    :param method:
    :param symbol:
    :return:
    """

    # main function
    if method == 'sina':
        url = 'http://hq.sinajs.cn/list='
        query_string = url + symbol
        response = requests.get(query_string)
        if response.status_code == 200:
            with open('quotes_data.txt', 'a') as f:
                f.writelines(response.text)
                # f.writelines('\n')
    else:
        pass

    # loop
    interval = 60
    timer = Timer(interval, _get_quotes, (method, symbol))
    timer.start()


def testcase():
    """

    :return:
    """
    method = 'sina'
    symbol = 'hf_CHA50CFD'
    _get_quotes(method, symbol)


if __name__ == '__main__':
    testcase()
