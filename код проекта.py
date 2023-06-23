import speech_recognition as sr
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog



def add_video():
    video_file = tk.filedialog.askopenfilename(initialdir='/', title='Выберите фаайл', filetypes=(('MP4 файлы', '*.mp4'),('Все файлы', '*.*')))
    video_path.insert(tk.END, video_file)

def extract_text():
    video = video_path.get()
    try:
        clip = mp.VideoFileClip(video)
        audio = clip.audio
        audio.write_audiofile('audio.wav')

        r = sr.Recognizer()
        with sr.AudioFile('audio.wav') as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language='ru-RU')

        for_text.delete(1.0, tk.END)
        for_text.insert(tk.END, text)

    except OSError:
        for_text.delete(1.0, tk.END)
        for_text.insert(tk.END, 'Я не нашел видео по такому пути. Возможно вы забыли написать расширение')
    except KeyError:
        for_text.delete(1.0, tk.END)
        for_text.insert(tk.END, 'Вы ввели файл с другим расширением.')


root = tk.Tk()
root.title('Извлечение текста из видео')
root.geometry('700x650')
root.resizable(False, False)



download_label = tk.Label(root, text='Введите путь к видео:', font=35)
download_label.place(x=230, y=20)

video_path = tk.Entry(root, width=70)
video_path.place(x=135, y=60)

button_choose = tk.Button(root, text='Выбрать видео', font=10, width=17, command=add_video)
button_choose.place(x=135, y=85)

button_do = tk.Button(root, text='Извлечь текст', font=10, width=17, command=extract_text)
button_do.place(x=350, y=85)

upload_label = tk.Label(root, text='Текст:', font=35)
upload_label.place(x=290, y=150)

for_text = tk.Text(root)
for_text.place(x=26, y=185)


root.mainloop()