# Danger-Jumper

Um mini jogo 2D feito com **Python** e **Pygame**, onde o jogador precisa pular para evitar inimigos que surgem continuamente. O objetivo? Sobreviver o máximo possível!

![image](https://github.com/user-attachments/assets/c31e558b-05eb-4b7e-ba8d-3db75d197910)

---

## 🎮 Como jogar

- Pressione **Espaço** para começar.
- Pressione **Espaço** para **pular** (até 2 pulos no ar).
- Não encoste nos inimigos ou é **game over**!

---

## 📂 Estrutura de pastas

my_game/
├── assets/             # Imagens e sons do jogo
│   ├── background.png
│   ├── player.png
│   ├── enemy.png
│   ├── music.wav
│   └── gameover.wav
│
├── code/               # Código-fonte do jogo
│   ├── main.py         # Ponto de entrada do jogo
│   ├── game.py         # Gerencia a execução do jogo
│   ├── level.py        # Lógica da fase (nível do jogo)
│   ├── player.py       # Classe do jogador
│   ├── enemy.py        # Classe dos inimigos
│   ├── background.py   # Classe para o fundo do jogo
│   └── game_menu.py    # Menu inicial
│
└── README.md           # Instruções e documentação do jogo

## 🛠 Requisitos

- Python 3
- Pygame

### Instalar dependências:

```bash
pip install pygame

## ▶️ Como rodar
cd code
python main.py

🧑‍💻 Feito por Rebeca (e o apoio técnico do ChatGPT 🤖)
Se curtiu, ⭐️ o repositório e compartilha!
