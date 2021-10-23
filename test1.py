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

regex = re.search('mở (.+)', "abc bng mở agw")
print(regex.group(1))