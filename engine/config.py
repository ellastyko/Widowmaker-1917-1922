from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy
import time, sys
import os

X = Y = Z = 1.0
rotate_z = rotate_y = rotate_x = 0.0
scale = 1.0


# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# # from image import *
# from PIL import Image

# ESCAPE = '\033'

# window = 0

# xrot = yrot = zrot = 0.0

# texture = 0

# def LoadTextures():
#     image = open("map_fe.tga")
#     print (image.format, image.size, image.mode)

#     ix = image.size[0]
#     iy = image.size[1]
#     image = image.tostring("raw", "RGBA", 0, -1)
	
#     glPixelStorei(GL_UNPACK_ALIGNMENT,1)
#     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)


# def InitGL(Width, Height):
#     LoadTextures()
#     glEnable(GL_TEXTURE_2D)
#     glClearColor(0.0, 0.0, 0.0, 0.0)
#     glClearDepth(1.0)
#     glDepthFunc(GL_LESS)
#     glEnable(GL_DEPTH_TEST)
#     glShadeModel(GL_SMOOTH)
	
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

#     glMatrixMode(GL_MODELVIEW)


# def ReSizeGLScene(Width, Height):
#     if Height == 0:
# 	    Height = 1

#     glViewport(0, 0, Width, Height)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
#     glMatrixMode(GL_MODELVIEW)


# def DrawGLScene():
# 	global xrot, yrot, zrot, texture

# 	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# 	glLoadIdentity()
    
# 	glTranslatef(0.0,0.0,-5.0)

# 	glRotatef(xrot,1.0,0.0,0.0)			
# 	glRotatef(yrot,0.0,1.0,0.0)			
# 	glRotatef(zrot,0.0,0.0,1.0)		

#     # glPushMatrix()
# 	glBegin(GL_QUADS)			    
	
# 	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	
# 	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	
# 	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	
# 	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	
	
# 	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)	
# 	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	
# 	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	
# 	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)	
	
# 	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	
# 	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)	
# 	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)	
# 	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	
	
# 	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)	
# 	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)	
# 	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	
# 	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	
	
# 	glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)	
# 	glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	
# 	glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	
# 	glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	
	
# 	glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)	
# 	glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	
# 	glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	
# 	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	
	
# 	glEnd()				
#     # glPopMatrix()
  

#     # glPushMatrix()
# 	glBegin(GL_QUADS)			    
	
# 	glTexCoord2f(0.0, 0.0); glVertex3f(-5.0, -5.0,  -10.0)	
# 	glTexCoord2f(1.0, 0.0); glVertex3f( 5.0, -5.0,  -10.0)	
# 	glTexCoord2f(1.0, 1.0); glVertex3f( 5.0,  5.0,  -10.0)	
# 	glTexCoord2f(0.0, 1.0); glVertex3f(-5.0,  5.0,  -10.0)	
	
#     # glEnd()                              
# 	glPopMatrix()
		
# 	xrot  = xrot + 0.02                
# 	yrot = yrot + 0.02                 
# 	zrot = zrot + 0.02                 

# 	glutSwapBuffers()


# def keyPressed(*args):
#     if args[0] == ESCAPE:
# 	    glutDestroyWindow(window)
# 	    sys.exit()

# def main():
#     global window
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
#     glutInitWindowSize(640, 480)
#     glutInitWindowPosition(0, 0)

#     window = glutCreateWindow("Transparency Test")
#     glutDisplayFunc(DrawGLScene)
#     glutIdleFunc(DrawGLScene)
#     glutReshapeFunc(ReSizeGLScene)
#     glutKeyboardFunc(keyPressed)
#     InitGL(640, 480)
#     glutMainLoop()


# main()
