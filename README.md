El siguiente proyecto está inspirado en el cuento, la biblioteca de babel de Jorge Luis Borges.

# Objetivo: 
Elaborar un script que genere archivos .txt. Cada uno de estos archivos representará uno de los libros de la infinita (o casi) biblioteca.


# Pregunta 1: ¿Cuántas páginas tendría cada libro y cuantas líneas tendría cada página?

Por fortuna, el escritor nos facilita esta respuesta en la siguiente línea de su cuento: “Cada libro es de cuatrocientas diez páginas; cada página, de cuarenta renglones; cada renglón de unas ochenta letras de color negro.”

# Pregunta 2:  ¿Cuántos y cuáles símbolos se usarán?

Esta pregunta es mucho más complicada. Ya que, mi primer pensamiento era que la biblioteca del cuento estaba escrito con los símbolos del español. Sin embargo, la mente de Borges no es tan limitada, en la ficción propone 25 símbolos. Con el espacio y limitando la puntuación a los símbolos:"." y",". Como resultado, esto nos deja 22 símbolos desconocidos.

## Pregunta 2.1: ¿Cuáles son estos 22 símbolos desconocidos?

Investigando, logre dar con [un proyecto](https://libraryofbabel.info/) que, como es de esperarse, plantea objetivos parecidos a los de este proyecto. Con la diferencia de que el proyecto investigado es mucho más ambiciosos. En el apartado de teoría pude hallar la respuesta: 

        Borges da cuenta de estas 22 letras en su ensayo “La biblioteca total” , precursor del cuento. El ensayo traza la historia de la idea del lenguaje como una mera combinatoria de letras o palabras desde sus comienzos en el relato de Aristóteles sobre el filósofo atomista Leucipo hasta la actualidad. Presumiblemente, Borges parte del alfabeto español moderno de 30 letras y rechaza las letras dobles (ch, ll, rr) como innecesarias junto con la ñ. Los 26 restantes incluyen k y w, que aparecen solo en palabras prestadas. Borges luego elimina q como “completamente superfluo” (discutible) y x como meramente “una abreviatura”. En inglés esto se referiría a la combinación ks, aunque en español puede tener otros valores.

Según esto, la biblioteca de Borges quedaría con el siguiente alfabeto: a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, r, s, t, u, v, y, z.

El mismo proyecto decide usar las 26 letras del alfabeto inglés. También nos cuenta que puede haber tantas bibliotecas de babel como sistemas simbólicos existan y anima a que desarrollemos una de estas bibliotecas. Lo que me lleva a la pregunta. 

## Pregunta 2.2: ¿Se podría realizar una biblioteca con el alfabeto fonético internacional?

El alfabeto fonético internacional (AFI) fue creado para transcribir cualquier lengua del mundo. Basado en los símbolos griegos y latinos (pero sin que su sonido corresponda necesariamente al original). Cada símbolo corresponde a un sonido producido en alguna lengua humana. En este sentido, si permutamos cada uno de los símbolos en teoría, podríamos conseguir una biblioteca total. El verdadero inconveniente es como hacerlo.

## Pregunta 2.3: ¿Existe algún formato de codificación de caracteres donde se encuentren los símbolos de AFI?

UTF-8 uno de los sistemas de codificación de caracteres más utilizados, soporta perfectamente los símbolos del AFI. Ya que, este puede representar cualquier carácter del estándar Unicode. A su vez, el estándar Unicode contempla los caracteres latinos y griegos. Además de facilitar las variaciones que el AFI aplica a estos símbolos.

## Conclusión:
Para la presente biblioteca se usarán los 107 símbolos básicos y 55 modificadores del alfabeto fonético internacional.

Empezando por los 107 símbolos, estos se dividen entre letras, diacriticos y subrasegmentales. A su vez, las letras se dividen entre vocales y consonantes. Las vocales son fundamentales porque se encuentran en el núcleo de cada sílaba. Es decir, cada golpe de voz producido por el aparato fonético humano lleva consigo una vocal más explícita o implícitamente. Los símbolos de las vocales son los siguientes: i, y, ɯ, u, ɪ, ʏ, ʊ, e, ɘ, ɤ, o, ə, ɛ, œ, ɜ, ɞ, ʌ, ɔ, æ, ɐ, a, ɶ, ɑ, ɒ
