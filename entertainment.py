import media
import fresh_tomatoes

forma_dagua = media.Movie("Forma da Água",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcSsVWxdLjAFyWj0YtR6cHiB8qfNl96yfC5O5QHw8Y4Cupp4fK_5",
                          "https://www.youtube.com/watch?v=XFYWazblaUA")

pantera = media.Movie("Pantera Negra",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcQarmjVytz3ISRKJNwmxG7o-r4sWWN5VxbPp9qJauK4VvGrKu36",
                      "https://www.youtube.com/watch?v=iSwppsDP7jM")

touro_ferdinando = media.Movie("O Touro Ferdinando",
                         "http://t2.gstatic.com/images?q=tbn:ANd9GcTtJPK7Q2req8Mrqu7GrWebnmzwRp35uaCBX0V5TpPYwrykaeK-",
                         "https://www.youtube.com/watch?v=HBXVM7oUPVk"
                         )

doze_herois = media.Movie("12 Heróis",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcTMHHfVqP4f0DnfNMe0XijrqtJumLiQH9zyhSh7fe-UOi0Lk5KK",
                          "https://www.youtube.com/watch?v=-Denciie5oA&t=3s")

operacao_red_sparrow = media.Movie("Operação Red Sparrow",
                                   "http://t1.gstatic.com/images?q=tbn:ANd9GcR7tD9CdW1vvXginNUbZx4kLyu4c5VKYASz9KMQ6hS8e8Mn30jf",
                                   "https://www.youtube.com/watch?v=dh-OYpLaNtM")

viva = media.Movie("Viva - A Vida é uma Festa",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcQLlC1BU-d_49KZvZrLQ6vhp_dsWObCyp9a7UuJe0-8tpQcJ3fM",
                   "https://www.youtube.com/watch?v=zNCz4mQzfEI")


movies = [forma_dagua, pantera, touro_ferdinando, doze_herois, operacao_red_sparrow, viva]

# fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)

# for filme in lista_filmes:
#     filme.show_trailer()

# print(forma.title)
# forma.show_trailer()
