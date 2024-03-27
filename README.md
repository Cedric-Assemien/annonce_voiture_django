Voici un guide détaillé pour un utilisateur novice qui souhaite télécharger et exécuter mon projet Django d’annonces de voitures à partir de GitHub. Suivez ces étapes pas à pas :
1.	Téléchargement du Projet:
a)	Première méthode
Telecharger en Archive
o	Rendez-vous sur le référentiel GitHub du  projet (annonce_voiture_django).
o	Cliquez sur le bouton “Code” et sélectionnez “Download ZIP”.
o	Extrayez le fichier ZIP sur votre ordinateur.
b)	Deuxieme methode
Cloner le Projet:
o	Ouvrez votre terminal (ou invite de commande).
o	Naviguez vers le répertoire où vous souhaitez enregistrer le projet.
o	Exécutez la commande suivante pour cloner le projet depuis GitHub :
Git clone https://github.com/Cedric-Assemien/annonce_voiture_django.git
1.	Création de l’Environnement Virtuel:
o	Si vous n’avez pas déjà créé un environnement virtuel, faites-le maintenant :
o	python -m venv env
o	Activez l’environnement virtuel : 
	Sur Windows : env\Scripts\activate
	Sur macOS/Linux : source env/bin/activate
2.	Installation des Dépendances:
o	Ouvrez une invite de commande (Terminal ou CMD).
o	Accédez au répertoire du projet (où se trouve le fichier requirements.txt).
o	Exécutez la commande suivante pour installer les dépendances :
o	pip install -r requirements.txt
3.	La Base de Données:
Il existe un fichier « db.spilte3 » (la base  de donnée par default de Django)  C’est notre base de donnée où est stokée toute les données.
4.	Appliquer les Migrations:
o	Dans l’invite de commande, exécutez :
o	python .\manage.py makemigrations
o	python manage.py migrate
Ceci va appliquer les changements dans la base de donnée
5.	Création d’un Superutilisateur (Admin):
Pour créer un superutilisateur, exécutez :
o	python manage.py createsuperuser
o	Entrer votre nom utilisateur
o	Entrer votre email
o	Entrer votre mot de passe 

Le Super User ou utilisateur spécial a accès a toutes les autorisations, il peut créer, modifier ou supprimer n’importe quel élément dans la base de donnée.

6.	Lancement du Serveur de Développement:
o	Exécutez :
o	python manage.py runserver
o	Ouvrez votre navigateur et accédez à http://localhost:8000/ pour voir l’application web.
7.	Accès au site web
Vous avez maintenant accès a l’interface du site web. Vous pouvez vous inscrit, vous connecter parcourir les annonces disponibles du site sur l’interface du Dashboard vous avez un bouton créer une annonce. Si vous voulez vous pouvez renseignez les informations requis pour soumettre une annonce.
8.	Accès a l’interface admin
Pour accéder aux privilèges de admin, vous devez ajouter « admin » a la fin de l’url. Ex : accédez à http://localhost:8000/admin
Vous verrez une page de connexion vous entrez le nom d’utilisateur et le mot de passe que vous avez renseigné lors de la création du super utilisateur. Ainsi vous avez accès a toutes les données du site : les annonces, utilisateurs, les contacts etc.
J’espère vraiment que vous aurez aucune difficulté l’ors du lancement, avec toutes les étapes en détaille que je vous ai fournie. 
Merci d’avoir télécharger mon application annonce_voiture_django j’espère que vous apprécieriez.   
