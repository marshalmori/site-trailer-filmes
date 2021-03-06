import media
import fresh_tomatoes

"""
Create six new Movie instance, store a list with them and execute the
open_movies_page method.
"""

forma_dagua = media.Movie("Forma da Água",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcSsVWxdL"
                          "jAFyWj0YtR6cHiB8qfNl96yfC5O5QHw8Y4Cupp4fK_5",
                          "https://www.youtube.com/watch?v=XFYWazblaUA")

pantera = media.Movie("Pantera Negra",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcQarmjVytz3I"
                      "SRKJNwmxG7o-r4sWWN5VxbPp9qJauK4VvGrKu36",
                      "https://www.youtube.com/watch?v=iSwppsDP7jM")

touro_ferdinando = media.Movie("O Touro Ferdinando",
                               "http://t2.gstatic.com/images?q=tbn:ANd9GcTtJPK"
                               "7Q2req8Mrqu7GrWebnmzwRp35uaCBX0V5TpPYwrykaeK-",
                               "https://www.youtube.com/watch?v=HBXVM7oUPVk")

doze_herois = media.Movie("12 Heróis",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcTMHHfVq"
                          "P4f0DnfNMe0XijrqtJumLiQH9zyhSh7fe-UOi0Lk5KK",
                          "https://www.youtube.com/watch?v=-Denciie5oA&t=3s")

ope_red_sparrow = media.Movie("Operação Red Sparrow",
                              "http://t1.gstatic.com/images?q=tbn:ANd9GcR7tD9"
                              "CdW1vvXginNUbZx4kLyu4c5VKYASz9KMQ6hS8e8Mn30jf",
                              "https://www.youtube.com/watch?v=dh-OYpLaNtM")

viva = media.Movie("Viva - A Vida é uma Festa",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcQLlC1BU-d_49KZv"
                   "ZrLQ6vhp_dsWObCyp9a7UuJe0-8tpQcJ3fM",
                   "https://www.youtube.com/watch?v=zNCz4mQzfEI")

# Objects to populate the site with data.
movies = [forma_dagua, pantera,
          touro_ferdinando,
          doze_herois,
          ope_red_sparrow,
          viva]

# Call open_movies_page method of fresh_tomatoes.py and recieve movies list.
fresh_tomatoes.open_movies_page(movies)
