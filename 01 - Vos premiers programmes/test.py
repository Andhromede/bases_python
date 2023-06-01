import turtle

# Ceci est un commentaire, les commentaires sont ignorés par l'ordinateur.
# Ils sont ici pour permettre aux développeur de garder leur code compréhensible 
# (pour eux même ou pour les autres)

turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)

# Début des instructions permettant de dessiner : insérer votre code ici !

turtle.begin_fill() # permet d'indiquer à la tortue que l'on souhaite remplir la forme dessinée.
turtle.forward(200) # Ici une instruction permettant d'avancer de 200px
turtle.circle(30) # Ici une instruction permettant de dessiner un cercle de rayon 30px
turtle.end_fill() # permet d'indiquer à la tortue que nous n'avons plus besoin de remplir les nouvelles formes
turtle.circle(90)

# fin des instruction permettant de dessiner.

turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin