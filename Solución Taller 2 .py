#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
from zipfile import ZipFile
import fitz #Libreria para leer pdf


# In[27]:


direccion = 'C:/Users/Aleja/Documents/Universidad/NLP/Taller 2/python_books.zip'


# Descomprimimos el archivo ZIP

# In[ ]:


# Descomprimir el archivo ZIP
with ZipFile(direccion) as archivo:
    archivo.extractall("C:/Users/Aleja/Documents/Universidad/NLP/Taller 2/")

# Se elimina la carpeta adicional creada    
import shutil
shutil.rmtree('C:/Users/Aleja/Documents/Universidad/NLP/Taller 2/__MACOSX')
     


# Leemos el archivo e identificamos la cantidad de páginas

# In[13]:



for raiz, dirs, archivos in os.walk("C:/Users/Aleja/Documents/Universidad/NLP/Taller 2/python_books"):
        for a in archivos:
            documento = fitz.open("C:/Users/Aleja/Documents/Universidad/NLP/Taller 2/python_books/"+ a)
            
            print("Nombre archivo: ", a,  " Número de páginas: ", documento.pageCount)


# Como en el anterior paso nos dio como resultado que los archivos solo tenían una página, utilizamos el siguiente código para obtener el número de palabras en cada Archivo
# 

# In[24]:


for raiz, dirs, archivos in os.walk("C:/Users/Aleja/Documents/Universidad/NLP/Taller 2/python_books"):
        for a in archivos:
            documento = fitz.open("C:/Users/Aleja/Documents/Universidad/NLP/Taller 2/python_books/"+ a)
            pagina = documento.loadPage(0)
            texto = pagina.getText("text")
            data= texto.split()
             
            print("Nombre archivo: ", a,  " Número de páginas: ", documento.pageCount, 'Número de Palabras:  ', len(data))


# Por lo tanto se identifica que el archivo con más palabras es Data Science Cookbook.pdf 
