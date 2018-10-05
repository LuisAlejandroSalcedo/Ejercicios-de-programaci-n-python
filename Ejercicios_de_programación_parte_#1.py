
# coding: utf-8

# # Ejercicios de Programación Python
# 

# 1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

# In[1]:


def max(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    
max(2,5)


# 2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

# In[2]:


def max_de_tres(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

max_de_tres(5,3,7)


# 3- Definir una función que calcule la longitud de una lista o una cadena dada. 

# In[3]:


def len_cadena(string):
    cont = 0
    for i in string:
        cont = cont + 1
    return cont

len_cadena("Hola Mundo")


# 4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

# In[5]:


def is_vocal(char):
    lista_vocales = ['a','e','i','o','u']
    for vocales in lista_vocales:
        if char == vocales:
            return True
    return False

is_vocal('r')


# 5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.

# In[10]:


def sum(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

def multip(lista):
    mult = 1
    for num in lista:
        mult *= num
    return mult

multip([1,4,5])


# 6- Definir una función inversa() que calcule la inversión de una cadena.

# In[12]:


def inversa(string):
    invertida = ""
    cont = len_cadena(string)
    indice = -1
    while cont >= 1:
        invertida += string[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

inversa("Luis")


# 7- Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas)

# In[ ]:


def es_palindromo(string):
    palabra_in = inversa(string)
    indice = 0
    cont = 0
    
    for i in range(len_cadena(string)):
        if palabra_in[indice] == string[indice]:
            indice += 1
            cont += 1
        else:
            print("No es palindromo")
            break
            
    if count == len_cadena():
        print("Es palindromo")


# 8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. 

# In[14]:


def superposicion(lista1, lista2):
    for num in lista1:
        for x in lista2:
            if num == x:
                return True
    return False

superposicion([1,2,3],[1,4,5])


# 9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

# In[16]:


def generar_n_caracteres(n, char):
    return n * char

generar_n_caracteres(5, "w")


# 10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 

# In[18]:


def procedimiento(lista):
    for i in lista:
        print(i*"X")
        
procedimiento([1,4,5,6,8,10,12])

