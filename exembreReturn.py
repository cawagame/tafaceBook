def DonneNombrePaire(nb=None):
     if nb ==None:return "Variable vide"
     if type(nb)!=type(0):return "variable no int "
     if str(nb/2).count("."):return "Impaire"
     else:return "GAGANER"



print (DonneNombrePaire())  #vide
print (DonneNombrePaire("ee"))#string
print (DonneNombrePaire(1.2))  #float
print (DonneNombrePaire(3))  #impaire
print (DonneNombrePaire(4))  #paire
