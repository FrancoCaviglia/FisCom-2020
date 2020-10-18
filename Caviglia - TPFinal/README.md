# Trabajo Práctico Final
## Modelo de Ising
### Física Computacional - Instituto Balseiro

En este repositorio se encuentran los códigos utilizados para la implementación de la simulación por medio del algoritmo de Metrópolis, al a vez que están los usados en el análisis de los datos. Para lo primero se utilizó C++, mientras que para lo segundo se hizo uso de Python. Dado que para cada parte del trabajo se usaron versiones ligeramente diferentes del mismo código, a los efectos de presentarlas de forma organizada se las distribuyó en subcarpetas dentro de */Problemas*, siguiendo como criterio el orden de los problemas de la Guía del Trabajo (sólo a efectos oorientativos).

Una versión del código de la simulación que sólo realiza una ejecución para un tamaño fijo de grilla y pasos de tiempo se muestra en la carpeta principal (*Ising-MC.cpp*). Las restantes versiones agregan sólamente loops, salvo en el caso del *Problema 8* donde la presencia del campo magnético exige ser más cuidadoso con el manejo de las probabilidades en los pasos de montecarlo. 

Los scripts en Python tienen la finalidad de levantar la información generada por la simulación, procesarla cuando sea necesario y armar con ella figuras. Las presentadas en el informe y algunas más se guardan también las carpetas de Problemas.

Para realizar las simulaciones se dispuso de notebooks de uso personal y en forma adicional de dos Máquina Virtuales montadas en el servicio de Clouding de Azure. Ambas dos estaban configuradas con 16 GB de memoria RAM y procesador Intel Xeon E5-2673 v4 a 2.30 GHz. Su uso principal fue realizar las 500 copias en el barrido de temperaturas de 0.5 a 5 y tamaños de 10 a 100, con pasos de 0.02 y 10 respectivamente.  

Ante cualquier inconveniente con los códigos o consultas sobre su uso, por favor contactar indistintamente a

- franco.caviglia.roman@gmail.com
- franco.caviglia@ib.edu.ar.

Los resultados de las simulaciones usadas para la confección del informe se guardan en la carpeta de Google Drive
https://drive.google.com/drive/u/1/folders/103bWd7fU80ZYb58DuUjj5Auhmj2ap-ik
