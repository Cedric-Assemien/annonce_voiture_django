CEDRIC ANNONCES (Annonce de voiture)
Vous cherchez à acheter ou vendre une voiture ? Vous êtes au bon endroit ! Notre site vous propose une sélection d’annonces de voitures d’occasion, soigneusement vérifiées par nos experts. Parcourez nos annonces, trouvez la voiture de vos rêves et entrez en contact avec les vendeurs en toute simplicité.
Voici une description détaillée des fonctionnalités de notre site d’annonces de voitures :
1.	Inscription et Connexion :
o	Les utilisateurs peuvent s’inscrire sur Cédric annonce  en créant un compte personnel. Ils fourniront des informations telles que leur nom, leur adresse e-mail et un mot de passe.
o	Une fois inscrits, les utilisateurs pourront se connecter à leur compte en utilisant leurs identifiants.
o	La connexion permettra aux utilisateurs d’accéder à des fonctionnalités spécifiques, telles que la soumission d’annonces et la consultation des annonces existantes.
2.	Consultation des Annonces :
o	Les utilisateurs peuvent parcourir les annonces disponibles sur le site. Ils auront accès à des informations détaillées sur les voitures, telles que la marque, le modèle, l’année, le kilométrage, le prix et des photos.
o	La recherche peut être filtrée par critères tels que la marque, le modèle, le prix, etc.
3.	Contact avec les Vendeurs :
o	Lorsqu’un utilisateur est intéressé par une annonce, il peut contacter le vendeur directement via le site. Un formulaire de contact permettra d’envoyer un message au vendeur.
o	Le vendeur recevra une notification via le site pour lui indiquer qu’un acheteur potentiel souhaite entrer en contact.
4.	Publication des Annonces par l’Administrateur :
o	Seuls les administrateurs du site seront autorisés à publier des annonces. Cela garantit que seules les annonces légitimes et de qualité seront affichées.
o	Les administrateurs vérifieront les détails de chaque annonce avant de la rendre publique.
Objectif du Site : Cédric annonce vise à offrir une plateforme conviviale pour les acheteurs potentiels qui souhaitent trouver leur prochaine voiture. Cédric annonce a aussi pour objectif de faciliter la vente et l’achat de voitures d’occasion entre particuliers de manière sécurisée et professionnelle. En mettant l’accent sur la qualité des annonces et la sécurité des transactions, nous créons ainsi un espace de confiance pour les passionnés d’automobiles.



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
