import speech_recognition #Thư viện nhận dạng giọng nói
from gtts import gTTS # Giúp trợ lý ảo nói (Thông qua file mp3)
import os # Thư viện hỗ trợ thao tác với file
from datetime import date, datetime # Hỗ trợ lấy ra ngày giờ
import playsound # Thư viện hỗ trợ chạy file mp3 đã lưu
import pyjokes # Thư viện giúp trợ lý ảo nói đùa
from googletrans import Translator # Thư viện hỗ trợ dịch văn bản
import re # Thư viện Regular Expression
import webbrowser # Thư viện hỗ trợ mở trình duyệt
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from chatterbot import ChatBot # Thư viện giúp AI bớt ngu :'>
from chatterbot.trainers import ChatterBotCorpusTrainer # Thư viện giúp AI bớt ngu :'>
from youtube_search import YoutubeSearch # Thư viện hỗ trợ tìm kiếm trên youtube
import time # Xử lý các tác vụ liên quan đến thời gian
import requests # Hỗ trợ gửi yêu cầu HTTP
from bs4 import BeautifulSoup # Hỗ trợ xử lý dữ liệu dạng html (Phân tích tài liệu html)
import subprocess
import sys
from pathlib import Path
import array as arr 



file_name = "abcd"
disk = 'e'
count = 0;

out = os.popen('dir /a-d /b "' + disk + ':\\' + file_name + '*" /s').read().strip()
temp = out.splitlines()
for x in range(len(temp)):
    file_name = temp[x].split('\\')
    file_name = file_name[len(file_name) - 1]
    count += 1
    print(str(count) + ". " + file_name)
print(len(temp))
os.startfile(temp[0])

# text = 'file thứ nhất'
# n = ['một', 'nhất']
# number = [n, 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười']
# for x in range(len(number)):
#     if number[x] in text:
#         a = number.index(number[x])
# print(a)  
