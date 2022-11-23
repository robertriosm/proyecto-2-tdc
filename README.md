# Proyecto 2: Teoría de la computación

## Descripcion

## Autores
- Rebecca Smith
- Luis Pedro Gonzalez
- Roberto Rios
## Modulos y temas

### Gramaticas

#### Convenciones
##### Formato de inicializacion de reglas de la gramatica

La series de reglas se meten una lista de tuplas que cumplen el siguiente formato, de acuerdo a la posición en la tupla: 
- 0: Simbolo del que parte
- 1: Contiene el lado derecho de la produccion en forma de lista, considerando or's, esta lista a su vez contiene sets que tiene por primera posicion el tipo de produccion (a terminales o no terminales) y la segunda la produccion en si.
- 2: (2) Tiene producciones a no terminales y a terminales, (1) contiene producciones a terminales unicamente, (0) contiene producciones a no terminales solamente
