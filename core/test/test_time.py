# -*- coding: utf-8 -*-
#author: kai.zhang


import arrow
import datetime
start = '2018-03-01'
end = '2018-03-02'
start = datetime.datetime.strptime(start, '%Y-%m-%d')
end = datetime.datetime.strptime(end, '%Y-%m-%d')

def get_range(start, dalt=1):
    list = []
    for i in range(dalt):
        td = (start + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:')
        start = datetime.datetime.strptime(td, '%Y-%m-%d %H:%M:')
    return start


def process(start):
    end = get_range(start)
    print(start, end)


i = 0
start = datetime.datetime.strptime((start + datetime.timedelta(minutes=-1)).strftime('%Y-%m-%d %H:%M:'), '%Y-%m-%d %H:%M:')
while start < end:
    td = (start + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:')
    start = datetime.datetime.strptime(td, '%Y-%m-%d %H:%M:')
    process(start)







