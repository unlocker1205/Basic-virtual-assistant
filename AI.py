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

# Khởi tạo
ai_brain = " " # Chuỗi rỗng do ban đầu máy chưa được học gì
count = 0 # Count hỗ trợ người dùng không nói nhiều lần sẽ tự tắt
you = " " # Người nói
name_sir = "" # Tên của người nói
chatbot = ChatBot('Tro Ly Ao Basic') # Khởi tạo bot
trainer = ChatterBotCorpusTrainer(chatbot) 
trainer.train("chatterbot.corpus.viet") # Train cho bot dữ liệu trong file chatterbot.corpus.english
translator = Translator() # Get phương thức translator

# Phương thức giúp trợ lí ảo nói
def ai_speak(text):
    print("Trợ lí: " + text + "\n") # In ra những gì trợ lý sẽ nói
    ai_mouth = gTTS(text, lang = "vi") # Gán cho biến ai_mouth để trợ lí có thể nói tiếng việt
    fileName = "AI.mp3" # Tên file mà trợ lí dùng để nói
    ai_mouth.save(fileName) # Lưu file (Cùng cấp với file python hiện tại)
    playsound.playsound(fileName, True) # Mở file AI.mp3 đã lưu ở trên
    os.remove(fileName) # Sau khi mở phải xóa file để tránh xung đột

# Phương thức giúp trợ lý có thể nghe
def ai_listen():
    ai_ear = speech_recognition.Recognizer() # Giúp trợ lý có thể nghe người dùng nói

    with speech_recognition.Microphone() as micro: # Gán speech_recognition.Microphone() cho biến micro
        ai_ear.adjust_for_ambient_noise(micro) # Giảm tiếng ồn
        print("Trợ lí: Tôi đang nghe ...")
        audio = ai_ear.record(micro, duration= 5) # Sau 5s sẽ tự ngắt micro
        print("Trợ lí: ...")
    try:
        you = ai_ear.recognize_google(audio, language = "vi-VN").lower() # Nghe và nói theo tiếng việt, đưa về chữ thường để dễ xử lý
        print("Người sử dụng: " + you)
        return you
    except: # Bắt lỗi khi người dùng không nói gì hoặc người dùng tạo những âm thành không phải từ ngữ
        you = ""
        return you

# Phương thức get thứ trong tuần
def weekToday(x):
        switcher={
                0: 'Thứ hai',
                1:'Thứ ba',
                2:'Thứ tư',
                3:'Thứ năm',
                4:'Thứ sáu',
                5:'Thứ bảy',
                6:'Chủ nhật'
             }
        return switcher.get(x)

# Phương thức lấy ra những gì trợ lý ảo nghe được
def get_ai_listen():
    text = ai_listen()
    if text:
        return text.lower()
    elif text == "":
        return ""

# Phương thức get tên người dùng
def get_name_sir(name):
    ai_speak("Bạn tên là gì?")
    name = get_ai_listen()
    name = name.title()
    ai_speak("Xin chào {}".format(name))
    return name

# Gán tên người dùng đã khai báo từ trước cho biến vừa get được
name_sir = get_name_sir(name_sir)

# Phương thức hỗ trợ mở browser
def open_brower(text):
    regex = re.search('mở (.+)', text) 
    if regex:
        domain = regex.group(1) # Lấy ra phần tử phía sau từ "mở" cho đến cuối của "text"
        url = 'https://www.' + domain
        webbrowser.open(url)
        ai_speak("Brower của bạn đã được mở")
        return True
    else:
        return False
        
# Phương thức hỗ trợ tìm kiếm trên google
def google_search(text):
    # search_key = text.split("kiếm", (1))[1]
    search_key = re.search('kiếm (.+)', text).group(1)
    url = f"https://www.google.com/search?q={search_key}"
    webbrowser.open(url) # Mở browser

# Phương thức hỗ trợ tìm kiếm trên youtube
def youtube_search():
    ai_speak("Nói từ khóa bạn muốn tìm kiếm trên Youtube!")
    text = get_ai_listen()
    results = YoutubeSearch(text, max_results=10).to_dict() # Đưa ra 10 link kết quả của tìm kiếm từ khóa 'text'
    url = 'https://www.youtube.com/' + results[0]['url_suffix'] # Lấy url là phần link đầu tiên
    # Lấy ra title của video chuẩn bị mở
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    ai_speak("Đang mở: " + s.find('title').text)
    time.sleep(0.5)
    webbrowser.open(url)

# Phương thức giúp AI bớt ngu được phần nào :'> (Nhưng vẫn ngu :)))
def smart_AI(text):
    # translation = translator.translate(text, dest='en', src='vi') # Dịch những gì người dùng nói sang tiếng anh
    ai_brain = chatbot.get_response(text) # Get câu trả lời thích hợp cho câu nói của người dùng
    # ai_brain = str(ai_brain_chatbot)
    
    translation_AI = translator.translate(ai_brain, dest='vi', src='auto') # Dịch những gì get được thành tiếng việt
    ai_speak(translation_AI.text)

# Phương thức dùng cmd tìm một file cụ thể trong ổ đĩa C 
def search_C(file_name):
    try:
        out = os.popen('dir /a-d /b "c:\\' + file_name +'" /s').read() # Chạy cmd trả về kết quả dưới dạng string
        temp = out.splitlines()
        ai_speak("Ứng dụng của bạn đang được mở!")
        os.startfile(temp[0]) # Mở file, vì chỉ có 1 file duy nhất nên là [0]
    except:
        ai_speak("Xin lỗi, tôi không tìm thấy File!")



def get_file_name(disk, file_name):
    number = ['một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười'] #Dùng cho trường hợp tìm kiếm được nhiều hơn 1 file
    count = 0; # Đếm số file
    a = ""
    out = os.popen('dir /a-d /b "' + disk + ':\\' + file_name + '*" /s').read().strip() # Chạy lệnh cmd
    temp = out.splitlines()
    for x in range(len(temp)): # Chạy vòng lặp for từ 0 -> chiều dài mảng temp
        file_name = temp[x].split('\\') 
        file_name = file_name[len(file_name) - 1] # Lấy ra phần tử cuối cũng của mảng file_name
        count += 1
        print(str(count) + ". " + file_name) # In ra danh sách các file tìm được
    if count > 1:
        ai_speak("Bạn muốn mở file thứ mấy?")
        time.sleep(1)
        text = get_ai_listen()
        for x in range(len(number)): # Chạy vòng for kiểm tra người dùng có nói đúng thứ tự hiện có hay không
            if number[x] in text:
                a = number.index(number[x])
        if a == "":
            ai_speak('Không thể mở file bạn yêu cầu!')
        elif a != "":
            ai_speak("File của bạn đang được mở")
            os.startfile(temp[a])
    elif count == 1:
        ai_speak("File của bạn đang được mở")
        os.startfile(temp[0])
    if len(temp)  == 0:
        ai_speak('File bạn muốn tìm kiếm không có trong ổ đĩa này, hãy thử lại ở ổ đĩa khác!')
        number_disk()

def number_disk():
    out = os.popen('wmic logicaldisk get name').read().strip() # Chạy cmd lấy ra danh sách ổ đĩa
    a = "".join(out.split()) # Xóa tất cả các khoảng trắng trong chuỗi
    output = a.split("Name")[1] 
    result = output.split(":")
    count = 1 # Đếm số ổ đĩa
    count2 = 0; # Dùng để kiểm tra người dùng có yêu cầu mở đúng ổ đĩa có trong danh sách hay không
    for x in range(len(result) - 2):
        count += 1
    ai_speak("Máy hiện tại có " + str(count) + " ổ đĩa ")
    for x in range(len(result) - 1):
        ai_speak(str(result[x]))
    ai_speak("Bạn muốn tìm kiếm ở ổ đĩa nào?")
    text = get_ai_listen()
    for x in range(len(result) - 1):
        if str(result[x]) not in text.upper():
            count2 += 1
    if count2 == len(result) - 1 and text != "":
        ai_speak('Xin lỗi, ổ đĩa bạn yêu cầu không tồn tại')
        number_disk()
    elif count2 != len(result) - 1:
        ai_speak("Bạn muốn tìm kiếm file tên gì?")
        text2 = get_ai_listen()
        if text2 != "":
            if "c" in text:
                get_file_name('c', text2)
            elif 'd' in text:
                get_file_name('d', text2)
            elif 'e' in text:
                get_file_name('e', text2)


# Phương thức mở dứng dụng
def open_application():
    ai_speak("Bạn muốn mở ứng dụng gì?")
    text = get_ai_listen()
    if "soạn thảo văn bản" in text:
        search_C("WINWORD.exe")
    elif "excel" in text:
        search_C("excel.exe")
    elif "powerpoint" in text:
        search_C("POWERPNT.EXE")
    elif "trình duyệt" in text:
        search_C("msedge.exe")


# Phương thức hoạt động chính
while True :
    you = get_ai_listen()

    if you == "":
        count += 1
        if count <= 2:
            ai_brain = "Tôi không nghe rõ, bạn hãy thử lại!"
            ai_speak(ai_brain)
    elif "ngày" in you:
        today = date.today()
        ai_brain = today.strftime("%d/%m/%Y")
        ai_speak("Ngày hôm nay là: " + ai_brain + " nha {}".format(name_sir))
        count = 0
    elif "thứ mấy" in you and "hôm nay" in you:
        week = date.today().weekday()
        ai_speak(weekToday(week))
        count = 0
    elif "mấy giờ" in you:
        now = datetime.now()
        ai_brain = now.strftime("%H:%M")
        ai_speak(ai_brain)
        count = 0
    elif "đùa" in you:
        ai_brain = pyjokes.get_joke(language="en")
        translation = translator.translate(ai_brain, dest='vi', src='auto')
        ai_speak(translation.text)
        count = 0
    # elif "mở trình duyệt" in you or "mở trình duyệt và tìm kiếm" in you:
    #     open_brower(you)
    #     count = 0
    elif "mở google và tìm kiếm" in you:
        google_search(you)
        count = 0
    elif "mở ứng dụng" in you:
        open_application()
        count = 0;
    elif "youtube" in you:
        youtube_search()
        count = 0
    elif "tìm kiếm trong máy" in you or "tìm kiếm" == you:
        number_disk()
        count = 0;
    elif "tạm biệt" in you or "bye" in you or "tắt" in you or "cảm ơn" in you:
        ai_brain = "Tạm biệt"
        ai_speak(ai_brain)
        break
    else:
        smart_AI(you)
        count = 0

    if count > 2 and you == "":
        ai_brain = "Hình như bạn đếch cần tôi nữa rồi, tạm biệt!"
        ai_speak(ai_brain)
        break
