import media

forma_dagua = media.Movie("Forma d'água.",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcSsVWxdLjAFyWj0YtR6cHiB8qfNl96yfC5O5QHw8Y4Cupp4fK_5",
                          "https://www.youtube.com/watch?v=XFYWazblaUA")

pantera = media.Movie("Pantera Negra",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcQarmjVytz3ISRKJNwmxG7o-r4sWWN5VxbPp9qJauK4VvGrKu36",
                      "https://www.youtube.com/watch?v=iSwppsDP7jM")

passageiro = media.Movie("O Passageiro",
                         "http://t2.gstatic.com/images?q=tbn:ANd9GcQ-ezHDsAD1Fp2TZCi2P1McftxmH4gaosMFRQreN4M4IcdntsIw",
                         "https://www.youtube.com/watch?v=WWexI9YiLSc"
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


lista_filmes = [forma_dagua, pantera, passageiro, doze_herois, operacao_red_sparrow, viva]

for filme in lista_filmes:
    filme.show_trailer()

# print(forma.title)
# forma.show_trailer()
