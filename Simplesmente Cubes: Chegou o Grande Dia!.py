#pgzero
import time

fundo = Actor("fundo_do_jogo")

WIDTH = fundo.width
HEIGHT = fundo.height
TITLE = "Simplesmente Cubes: Chegou o Grande Dia!"
FPS = 30

# Gráficos

transicao = Actor("transicao1")
glimmer = Actor("glimmer", (WIDTH // 2, HEIGHT // 1.8), size=(150, 150))
botao_jogar = Actor("botao_jogar", (WIDTH // 2, HEIGHT // 1.8), size = (500, 277))
chapeu_do_inicio = Actor("Chapeu_do_inicio", (WIDTH // 3.5, HEIGHT // 3.2), size = (100, 100))
fundo_permitido = Actor("fundo_do_jogo_cortado", (WIDTH // 2, HEIGHT // 2), size=(WIDTH, HEIGHT))
teto = Actor("tetos", (WIDTH // 2, HEIGHT // 2), size=(WIDTH, HEIGHT))
mode = "menu"
a = 0
fundo_timer = 0
fundo_frame = 1
teto_visivel = True
# Função para transição
def transicao_1():
    global a
    a = 1
    time.sleep(0.2)
    transicao.image = "transicao2"
    time.sleep(0.2)
    transicao.image = "transicao3"
    time.sleep(0.2)
    transicao.image = "transicao4"
    time.sleep(0.2)
    transicao.image = "transicao5"

def transicao_2():
    global a
    time.sleep(0.2)
    transicao.image = "transicao4"
    time.sleep(0.2)
    transicao.image = "transicao3"
    time.sleep(0.2)
    transicao.image = "transicao2"
    time.sleep(0.2)
    transicao.image = "transicao1"
    time.sleep(0.2)
    a = 0

# Animação inicial
def fundo_inicial():
    global fundo
    fundo.image = "fundo_inicial1"
    time.sleep(0.2)
    fundo.image = "fundo_inicial2"
    time.sleep(0.2)
    fundo.image = "fundo_inicial3"

# Desenhando gráficos
def draw():
    fundo.draw()

    if a == 1:
        transicao.draw()

    if mode == "menu":
        botao_jogar.draw()
        chapeu_do_inicio.draw()

    if mode == "game":
        fundo_permitido.draw()
        glimmer.draw()
        if teto_visivel:
            teto.draw()

# Atualização do jogo
def update(dt):
    global mode, fundo_timer, fundo_frame, teto_visivel

    # Controles
    if mode == "game":
        if keyboard.left:
            glimmer.image = "glimmer_left"
            glimmer.x -= 5

        elif keyboard.right:
            glimmer.image = "glimmer_right"
            glimmer.x += 5

        if keyboard.up:
            glimmer.image = "glimmer"
            glimmer.y -= 5

        elif keyboard.down:
            glimmer.image = "glimmer"
            glimmer.y += 5

    # Reiniciar
    if mode == "fim" and keyboard.enter:
        mode = "menu"

    # Definindo fundo do jogo
    if mode == "game":
        fundo.image = "fundo_do_jogo"
    
    elif mode == "menu":
        fundo_timer += dt
    
        if fundo_timer >= 0.2:
            fundo_timer = 0
            fundo_frame += 1
    
            if fundo_frame > 3:
                fundo_frame = 1
    
        fundo.image = "fundo_inicial" + str(fundo_frame)
    
    elif mode == "fim":
        fundo.image = "fundo_final"
    
    else:
        fundo.image = "fundo_erro"
    # Fazendo o teto desaparecer ao entrar na casa
        global teto_visivel

    if mode == "game":
        if teto_visivel and glimmer.colliderect(teto):
            teto_visivel = False
            fundo.image = "fundo escurecido"
        elif teto_visivel:
            fundo.image = "fundo_do_jogo"

    # passar do menu
    if mode == "menu" and keyboard.space:
        mode = "game"


    if glimmer.left < 0:
        glimmer.left = 0
    if glimmer.right > WIDTH:
        glimmer.right = WIDTH
    if glimmer.top < 0:
        glimmer.top = 0
    if glimmer.bottom > HEIGHT:
        glimmer.bottom = HEIGHT
# Clique do mouse
def on_mouse_down(pos, button):
    global mode

    if button == mouse.LEFT:
        if mode == "menu" and botao_jogar.collidepoint(pos):
            mode = "game"
