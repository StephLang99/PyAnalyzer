# MGL Projet étude empirique

Ce projet consiste en une étude empirique sur la relation entre le nombre de contributeur et la qualité logicielle.

## Contexte

Le présent *README.md* est la méthode pour réaliser l'expérience. 

## Pré-requis

Pour l'outil *PyAnalyzer*
- [ ] [Installer *Python* 3.9, v64bits](https://www.python.org/downloads/)
- [ ] [Installer *Pycharm* 2020.2.3](https://www.jetbrains.com/pycharm/download/?_ga=2.97838684.232200316.1585182235-1278111478.1582600558#section=windows)
- [ ] [Installer *Git* 2.29.0](https://git-scm.com/downloads)
- [ ] [Créer un compte sur *github*](https://github.com/)

Pour Sonarqube
- [ ] [Installer *Java, JDK* 11.0.4](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html)
- [ ] [Installer *SonarQube* 8.4.2.36762](https://www.sonarqube.org/downloads/)
- [ ] [Installer *Sonar-scanner* 4.4.0.2170](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)
- [ ] [Installer *DbVisualizer* 11.0.5](https://www.dbvis.com/)

Autres outils 

- [ ] [Installer *TortoiseGit* 2.11.0](https://tortoisegit.org/)
- [ ] [Installer *Typora* 0.9.96](https://typora.io/) 

 ## Installation de l'outil *PyAnalyzer*

Cloner le référentiel *PyAnalyzer*

- [ ] Au besoin, modifier votre variable d'environnement *Path* pour utiliser *Git*
- [ ] Ouvrir la console de commande 
- [ ] Utiliser *git* clone pour cloner le référentiel sur *Github*

```console
git clone https://github.com/StephLang99/PyAnalyzer.git PyAnalyzer
```

Ouvrir le projet *PyAnalyzer* 
- [ ] Ouvrir dans *Pycharm* le référentiel *PyAnalyzer*
- [ ] Ouvrir le programme *mainProjet.py* 

Installer les librairies (si non présente)
- [ ] Utiliser *[pip](https://pip.pypa.io/en/stable/)* pour installer les librairies

```bash
pip3 install PyGithub
pip3 install GitPython
```
## *Installation pour la partie SonarQube*

Pour débuter avec *SonarQube*
- [ ] Modifier votre variable d'environnement *Path* pour utiliser *Java JDK* 11
- [ ] Modifier votre variable d'environnement *Path* pour utiliser *Sonar-scanner*
- [ ] Démarrer *SonarQube*
- [ ] Valider le chemin http://localhost:9000/, le port par défaut est 9000

## Paramétrage de *PyAnalyzer*

Pour débuter la paramétrisation de *PyAnalyzer* 

- [ ] Ouvrir le programme *mainProjet.py*, la section *main*

- [ ] Modifier le paramètre pour la taille de l'échantillonnage 


```python
# Sample Size
max_size_project = 3
```
- [ ] Modifier les paramètres pour la recherche sur *Github*
```python
# kotlin or python
language_project = "python"

# sort by stars, forks, updated
sort_by = 'stars'

# desc or asc
sort_type = 'desc'
```
- [ ] Modifier les paramètres pour télécharger les référentiels et l'exécution de *SonarQube* 

Veuillez noter que le module qui permet de faire la compilation est désactiver par défaut. (voir le chapitre 6 dans la section future travaux)
```python
# Configuration
download_repository = True
execute_sonarqube = True

# future usage
execute_compiler = False
```
- [ ] Modifier le répertoire de travail où les référentiels seront téléchargés
```python
 # Other configuration
 work_dir = "C:\\workdir\\"
```
- [ ] Modifier le [token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) pour l'accès à *Github*
```python
# your github token
token = 'your token'
gh = Github(token)
```


## Exécution de l'outil *PyAnalyzer*

Pour exécution de *PyAnalyzer*

- [ ] Exécuter le programme *mainProjet.py* dans *Pycharm* 

La console affichera les informations pertinentes lors de l'exécution
``` python
You have 30/30 API calls remaining
Query = language:python
1 / 3 : https://github.com/donnemartin/system-design-primer.git ; system-design-primer ; Python ; 11160 ; True ; 98; 2; 315 ; 0
Download = 0 ; Compiler = 0 ; Sonar = 0
2 / 3 : https://github.com/public-apis/public-apis.git ; public-apis ; Python ; 2730 ; True ; 429; 2; 2215 ; 0
Download = 0 ; Compiler = 0 ; Sonar = 0
3 / 3 : https://github.com/jackfrued/Python-100-Days.git ; Python-100-Days ; Python ; 265473 ; True ; 12; 1; 323 ; 0
Download = 0 ; Compiler = 0 ; Sonar = 0

Process finished with exit code 0
```

La console affiche les éléments suivants:

- Le nombre de référentiels téléchargés sur la taille de l'échantillon;
- Le référentiel téléchargé;
- Le nom du référentiel;
- Le langage de programmation du référentiel;
- La taille du référentiels;
- Utilisation de *Gradle* dans le référentiel (future utilisation);
- Le nombre de collaborateurs;
- Le nombre de branches actives; 
- Le nombre de soumissions de code;
- Le nombre de publication de code;
- Indicateur si le référentiel a été téléchargé 
  - 0 = le référentiel n'a pas téléchargé;
  - 1 = le référentiel a été téléchargé avec succès;
  - -1 = le référentiel a été téléchargé avec une erreur;
- Indicateur si le référentiel a été compilé (future utilisation) 
    - 0 = le référentiel a été compilé avec succès;
    - 1 = le référentiel a eu une erreur lors de la compilation;
- Indicateur si le référentiel a été analysé avec *SonarQube*
    - 0 = le référentiel a été analysé avec succès;
    - 1 = le référentiel a eu une erreur lors de l'analyse.



Des référentiels peuvent ne pas être téléchargés pour les raisons suivantes: 

- la taille du référentiel est trop volumineuse;

- le référentiel a un langage de programmation qui n'est pas reconnu.

  

Plusieurs fichiers sera crées lors l'exécution. 

- [ ] Valider résultat de l'exécution dans votre répertoire de travail où les référentiels sont téléchargés
  
  - *log_repo.csv* contient les mesures relié au référentiel 
    - Le référentiel téléchargé;
    - Le nom du référentiel;
    - Le langage de programmation du référentiel;
    - Le nombre de collaborateurs;
    - Le nombre de branches actives; 
    - Le nombre de soumissions de code;
    - Le nombre de publication de code;
    - Indicateur de téléchargement du référentiel
    - Indicateur de compilation du référentiel
    - Indicateur de l'analyse du référentiel
  
```text
https://github.com/donnemartin/system-design-primer.git;system-design-primer;Python;98;2;315;0;0;0;0
https://github.com/public-apis/public-apis.git;public-apis;Python;429;2;2215;0;0;0;0
https://github.com/jackfrued/Python-100-Days.git;Python-100-Days;Python;12;1;323;0;0;0;0
```

- [ ] Valider résultat de l'exécution les répertoire des chaque référentiels

  - *sonar.bat* contient la ligne de commande pour que le programme python invoque l'analyse 
  
```shell script
call sonar-scanner
```

  - *out_sonar.txt* contient le journal d'exécution de l'analyse de *SonarQube*
  - *sonar_done.txt* indique si l'analyse du référentiel s'est effectué avec succès.
  - *sonar-project.properties*  contient les informations nécessaire pour analysé le référentiel avec *SonarQube*
      - *sonar.projectKey* est le nom du référentiel 
      - *sonar.scm.provider* utilise quel gestionnaire de source
      - *sonar.java.binairies* est emplacement des binaires
      - *sonar.projectVersion* est la version du référentiel
```shell script
sonar-project.properties
sonar.projectKey=zulip
sonar.scm.provider=git
sonar.java.binaries=.
sonar.projectVersion=371
```

## Extraction mesure *SonarQube*

Pour extraire les mesures de *SonarQube*

- [ ] Configurer la connexion à la base de données *H2*  (jdbc:h2:tcp://127.0.0.1:9092/sonar)
- [ ] Ouvrir dans une fenêtre SQL, et exécuté le script "tools\script_extract.sql*"

La requête SQL extrait les informations pertinentes de la dernière analyse du référentiel effectuée
- le nom du référentiel 
- le nom de la mesure
- la valeur de la mesure
- le domaine de la mesure
- le type de mesure

```sql
select a.name, c.short_name, b.value, c.domain, c.val_type from projects a
inner join project_measures b on a.uuid = b.component_uuid
inner join snapshots d on  b.analysis_uuid = d.uuid 
inner join metrics c on c.uuid = b.metric_uuid
where d.islast = true
```

- [ ] Exporter les données en format csv

## Analyse des données

Analyse les données avec l'outil de votre choix (ex. *Excel*)

## Version

Version 2.0 de l'outil *PyAnalyzer*.
- Ajout du *README.md*

## Licence

Auteur : Stéphane Langlois

Logiciel libre