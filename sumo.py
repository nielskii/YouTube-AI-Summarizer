import os
import datetime
from dotenv import load_dotenv
from pytubefix import YouTube
from pytubefix.cli import on_progress
from groq import Groq
import whisper
import re

load_dotenv()
chave_api = os.environ.get('GOOGLE_GEMINI_API')
hoje = datetime.date.today()
hoje_personalizado = hoje.strftime('%d/%m/%y')

class VideoSummarizer:
    def __init__(self,pasta_base="C:/projetos/resumo_videos"):
        self.pasta_videos = os.path.join(pasta_base, "videos")
        self.pasta_resumos = os.path.join(pasta_base, "resumosTxt")
        os.makedirs(self.pasta_videos, exist_ok=True)
        os.makedirs(self.pasta_resumos, exist_ok=True)


    def baixar_video(self,url):
        pasta_destino = "C:/projetos/resumo_videos/videos"
        os.makedirs(pasta_destino,exist_ok=True)
        caminho_video = os.path.join(pasta_destino,'resumo.mp4')
        video_removido = False
        if os.path.exists(caminho_video):
            os.remove(caminho_video)
            print('Video anterior removido')
            video_removido = True
        else:
            video_removido = True
        if video_removido:
            yt = YouTube(url,on_progress_callback=on_progress,use_oauth=True)
            print(f'{yt.title} - {yt.author}')
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path=pasta_destino,filename='resumo.mp4')
        return caminho_video,yt
            

    def transcrever_video(self,caminho_video):
        modelo = whisper.load_model("base")
        resposta = modelo.transcribe('C:/projetos/resumo_videos/videos/resumo.mp4', fp16=False)
        # print(f"Texto transcrito: {resposta['text']}") --> Tire esse comentário se quiser ver a transcrição completa no terminal
        if resposta:
            print('\nTranscrição concluída com sucesso...\n')
        return resposta['text']

    def api_groq(self,transcricao):
        client = Groq(
        # This is the default and can be omitted
        #api_key=os.environ.get("GROQ_API_KEY"),
        api_key="",
        )

        response = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant."
                    },
                    {
                        "role": "user",
                        "content": f"Resuma em português de forma coesa e completa e formatado para arquivo de txt, não precisa escrever esse prompt no arquivo e nem repetir a letra, apenas o resumo de uma forma totalmente inteligivel, apenas o conteudo do video e titulo: {transcricao}",
                    } 
                ],
                model="llama-3.3-70b-versatile",
                temperature= 0.5,
            )
        return response.choices[0].message.content

    def salvar_resumo(self,ys,resumo_ia):
        titulo_limpo = re.sub(r'[\\/*?:"<>|]',"",yt.title)
        autor_limpo = re.sub(r'[\\/*?:"<>|]',"",yt.author)
        caminho = f'C:/projetos/resumo_videos/resumosTxt/{titulo_limpo}_feito_por_{autor_limpo}'
        os.makedirs('C:/projetos/resumo_videos/resumosTxt/',exist_ok=True)
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            data = arquivo.write(f'\nData: {hoje_personalizado}\n')
            resumo = arquivo.write(f'{resumo_ia.choices[0].message.content}')
        print(f'Arquivo salvo com sucesso em: {caminho}')        
