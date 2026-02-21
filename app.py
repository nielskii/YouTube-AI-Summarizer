import os
import datetime
from dotenv import load_dotenv
from pytubefix import YouTube
from pytubefix.cli import on_progress
from groq import Groq
import whisper
import re
from flask import Flask, render_template,request
from sumo import VideoSummarizer

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
summarizer = VideoSummarizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['GET'])
def summarize():
    url = request.args.get('url_video')
    caminho, info = summarizer.baixar_video(url)
    texto = summarizer.transcrever_video(caminho)
    resumo = summarizer.api_groq(texto)
    return render_template('index.html',resumo_ia = resumo)

if __name__ == "__main__":
    app.run(debug=True)