# coding: utf-8

import requests
from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession
from werkzeug.exceptions import InternalServerError
from HTMLParser import HTMLParser
from . import grade_index_url
from . import link_index_url
from . import grade_detail_url
from . import headers
from . import proxy


def get_grade_detail(_s, s, sid, xnm, xqm, course, jxb_id):
    grade_detail = {}
    detail_url = grade_detail_url % sid
    link_url = link_index_url
    try:
	_s.get(link_url)  # 新版与旧版信息门户过渡, 获取cookie
    except requests.exceptions.ConnectionError:
	raise 444
    data = {'xh_id': sid, 'xnm': xnm, 'xqm': xqm,
            'jxb_id': jxb_id, 'kcmc': course}
    try:
        r = s.post(detail_url, data, headers=headers, proxies=proxy)
        soup = BeautifulSoup(r.result().content, 'html.parser', from_encoding='utf-8')
        strings = soup.find('table',
            class_="table table-bordered table-striped table-hover tab-bor-col-1 tab-td-padding-5"
        ).tbody.stripped_strings
    except AttributeError:
        pass
    else:
        _strings = list(strings)
        if len(_strings) == 2:
            usual = ""; ending = ""
        else:
            usual = _strings[2] if len(_strings[2]) < 3 else ""
            ending = _strings[5] if len(_strings[5]) < 3 else ""
        grade_detail.update({
            'usual': usual,
            'ending': ending })
        return grade_detail


def get_grade(_s, s, sid, xnm, xqm):
    grade_url = grade_index_url % sid
    link_url = link_index_url
    _s.get(link_url)  # 中转过度, 获取cookie
    post_data = {
        'xnm': xnm, 'xqm': xqm,
        '_search': 'false', 'nd': '1466767885488',
        'queryModel.showCount': 15, 'queryModel.currentPage': 1,
        'queryModel.sortName': "", 'queryModel.sortOrder': 'asc',
        'time': 1 }
    try:
        r = s.post(grade_url, post_data, headers=headers, proxies=proxy, timeout=(5, 10))
        json_data = r.result().json()
    except ValueError:
        pass
    else:
        gradeList = []
        # return gradeList
        _gradeList = json_data.get('items')
        for item in _gradeList:
            gradeList.append({
                'course': item.get('kcmc'),
                'credit': item.get('xf'),
                'grade': item.get('cj'),
                'category': item.get('kclbmc'),
                'type': item.get('kcgsmc'),
                'jxb_id': item.get('jxb_id')})
        return gradeList
