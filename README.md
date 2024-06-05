# SmartPool

## Descripción

La smart pool es una piscina inteligente con los procesos totalmente  automatizados

-Contiene los siguientes sensores y actuadores

- Motores que abren y cierran la cubierta
- Pantalla LCD que indica mi nombre, el nombre del proyecto e instituto, la temperatura, la humedad, y la cantidad de luz
- Ventilador que se activa mediante un relé cuando el sensor DHT11 capta cierta temperatura
- LED RGB que indica la temperatura del ambiente con un sencillo código de color
## Fritzing



## Programación

Para programar el código de mi maqueta , primero tuve que hacer el código de cada parte por separado, y acto seguido se combinar todos los códigos en uno mismo para toda la maqueta

### Botones

En el caso de mi maqueta los botones y el final de carrera están programados para poder abrir,cerrar y parar la cubierta cuando queramos

### LDR

El LDR lo utilicé ligado a los motores, para que cuando detecten un bajo nivel de luz se activen para cerrar la cubierta

### DHT11

Este sensor se encarga de medir la temperatura y humedad de ambiente, ambos datos se muestran en la LCD, acto seguido en función de la temperatura se activan el ventilador y un LED RGB 

### Pantalla

La pantalla LCD la utilicé para poder mostrar datos como mi nombre, el nombre del proyecto, la temperatura y humedad del ambiente y por último la cantidad de luz detectada

### Ventilador

Este componente actúa en función de la temperatura, a partir de ciertos grados el código hace que un réle se accione haciendo asi que el ventilador se active

### LED RGB

En el caso de el LED RGB, Al igual que el ventilador, actua en función de la temperatura utilizando colores para indicarnos las temperaturas: Rojo (Calor), Verde (Templado), y Azul (Frio).<br/>
