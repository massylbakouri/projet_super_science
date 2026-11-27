import numpy as np
import numpy.random as npr
from abc import ABC, abstractmethod

monuments={"Gare":4,
           "Centre Commercial":10,
           "Parc d'attractions":16,
           "Tour Radio":22}

etablissements={"Champ de blé":[[1],1,"b"],
                "Ferme":[[2],2,"b"],
                "Boulangerie":[[2,3],2,"v"],
                "Cafe":[[3],2,"r"],
                "Superete":[[4],2,"v"],
                "Foret":[[5],3,"b"],
                "Fomagerie":[[7],5,"v"],
                "Fabrique de meuble":[[8],3,"v"],
                "Mine":[[9],6,"b"],
                "Restaurant":[[9,10],3,"r"],
                "Verger":[[10],3,"b"],
                "Marche de fruits et legumes":[[11,12],2,"v"],
                "Centre d'affaires":[[6],8,"p"],
                "Stade":[[6],6,"p"],
                "Chaine de television":[[6],7,"p"]
                }


    

class carte(ABC):
    def __init__(self,nom:str):
        self._nom=nom

    @abstractmethod
    def effet(self):
        pass

class monument:
    def __init__(self,nom:str):
        super().__init__(nom)
        self._cout = monuments[self._nom]

    def effet(self,joueur):
        if self._nom=="Gare":
            lancer_2_des = input("voulez_vous lancer 2 dés ? (0 pour non ,1 pour oui)")
            joueur.lancer_de(lancer_2_des)
            
        elif self._nom=="Centre Commercial":
            for i in joueur._etablissements:
                if etablissements[i][2] == "r" or etablissements[i][2] == "v":
                    joueur.recevoir_pieces(1)

        elif self.nom=="Parc d'attractions":
            if joueur._de1 == joueur._de2:


        else:


class etablissement:
    def __init__(self,nom:str):
        super().__init__(nom)
        self.numero = etablissements[self._nom][0]
        self._cout = etablissements[self._nom][1]
        self._type = etablissements[self._nom][2]


class reserve:
    def __init__(self):
        self._etablissement_dispo={"Champ de blé":6,
                "Ferme":6,
                "Boulangerie":6,
                "Cafe":6,
                "Superete":6,
                "Foret":6,
                "Fomagerie":6,
                "Fabrique de meuble":6,
                "Mine":6,
                "Restaurant":6,
                "Verger":6,
                "Marche de fruits et legumes":6,
                "Centre d'affaires":4,
                "Stade":4,
                "Chaine de television":4
                }

    def est_disponible(self,nom_etablissement):
        if self._etablissement_dispo[nom_etablissement] > 0 : return True
        else : return False

    def retirer(self,nom_etablissement):
        if self.est_disponible(nom_etablissement):
            self._etablissement_dispo[nom_etablissement] -= 1
        else:
            raise ValueError("la carte n'est pas disponible")


       
