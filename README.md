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

___________

* Page d'accueil
  * 1 - Player
    * 1 - Create
      * ``player_code``
      * ``first_name``
      * ``last_name``
      * ``birthday``
      * ``gender``
      * ``rank``


  * 2 - Tournament
    * 1 - Create
      * ``name``
      * ``place``
      * ``nbr_round``
      * ``start_date``
      * ``end_date``
      * ``current_round``
      * ``comment``

  * 3 - Match

  * 4 - Round
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
