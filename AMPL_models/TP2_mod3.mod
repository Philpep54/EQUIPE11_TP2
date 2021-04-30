# Technique de r�solution 3
# Sc�nario o� nous conservons les dimmensions de l'usine actuelle et o� nous p�nalisons les d�placements

#************Ensembles*******************************
set K;  # Ensemble des d�partements

#************Param�tres*******************************

param c {K, K}; # Co�t du d�placement de i � j
param n ; # Nombre de d�partements
param m ; # Nombre maximal de rang�es
param d ; # Largeur des rang�es 
param lon {K}; # Longueur du d�partement k
param L; # Somme des longueurs de tous les d�partements
param Lon_u; #longeur max de l'usines
param Lar_u; #largeur max de l'usines
param Xa {K}; # Position horizontale actuelle du d�partement k
param Ya {K}; # Position verticale actuelle du d�partement k
param cd; # Co�t du d�m�nagement d'un d�partement de sa position actuelle � sa nouvelle position


#************Variable*********************************
var X {K} integer; #Position horizontale du d�partement k
var Y {K} integer; # Position verticale du d�partement k
var Aij {K, K}binary; # Position relative; =1 si i est dans la m�me rang�e � la gauche de j, 0 sinon
var Bij {K, K}binary; # Position relative; =1 si i et j ne sont pas dans la m�me rang�e et que i est en dessous de j, 0 sinon
var dx {K, K}; # Distance horizontale entre i et j
var dy {K, K}; # Distance verticale entre i et j
var ddx {K}; # Distance de d�m�nagement horizontale
var ddy {K}; # Distance de d�m�nagement verticale 

#************Fonction objectif************************
minimize Z: sum {i in K,j in K: 1<= i < j <= n}	((c[i, j] * (dx[i, j]+dy[i, j]))) + sum {k in K}(cd*(ddx[k]+ddy[k]));


#************Contraintes******************************
subject to dist_horizontal {i in K, j in K: 1<= i < j <= n}: 
	dx[i,j]>= X[i]-X[j]; #�tablissement distance horizontale entre les d�partements subject to dist_horizontal_2 {i in I, j in J}: dx[i,j]>= Xj[j]-Xi]i];
subject to dist_horizontal_2 {i in K,j in K: 1<= i < j <= n}: 
	dx[i,j]>= X[j]-X[i];

subject to demenagement_horizontal {k in K}: 
	ddx[k]>= Xa[k]-X[k]; #�tablissement distance horizontale entre les d�partements subject to dist_horizontal_2 {i in I, j in J}: dx[i,j]>= Xj[j]-Xi]i];
subject to demenagement_horizontal_2 {k in K}: 
	ddx[k]>= X[k]-Xa[k];
	
subject to demenagement_verticale {k in K}: 
	ddy[k]>= Ya[k]-Y[k]; #�tablissement distance verticales entre les d�partements
subject to demenagement_verticale_2 {k in K}: 
	ddy[k]>= Y[k]-Ya[k];

subject to dist_verticale {i in K, j in K: 1<= i < j <= n}: 
	dy[i,j]>= Y[i]-Y[j]; #�tablissement distance verticales entre les d�partements
subject to dist_verticale_2 {i in K, j in K: 1<= i < j <= n}: 
	dy[i,j]>= Y[j]-Y[i];

subject to dep_overlap {i in K, j in K: 1<= i < j <= n}: 
	X[j]-X[i]>= (0.5*(lon[i]+lon[j]))-(L*(1-Aij[i,j])); #Emp�che les d�partements d'�tre l'un sur l'autre
subject to dep_overlap_2 {i in K, j in K: 1<= i < j <= n}: 
	X[i]-X[j]>= (0.5*(lon[i]+lon[j]))-(L*(1-Aij[j,i])); #Emp�che les d�partements d'�tre l'un sur l'autre

subject to row_overlap {i in K, j in K: 1<= i < j <= n}: 
	Y[j]-Y[i]>= d-(m*d*(1-Bij[i,j])); #Emp�che les rang�es d'�tre l'une sur l'autres
subject to row_overlap_2 {i in K, j in K: 1<= i < j <= n}: 
	Y[i]-Y[j]>= d-(m*d*(1-Bij[j,i])); #Emp�che les rang�es d'�tre l'une sur l'autres

subject to coherence {i in K, j in K: 1<= i < j <= n}: 
	Y[i]-Y[j]<= (1-Aij[i,j]-Aij[j,i])*(m-1)*d; #Contrainte pour que yi=yj lorsqu'ils sont sur la m�me rang�e
subject to coherence_2 {i in K, j in K: 1<= i < j <= n}: 
	Y[j]-Y[i]<= (1-Aij[i,j]-Aij[j,i])*(m-1)*d; #

subject to min_rang�es {i in K: 1<= i <= n}: 
	Y[i]>=0;#Contraintes de bases pour yi
subject to max_rang�es {i in K: 1<= i <= n}: 
	Y[i]<=d*(m-1); #Limite le nombre de rang�es 

subject to min_xi {i in K: 1<= i <= n}: 
	X[i]>=(0.5*lon[i]); #Contraintes de bases pour xi
subject to max_xi {i in K: 1<= i <= n}: 
	X[i]<=L-(0.5*lon[i]); #Contraintes de bases pour xi

subject to equilibre {i in K,j in K: 1<= i < j <= n}: 
	Aij[i,j]+Aij[j,i]+Bij[i,j]+Bij[j,i]=1; #Contraintes d'�quilibre de base
subject to equilibre_2 {i in K,k in K, j in K: 1<= i < j <= n}: 
	Aij[i,j]+Aij[j,k]<=1+Aij[i,k]; #Contraintes triangulaire d'�quilibre
subject to equilibre_3 {i in K,k in K, j in K: 1<= i < j <= n}: 
	Bij[i,j]+Bij[j,k]<=1+Bij[i,k]; #Contraintes triangulaire d'�quilibre

subject to largeur_usine {i in K,j in K: 1<= i < j <= n}: dy[i,j] + 0.5*(Y[j]+Y[i])<=Lar_u;
subject to longueur_usine {i in K,j in K: 1<= i < j <= n}: dx[i,j] + 0.5*(X[j]+X[i])<=Lon_u;


subject to Aij_1 {i in K, j in K: 1 <= i and j <= n}: Aij[i,j]>=0;
subject to Bij_1 {i in K, j in K: 1 <= i and j <= n}: Bij[i,j]>=0;
	
