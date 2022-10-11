# Fonction ConvBinEnDec(bin) qui prend en paramètre une chaîne représentant le codage en binaire d'un nombre
# et qui calcule puis retourne le nombre correspondant en codage décimal

def ConvBinEnDec(bin):
    puissance_2 = len(bin)-1     # La puissance maximale de 2 (associée au bit de poids fort)
                                    # est égale à la longueur de la suite de bits - 1
    rang_bit = 0                        # On va commencer par traiter le bit de poids fort (1er caractère de la suite de bits)
    conversion_dec = 0                  # On initialise la conversion décimale à 0

    while puissance_2 >= 0:           # On va traiter tous les bits de la chaîne, du poids fort vers le poids faible

        # On ajoute à la conversion décimale le bit examiné, que l'on multiplie par la puissance de 2 qui lui est associée
        conversion_dec = conversion_dec + (int(bin[rang_bit]) * (2**puissance_2))

        # On passe au bit suivant
        rang_bit = rang_bit + 1

        # Le passage au bit suivant diminue la puissance de 2
        puissance_2 = puissance_2 - 1

    return conversion_dec

# Même fonction que la précédente mais dans une version récursive

def ConvBinEnDecRec(bin):
    if len(bin)==1:
        return int(bin[0])*2**0
    else:
        return int(bin[0])*2**(len(bin)-1) + ConvBinEnDecRec(bin[1:])
    

# Programme principal

nb_bin=input("Saisissez le nombre binaire à convertir en un nombre décimal :")

print(f"La conversion en décimal de {nb_bin} est {ConvBinEnDecRec(nb_bin)}.")

