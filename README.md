
# ProyectoETL

Este proyecto consiste en la extracción, transformación y limpieza de datos para crear un database de todas las películas, series y documentales de Netflix. Para ello, he realizado un proceso de ETL utilizando 3 métodos diferentes: 
- Descarga de csv. de películas y actores de Netflix de Kaggle
- Descarga de csv. de película de Netflix Original Films & IMDB Scores de Kaggle
- Webscraping de reseñas y comentarios de cada película desde la página de IMDB
- Descarga de todos los géneros de cada película a través de la API de TMDB


1. CSV.

Descarga del csv Netflix TV Shows and Movies, Movies and TV Shows listings on Netflix (July, 2022), de VICTOR SOEIRO
https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies

y de Netflix Original Films & IMDB Scores, Netflix Films since 06/01/2021, de LUIS
https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores

2. Creamos un código se scrapeo del HTML de la página de IMDB para obtener las reviews y el rating de cada pleícula. Ejemplo:

            Output

            Review: A one-of-a-kind mind-blowing masterpiece!
            Rating: 10/10
            ------------------------------
            Review: Is it possible the makers understand how incredible this film is?
            Rating: 10/10
            ------------------------------
            Review: Answering all the questions with one answer: I feel guilt. ⭐
            Rating: 10/10
            ------------------------------
            Review: Inception was only less shocking to me than the Matrix
            Rating: 10/10
            ------------------------------
            Review: Insanely Brilliant ! Nolan has outdone himself !!
            Rating: 10/10
            ------------------------------
            Review: Didn't win Best Picture? WHAT?
            Rating: 10/10
            ------------------------------
            Review: In a Decade, "Inception" May Be A Religion
            Rating: 10/10
            ------------------------------
            Review: Amazingly original...but also a bit overwhelming.
            Rating: 8/10
            ------------------------------

3. Creamos un código para extraer los géneros de cada película a través de la API de TMDB.

4. Limpieza de datos:

4.1. Renombramos tablas, hacemos merge() y reorganizamos las tablas para darles sentido a las relaciones que existen entre ellas.
4.2. Valoramos qué nulos eliminar. Por ejemplo, para la tabla Age_certification, si encontramos algún valor nulo cuyo género de la película sea Horror, lo cambiamos por R (+17).
Los dataset, por lo general, estaban bastante limpios, igualmente he tomado la decisión de eliminar las filas que tenian valores nulos en los ids, ya que, curiosamente, también tenían nulos el resto de valores de la fila.

5. Subida de tablas a la base de datos (SQL)






