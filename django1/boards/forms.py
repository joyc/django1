#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/1/31/0031 0:32
# @Author  : Hython.com
# @File    : forms.py
from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Topic
        fields = ['subject', 'message']
