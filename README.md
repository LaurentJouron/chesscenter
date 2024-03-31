<h1 align="center">Bienvenue sur le readme de Centre échecs 👋</h1>
<p align="center">
  <a href="https://twitter.com/LaurentJouron">
    <img alt="Twitter: LaurentJouron" 
      src="https://img.shields.io/twitter/follow/LaurentJouron.svg?style=social" target="_blank" />
  </a>
  <a href="https://github.com/LaurentJouron">
    <img alt="GitHub followers" 
      src="https://img.shields.io/github/followers/LaurentJouron?style=social" />
  </a>
</p>

___________

    Cet exercice a été réalisé dans le cadre d'une formation dont voici le sujet:
___

<h1 align="center">Centre échecs</h1>

<p align="center">
    <img align="right"
      width="200px" 
      src="https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png" />
</p>

* Vous allez créer des classes qui vous serviront de modèles pour le tournoi, les joueurs, les matchs et les rondes.
* Vous écrirez des contrôleurs pour accepter les données de l'utilisateur, produire les résultats des matchs, lancer de nouveaux tournois, etc...
* En plus de cela, il y aura des vues pour afficher les classements, les appariements et d'autres statistiques.

Comme ils savent qu'il s'agit de votre premier projet client, ils veulent avoir l'assurance que votre code sera propre et maintenable. En tant que passionné de Python, vous savez immédiatement qu'ils veulent vous voir suivre les directives de style de code – la PEP 8 en particulier.

___________

<h1 align="center">Installation de l'application </h1>

Pour installer les dépendances du projet, nous utilisons l'outil pipenv que vous devez avoir pré-installé sur votre ordinateur.
  <a href="https://github.com/pypa/pipx" title="Visuable Studio Code" target="_blank">Documentation pypa/pipx</a>

  * ``pip install pipx``
  * ``pipx ensurepath``
  * ``pipx install pipenv``

Pour commencer il faut cloner le projet grâce à l'url suivante :
  * ``git clone https://github.com/LaurentJouron/chesscenter.git``

Il faut se déplacer dans le dossier:
  * ``cd chesscenter``

Voici la procédure pour afficher la page d'accueil du site:

Créer un répertoire avec le nom .venv
  * ``mkdir .venv``

Installer les bibliothèques nécessaires avec
  * ``pipenv install``

Activer l'environnement de travail (environnement virtuel) avec
  * ``pipenv shell``

Pour lancer l'application depuis le terminal
  * ``python -m chesscenter``

___

<h1 align="center">Générer de données</h1>

Certaines fonctions - comme la revue des joueurs et les tournois - ne sont vraiment utiles qu’après avoir généré une base de données.

En plus du programme, un ensemble de données (joueurs, matchs, tours) a été ajouté pour générer des tournois de façon aléatoire.

Pour générer un tournoi, lancer le fichier ``tournament_random.py`` à partir d'un terminal, dans le dossier de niveau supérieur du projet :
  * ``python random_tournament.py``

Le script va générer un ensemble de 50 joueurs et 10 tournois aléatoires.


___

<h1 align="center">Base de données des joueurs</h1>

Cette option donne accès à la base de données de tous les joueurs.

Les actions suivantes sont possibles :

  - Voir tous les joueurs de la base de données et les trier par classement ou par nom.

  - Changer le classement des joueurs.

  - Ajouter un nouveau joueur.

___________

<h1 align="center">Base de données des tournois</h1>

Cette option donne accès à la base de données de tous les tournois.

Les actions suivantes sont possibles :

  - Voir tous les tournois de la base de données, ainsi que les détails de tout tournoi.

  - Voir les joueurs du tournoi : Recherchez un tournoi par nom, lieu ou année, et triez ses joueurs par classement ou par nom de famille.

___________

<h1 align="center">Générer un rapport flake8-html</h1>

flake8-html est un plugin de flake8 qui génère des rapports HTML de violations de flake8.

flake8 est un outil de linting pour Python qui vérifie le code source afin de détecter les erreurs de syntaxe, les violations de style et les problèmes de formatage conformément aux directives de la PEP8. Il combine plusieurs outils populaires tels que PyFlakes, pycodestyle (anciennement pep8), et McCabe pour fournir une vérification complète du code.

Installation de flake8
  * ``pipenv install flake8``


Installation du plugin flake8-html:
  * ``pip install flake8-html``

Exécuter flake8 à partir du dossier top_level du programme:

  * ``flake8 --format=html --htmldir=flake-report``

Ouvrez le fichier flake-report et lancez le fichier index.html dans un navigateur pour voir le resultat.

___________

<h1 align="center">Auteur et collaborateurs</h1>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LaurentJouron">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlW-w7O7g3hQTw8qcIAy3LCRhiHg5tUPfvVg&usqp=CAU"
          width="100px;"/><br />
        <sub><b>Laurent Jouron</b></sub></a><br />
      <a href="https://openclassrooms.com/fr/" title="Étudiant">🈸</a>
      <a href="https://github.com/LaurentJouron/Books-online" title="Codeur de l'application">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/thierhost">
        <img src="https://avatars.githubusercontent.com/u/7854284?s=100&v=4"
          width="100px;"/><br />
        <sub><b>Thierno Thiam</b></sub></a><br />
      <a href="https://github.com/thierhost" title="Mentor de Laurent">👨‍🏫</a> 
      <a href="https://www.python.org/dev/peps/pep-0008/" title="Doc PEP 8">📄</a>
    </td>
  </tr>
</table>
