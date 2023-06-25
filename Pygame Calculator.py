import pygame


# Configuração da tela
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CALCULADORA")
numeros_display = [" ",""]

# Cores
black = (0,0,0)
white = (255, 255, 255)
azulbb = (222, 255, 255)
lgreen= (0, 255, 143)
dred = (178, 0, 0)
purple = (255, 0, 255)

# Palavras
def palavra(text,font,text_col,x,y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x,y))

pygame.font.init()
text_font = pygame.font.SysFont('Arial',30)
text_font2 = pygame.font.SysFont('Arial',60)
text_font3 = pygame.font.SysFont('Arial',90)

#Texto números
def texto ():
  global numero_no_display
  global numeros_display
  global font
  font = pygame.font.Font("ARIAL.TTF", 50)
  t = font.render("".join(numeros_display), True, (0,0,0))
  screen.blit(t, t.get_rect(top = 60, left = 40))
  numero_no_display = str("".join(numeros_display))
# Estrutura gráfica
def grafico():
  pygame.draw.rect(screen, white, (0, 0, 550, 700))
  pygame.draw.rect(screen, azulbb, (30, 50, 490, 85))
  #botões
  pygame.draw.rect(screen, black, (30, 180, 70, 70))
  pygame.draw.rect(screen, black, (170, 180, 70, 70))
  pygame.draw.rect(screen, black, (310, 180, 70, 70))
  pygame.draw.rect(screen, lgreen, (450, 180, 70, 70))
  pygame.draw.rect(screen, black, (30, 320, 70, 70))
  pygame.draw.rect(screen, black, (170, 320, 70, 70))
  pygame.draw.rect(screen, black, (310, 320, 70, 70))
  pygame.draw.rect(screen, lgreen, (450, 320, 70, 70))
  pygame.draw.rect(screen, black, (30, 460, 70, 70))
  pygame.draw.rect(screen, black, (170, 460, 70, 70))
  pygame.draw.rect(screen, black, (310, 460, 70, 70))
  pygame.draw.rect(screen, lgreen, (450, 460, 70, 70))
  pygame.draw.rect(screen, black, (170, 600, 70, 70))
  pygame.draw.rect(screen, lgreen, (450, 600, 70, 70))
  pygame.draw.rect(screen, dred, (310, 600, 70, 70))
  pygame.draw.rect(screen, purple, (30, 600, 70, 70))



# Funcionamento
def clicar_numero(x, numero):
  global numero_a
  mouse_click = pygame.mouse.get_pressed()
  if mouse_click[0] and numero.collidepoint(pygame.mouse.get_pos()) == True:
    numeros_display.append(str(x))
    if x == "+" or x == "*" or x == "/" or x == "-":
      numero_a = int(str(numero_no_display[0:]))
      


# Operações
def igual_simbolo ():
  global numero_b
  mouse_click = pygame.mouse.get_pressed()
  if mouse_click[0] and num_i.collidepoint(pygame.mouse.get_pos()) == True:
    numero_igual = str(numero_no_display+"=")
    i1 = numero_igual.find("+")
    i2 = numero_igual.find("*")
    i3 = numero_igual.find("-")
    i4 = numero_igual.find("/")
    if i1 != -1:
      numero_b = int(numero_igual[i1+1:-1])
      numeros_display.clear()
      numeros_display.append(str(numero_a + numero_b))
    elif i2 != -1:
      numero_b = int(numero_igual[i2+1:-1])
      numeros_display.clear()
      numeros_display.append(str(numero_a * numero_b))
    elif i3 != -1:
      numero_b = int(numero_igual[i3+1:-1])
      numeros_display.clear()
      numeros_display.append(str(numero_a - numero_b))
    elif i4 != -1:
      numero_b = int(numero_igual[i4+1:-1])
      numeros_display.clear()
      numeros_display.append(str(numero_a / numero_b))

def novo_calculo():
  mouse_click = pygame.mouse.get_pressed()
  if mouse_click[0] and num_c.collidepoint(pygame.mouse.get_pos()) == True:
    numeros_display.clear()




clock = pygame.time.Clock()

def update():
  clicar_numero("0", num_0)
  clicar_numero("1", num_1)
  clicar_numero("2", num_2)
  clicar_numero("3", num_3)
  clicar_numero("4", num_4)
  clicar_numero("5", num_5)
  clicar_numero("6", num_6)
  clicar_numero("7", num_7)
  clicar_numero("8", num_8)
  clicar_numero("9", num_9)
  clicar_numero("+", num_a)
  clicar_numero("-", num_s)
  clicar_numero("*", num_m)
  clicar_numero("/", num_d)
  igual_simbolo()
  novo_calculo()
  



  
    

# Loop principal da calculadora
running = True
while running:

  grafico()
  #números
  palavra('1', text_font, white, 30, 180)
  palavra('2', text_font, white, 170, 180)
  palavra('3', text_font, white, 310, 180)
  palavra('4', text_font, white, 30, 320)
  palavra('5', text_font, white, 170, 320)
  palavra('6', text_font, white,310,320)
  palavra('7', text_font, white,30,460)
  palavra('8', text_font, white,170,460)
  palavra('9', text_font, white,310,460)
  palavra('0', text_font, white,170,600)
  palavra('+', text_font2, white,460, 175)
  palavra('-', text_font3, white,468, 295)
  palavra('x', text_font2, white,468, 455)
  palavra('=', text_font2, white,320, 595)
  palavra('/', text_font2, white,477, 595)
  palavra('C', text_font2, white,40, 595)
  
  
  num_1 = pygame.Rect((30, 180, 70, 70))
  num_2 = pygame.Rect((170, 180, 70, 70))
  num_3 = pygame.Rect((310, 180, 70, 70))
  num_4 = pygame.Rect((30, 320, 70, 70))
  num_5 = pygame.Rect((170, 320, 70, 70))
  num_6 = pygame.Rect((310, 320, 70, 70))
  num_7 = pygame.Rect((30, 460, 70, 70))
  num_8 = pygame.Rect((170, 460, 70, 70)) 
  num_9 = pygame.Rect((310, 460, 70, 70))
  num_0 = pygame.Rect((170, 600, 70, 70))
  num_a = pygame.Rect((450, 180, 70, 70))
  num_s = pygame.Rect((450, 320, 70, 70))
  num_m = pygame.Rect((450, 460, 70, 70))
  num_d = pygame.Rect((450, 600, 70, 70))
  num_i= pygame.Rect((310, 600, 70, 70))
  num_c = pygame.Rect((30, 600, 70, 70))
  texto()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      update()
  
      
  
  
  clock.tick(60)
  pygame.display.update()  

pygame.quit()
