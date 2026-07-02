# DreamHell
## Contexto
Um projeto final para a disciplina de Introdução à Programação na UFPE. Nessa cadeira, aprendemos conceitos básicos de lógica de programação usando Python e, posteriormente, formamos grupos que aplicam esses conhecimentos na construção de um jogo orientado a objetos.
## Autores
| Nome completo                            | Curso na UFPE          | E-mail do CIn     | Conta no GitHub      |
| ---------------------------------------- | ---------------------- | ----------------- | -------------------- |
| Erick Lincoln de Souza                   | Ciência da Computação  | els11@cin.ufpe.br | [ericksouzasou][1]   |
| Helloisa Helena Gonzaga Silva dos Santos | Ciência da Computação  | hhgss@cin.ufpe.br | [helloisagonzaga][2] |
| Ialy Gabriela Soares da Silva            | Engenharia de Produção | igss2@cin.ufpe.br | [ialygabriela][3]    |
| Marcus Cézar Guimarães Carneiro          | Ciência da Computação  | mcgc@cin.ufpe.br  | [marcus-carneiro][4] |
| Ruan Porfirio Lima da Gama               | Ciência da Computação  | rplg@cin.ufpe.br  | [Rplg1501][5]        |
## Arquitetura do código
A arquitetura do nosso projeto inspirou-se no [modelo de projeto][6] disponibilizado pela monitora Safira Moraes, tendo a equipe decidido adotar uma modularização considerável do código a fim de deixá-lo mais organizado.
```
py-project/
├── assets/
│   ├── images/                  # Arquivos PNG e JPG com as texturas do jogo
│   └── music/                   # Arquivos MP3 com as músicas e efeitos sonoros do jogo
├── classes/
│   ├── boss.py                  # Classe Boss: comportamento do boss do jogo
│   ├── bullet.py                # Classes Bullet e SpecialBullet: definem as balas lançadas pelo jogador
│   ├── enemy.py                 # Classes Enemy e MiniSpider: definem as balas teleguiadas do boss
│   ├── game_object.py           # Classe Collectable e subclasses Heart, Potion e Battery: definem os coletáveis do jogo
│   ├── hud.py                   # Classe HUD: mostra o HUD do jogo com informações sobre vida e quantidade de coletáveis coletados
│   ├── player.py                # Classe Player: define a movimentação, ataques e dados do jogador
│   ├── screen_paramaters.py     # Classe ScreenParameters: define a resolução do jogo
├── utils/
│   ├── animation.py             # Classe Animations: torna uma sheet de sprites numa animação
│   ├── button.py                # Classe Button: define os botões do menu
│   ├── collision.py             # Funções check_collision e check_object_group_collision: definem respectivamente a colisão entre dois objetos e a colisão entre um objeto e um grupo
│   ├── helpers.py               # Classe Helpers: ajusta as imagens do jogo
│   ├── menu.py                  # [não existe]
│   ├── options.py               # [não existe]
│   ├── spritesheet.py           # Classe SpriteSheet: corta as spritesheets em sprites
│   └── text.py                  # [?????]
├── main.py                      #
└── constants.py                 # Define algumas constantes com cores, fontes etc.
```
## Ferramentas utilizadas
 - **Git** e **GitHub**, recursos padrão para a organização de código escrito por múltiplas pessoas;
 - **Python** 3.13, a linguagem de programação obrigatória para todo o código na disciplina de IP;
 - **Pygame** 2.6.1, uma biblioteca de Python que traz recursos essenciais para o desenvolvimento de jogos;
 - **VS Code** e **PyCharm** para edição de código;
 - **StackEdit** para edição de Markdown;
 - **LMMS** para a criação de música e efeitos sonoros originais;
 - **Aseprite** para a criação de sprites.
## Divisão de tarefas
 - Todos os membros: geração de ideias;
 - Erick: base do código, movimentação dos personagens, elaboração das artes (sprites, efeitos sonoros e músicas);
 - Ialy e Ruan: mecânicas de combate;
 - Helloisa: mecânicas de combate, slides;
 - Marcus: gerenciamento dos ambientes e da arquitetura do projeto; documentação; interfaces.
## Conceitos da disciplina utilizados
### Conceitos aprendidos nas listas
 - **Condicionais (if/else)** foram basilares para as mecânicas de jogo pois processam as entradas do jogador.
 - **Laços de repetição** foram usados para que diferentes sprites se repitam várias vezes para formar uma animação e também para a geração dos coletáveis no mapa.
 - **Listas e tuplas** foram essenciais para as animações e outros diversos usos.
 - **Funções** 
### Conceitos aprendidos após as listas
 - **Classes** e **métodos** foram usadas para criar objetos que caracterizam os coletáveis, os personagens e as balas; também foram usadas como utilitários para animações e apresentação do jogo.
 - **Polimorfismo** e **herança** foram usados várias vezes para as subclasses, principalmente nos coletáveis.
 - **Abstração** foi utilizada para facilitar a compreensão de todo o código.
 ## Desafios, erros e lições aprendidas
 ### Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
 O principal erro foi a falta de organização e de uma gestão de tempo mais eficiente. Apesar de haver uma divisão de tarefas, nem sempre ela foi seguida corretamente, o que prejudicou o andamento do trabalho. Em vários momentos, acabamos tentando “acelerar” o projeto de forma desorganizada, chegando a virar noites para conseguir finalizar as atividades. Para lidar com isso, realizamos reuniões em grupo para concentrar a produção e conseguir concluir o que estava pendente.
### Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
A dificuldade em utilizar as plataformas necessárias para a realização do projeto, o que gerou atrasos em algumas etapas e exigiu tempo adicional de adaptação e aprendizado.
### Quais as lições aprendidas durante o projeto?
Como lições aprendidas, destacamos a importância de seguir o planejamento estabelecido, respeitar a divisão de tarefas e manter uma gestão de tempo mais consistente. Também aprendemos que a organização ao longo do processo é essencial para evitar sobrecarga no final e que o uso adequado das ferramentas desde o início pode facilitar significativamente o desenvolvimento do trabalho.
## Como executar o jogo
### Informações importantes
 - Os pré-requisitos são um computador com acesso ao GitHub na instalação e Python 3.13 (o jogo provavelmente funciona em outras versões do Python, mas ele não foi testado nelas).
 - Ao realizar o passo a passo, `python` provavelmente deve ser substituído por `py`, `python3`, `python3.13` ou outro nome a depender de seu sistema operacional e de como a instalação do Python foi feita.
### Passo a passo
1. Abrir o terminal
2. Acessar a pasta em que deseja armazenar o jogo
3. Clonar o repositório com `git clone https://github.com/equipe5-ipufpe-20261ccia/py-project/`
4. Acessar a pasta do repositório com `cd py-project`
5. Criar um ambiente virtual Python com `python -m venv .venv`
6. Ativar o ambiente virtual
	- No macOS ou Linux use `source .venv/bin/activate`
	- No CMD do Windows use `.venv\Scripts\Activate.bat`
	- No Windows Powershell use `.venv\Scripts\Activate.ps1`	
7. Instalar a biblioteca necessária para a execução com `python -m pip install pygame`
8. Executar finalmente o jogo com `python main.py`

<!-- Links referenciais -->
[1]: https://github.com/ericksouzasou
[2]: https://github.com/helloisagonzaga
[3]: https://github.com/ialygabriela
[4]: https://github.com/marcus-carneiro
[5]: https://github.com/Rplg1501
[6]: https://github.com/safiracode/Game_Template
