# -*- coding: utf-8 -*-
"""
Created on 2017-14-7

@author: rotrux
"""


class regex_strings(object):

    EMAIL1 = r'(\w+[.|\w]\w+(@\w+[.]\w+[.|\w+]\w+))'
    EMAIL2 = r'(\w+[.|\w])*@(\w+[.])*\w+'
    EMAIL3 = r'\s([\w-].+@\w.+\.\w+)\s+'
    EMAIL4 = r'^\W*(\w+-*\w*@\w+\.\w{2,6})\W*'
    EMAIL5 = r'\W*(\w+-*\w*@\w+\.\w{2,6})\W*$'

    # pay attention to where the capture groups are.
    # capture groups are denoted by ().
    # In most cases, you will want .group(1) or .group(2) AND NOT .group(0).
    HTML_A_BETWEEN = r'<a \S+="\S+"\s?.*\S?>([^\r\n]+)</a>'
    HTML_A_INNER1 = r'<a (\S+="\S+")\s?(.*)\S?>[^\r\n]+</a>'
    HTML_A_INNER2 = r'<a (\S+="\S+")\s?(.*?)\S?>[^<]+?<?'

    HTML_DIV_INNER = r'<div (\S+="\S+")\s?(.*?)>'
    HTML_IMG_INNER = r'<img (\S+="\S+")\s?(.*?)>'

    HTML_A_HREF = r'<a .* ?href="(\S+)"\s?.*\S?>[^\r\n]+</a>'
    HTML_IMG_SRC = r'<img .* ?src="(\S*)"\s?.*?/?>'
    #TODO: more <script> & <meta> support.
    HTML_SCRIPT_SRC = r'<script .* ?src="(\S+)"\s?.*?/?>'


    # format tags allow you to insert an arbitrary tag at {0}.
    # You must use the .format('foo') string method on these patterns.
    # where 'foo' is an html tag.
    HTML_FORMAT_BETWEEN = r'<{0}.*>(.*?)</{0}>'
    HTML_FORMAT_INNER = r'<{0} (\S+="\S+")\s?(.*?)\S?>[^<]+?<?'

    # Example regex-format-string usage:

    # >>> HTML_FORMAT_BETWEEN.format('a') is equivalent to:
    # >>> r'<{0}.*>(.*?)</{0}>'.format('a') which is equivalent to:
    # r'<a.*>(.*?)</a>'


    def __new__(cls, *args, **kwargs):
        pass
    def __init__(self):
        super(regex_strings, self).__init__()
