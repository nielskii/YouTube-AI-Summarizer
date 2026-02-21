# 🤖 YouTube AI Summarizer

**`AI & Backend Intelligence`**

> [!CAUTION]
> ⚠️ **PROJETO EM MANUTENÇÃO**: Esta aplicação está em fase de desenvolvimento. Melhorias em validações de dados, tratamento de exceções em vídeos longos e otimização de transcrição estão sendo implementadas.

<br>

Este projeto é uma ferramenta poderosa de **Sumarização de Vídeos** que une o poder do processamento de linguagem natural (NLP) com a agilidade do Flask. A aplicação baixa vídeos do YouTube, transcreve o áudio localmente e utiliza modelos de linguagem de última geração para gerar resumos inteligentes.

<br>

# 📌 Sobre o Projeto:
<p align="justify">
  O fluxo de trabalho foi desenhado para ser totalmente automatizado, transformando horas de vídeo em minutos de leitura. A arquitetura segue o modelo de classes em Python (POO) para facilitar a manutenção.
  <br><br>
  <b>O Fluxo:</b>
  1. <b>Extração:</b> Download do vídeo via <b>Pytubefix</b> com integração OAuth para evitar bloqueios.
  2. <b>Transcrição:</b> O motor <b>Whisper (base model)</b> processa o áudio localmente, garantindo que o texto seja extraído com precisão.
  3. <b>IA Generativa:</b> O texto é enviado para o modelo <b>Llama 3.3-70b</b> via Groq, que condensa o conteúdo em um resumo estruturado.
  <br><br>
  <b>Estrutura de Pastas:</b> O sistema gerencia automaticamente o diretório <code>C:/projetos/resumo_videos</code>, criando subpastas para <code>videos</code> e <code>resumosTxt</code>.
</p>

### 🛠 Tecnologias e Ferramentas
<img 
    align="left" 
    alt="HTML5"
    title="HTML5" 
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg"
/>
<img 
    align="left" 
    alt="CSS3"
    title="CSS3" 
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" 
/>
<img 
    align="left" 
    alt="Python"
    title="Python" 
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
/>
<img 
    align="left" 
    alt="Flask"
    title="Flask" 
    width="30px" 
    style="padding-right: 10px;" 
    src="https://raw.githubusercontent.com/tandpfun/skill-icons/65dea6c4eaca7da319e552c09f4cf5a9a8dab2c8/icons/Flask-Dark.svg" 
/>
<img 
    align="left" 
    alt="OpenAI"
    title="Whisper (OpenAI)" 
    width="30px" 
    style="padding-right: 10px;" 
    src="https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg"
/>
<img 
    align="left" 
    alt="AI"
    title="Groq & Llama" 
    width="30px" 
    style="padding-right: 10px;" 
    src="https://skillicons.dev/icons?i=ai"
/>
<img 
    align="left" 
    alt="Git" 
    title="Git"
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" 
/>

<br/>
<br/>

### ⚙️ Funcionalidades Detalhadas

* **Gestão de Cache:** O sistema remove automaticamente vídeos antigos antes de iniciar um novo processamento para economizar espaço.
* **Sanitização de Arquivos:** Uso de Expressões Regulares (Regex) para garantir que títulos de vídeos com caracteres especiais não quebrem o sistema de arquivos do Windows.
* **Transcrição Local:** Independência de APIs pagas para transcrição, utilizando o modelo Whisper da OpenAI.
* **Resumos Customizados:** Prompt de sistema configurado para gerar saídas coesas, em português e prontas para leitura em formato `.txt`.

### 🛠️ Próximas Implementações (Roadmap)

* [ ] **Otimização de Performance:** Melhorar o tempo de resposta da IA e o processamento de áudio.
* [ ] **UI/UX Design:** Refinar o design do site para uma interface mais moderna e intuitiva.
* [ ] **Confirmação Visual:** Adicionar a miniatura (thumbnail) do vídeo para confirmação antes do resumo.
* [ ] **Feedback de Processamento:** Implementar uma tela/ícone de *Loading* enquanto a IA gera o resumo.
* [ ] **Rich Text:** Melhorar a formatação do texto de saída para facilitar a leitura.

### 🚀 Como Executar

1. **Pré-requisitos:**
   * Instale o [FFmpeg](https://ffmpeg.org/) (Essencial para o Whisper converter áudio).
   * Crie uma conta na [Groq Cloud](https://console.groq.com/) para obter sua API Key.

2. **Crie o ambiente virtual:**
   ```bash
   python -m venv venv
   
3. **Ative o ambiente virtual:**

   * **Windows:**
     ```bash
     .\venv\Scripts\activate.bat
     ```
   * **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

5. **Configure as variáveis de ambiente:**
````bash
  GROQ_API_KEY = sua_chave_aqui
````

6. **Inicie o servidor**
   ```
   python app.py
   
<p align="center">Feito por Daniel Borges</p>
