# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:17:06 2020

@author: simon
"""


#%%
a = [{'flightNo': 'NJE794R',
  'airport': 'Ljubljana',
  'via': '',
  'scheduledTime': '12:30',
  'estimatedTime': '',
  'gate': '',
  'status': '',
  'privateflight': 'Private Flight',
  'direction': 'departure'},
 {'flightNo': 'DFC6HX',
  'airport': 'Shannon',
  'via': '',
  'scheduledTime': '14:00',
  'estimatedTime': '14:35',
  'gate': '',
  'status': 'Delayed',
  'privateflight': '',
  'direction': 'departure'}
 ]

a = [a, a]

newlist = sorted(a, key=lambda k: k['scheduledTime']) 


print(newlist)

