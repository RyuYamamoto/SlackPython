#!/usr/local/pyenv/shims/python
# coding:utf-8
from slackclient import SlackClient

token = "xoxp-209346279542-209346279590-211596497334-5f5ff0ff50fd6dfcc604b359f9521943"

sc = SlackClient(token)

if sc.rtm_connect():
    while True:
        return_data = sc.rtm_read()
        if len(return_data) > 0:
            for item in return_data:
                if item["type"] == "message":
                    print item["text"]
else:
    print "Connection Error."

