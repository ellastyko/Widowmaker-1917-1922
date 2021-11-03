from config import *
from handlers import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
scale = 1.0
textureID = 0

def board():
    # for i in range(590):
    #     for j in range(378):

    #         x=i*Zoom
    #         y=j*Zoom; 
    #         glBegin(GL_TRIANGLE_STRIP)

    #         glTexCoord2f(i*TextureBit, j*TextureBit)
    #         glVertex3f(x, y, HeightMap[i][j])
    #         glTexCoord2f((i + 1)*TextureBit, j*TextureBit)
    #         glVertex3f(x+Zoom, y, HeightMap[i+1][j])
    #         glTexCoord2f(i*TextureBit,(j + 1)*TextureBit)
    #         glVertex3f(x, y+Zoom, HeightMap[i][j+1])
    #         glTexCoord2f((i + 1)*TextureBit,(j + 1)*TextureBit)
    #         glVertex3f(x+Zoom, y+Zoom, HeightMap[i+1][j+1])

    #         glEnd()
  

    glEnable( GL_TEXTURE_2D )
    glBindTexture(GL_TEXTURE_2D, textureID)
    glBegin(GL_QUADS)
    glTexCoord2f(1, 1)
    glVertex3f(30, 0, -1)

    glTexCoord2f(0, 1)
    glVertex3f(-30, 0, -1)

    glTexCoord2f(0, 0)
    glVertex3f(-30, 0, -4)

    glTexCoord2f(1, 0)
    glVertex3f(30, 0, -4)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
def key_pressed(key, x, y):
    print(key[0])
    global X, Y, Z
    if key[0] == 119:
        Z -= 0.5
    elif key[0] == 115:
        Z += 0.5
    elif key[0] == 100:
        X += 0.5
    elif key[0] == 97:
        X -= 0.5
    elif key[0] == 'u':
        Y += 0.5

    glutPostRedisplay()

def special_key(key, x, y):
    global rotate_y, rotate_z, rotate_x, scale
    global X, Y, Z
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх    
        rotate_x -= 2.0             # Уменьшаем угол вращения по оси X    
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        rotate_x += 2.0             # Увеличиваем угол вращения по оси X   
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        rotate_y -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        rotate_y += 2.0             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки

#  Mouse click
def mouse(key, status, x, y):
    global scale
    # print(key, status, x, y)
    if key == 1:
        pass
    elif key == 2:
        pass
    elif key == 3:
        scale += 0.1
    elif key == 4:
        scale -= 0.1
    
    glutPostRedisplay()         # Вызываем процедуру перерисовки

    
def display():
    global rotate_x, rotate_y, rotate_z, scale
    global X, Y, Z
    glClearColor(0.9, 0.6, 0.4, 0) # Фон
    glClear        ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ) # Clear screen
    glEnable( GL_DEPTH_TEST)
    
    glMatrixMode   ( GL_MODELVIEW )
    glLoadIdentity () # Возвращает систему координат в начальное положение после сдвига translatef

    # gluLookAt( 
    #     0.0, 1.0, 1.0,
    #     0.0, 0.0, -1.0,  
    #     0.0, 0.0, 1.0
    # )
    glRotatef(rotate_x, 1.0, 0.0, 0.0)
    glRotatef(rotate_y, 0.0, 1.0, 0.0)
    # glRotatef(rotate_z, 0.0, 0.0, -1.0)

    glTranslatef(0.0, 1.0, 0.0) # Смещение оси
    glFrustum(-10.0, 10.0, -10.0, 10.0, 1.0, 20.0)
    glScalef(scale, 1.0 , 1.0)

    
    board()
    

    glutSwapBuffers ()

def Init(filename='textures/screen-10.jpg'): #screen-10.jpg

    # PIL can open BMP, EPS, FIG, IM, JPEG, MSP, PCX, PNG, PPM
    # and other file types.  We convert into a texture using GL.
    print('trying to open', filename)
    try:
        image = Image.open(filename)
    except IOError as ex:
        print('IOError: failed to open texture file')
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        return -1
    print('opened file: size=', image.size, 'format=', image.format)
    imageData = numpy.array(list(image.getdata()), numpy.uint8)
    # print(len(imageData))
    global textureID
    textureID = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, textureID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1],
        0, GL_RGB, GL_UNSIGNED_BYTE, imageData)

    image.close()
    return textureID
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowPosition( 0, 0 )
    glutInitWindowSize( 1600, 900 )
    glutCreateWindow('Widowmaker 1917-1922')
    
    Init()
   
    glutKeyboardFunc(key_pressed)	
    glutSpecialFunc(special_key)  
    glutReshapeFunc(change_size)
    glutMouseFunc(mouse)
    glutMotionFunc(on_motion)

    glutDisplayFunc(display)
    
    glutMainLoop()
    
	
	

if __name__ == "__main__":
	main()

