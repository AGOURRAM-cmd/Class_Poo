class GestionCptb:
    def __init__(self,nCompte,nomClient,soldCompte):
        self.__nCompte = nCompte
        self.__nomClient = nomClient
        self.__soldCompte = soldCompte
    
    #Getters
    def get_nCompte(self):
        return self.__nCompte
    
    def get_nomClient(self):
        return self.__nomClient
    
    def get_soldCompte(self):
        return self.__soldCompte
    
    #Setters
    def set_nCompte(self,nCompte):
        if self.__nCompte == 0 or self.__nCompte < 0:
            raise ValueError("Le numero compte ne doit pas null ou negative ")    
        else:
            self.__nCompte = nCompte

    def set_nomClient(self,nomClient):
        self.__nomClient = nomClient

    def set_soldClient(self,soldClient):
        self.__soldCompte = soldClient

    #Methode de versement
    def versement(self,montant):
        if montant != 0 or montant > 0 :
            self.__soldCompte += montant
        else:
            print("Sold doit etre positive svp!")
    
    #Methode de retrait
    def retrait(self,montant):
        if montant <=0 : 
            print("Le montant doit etre positif et not null")
        elif montant < self.__soldCompte :
            print("Le solde est insuffisanr")
        else:
            self.__soldCompte -= montant

    #methode affichage les info 
    def affichage_info(self):
        print("Nom client : ",self.__nomClient,"\nNumero compte : ",self.__nCompte,"\nSold : ",self.__soldCompte)
