# Résa

Réservation de salle de réunion.

## Acquisition

Vous pouvez obtenir une copie de ce programme en clonant ce dépôt.

## Utilisation

L'objectif de ce programme est de réserver une salle de réunion en fonction du nombre de participants. Pour réserver une salle de réunion pour `<N>` participants, placez-vous à l'intérieur de votre clone local de ce dépôt et lancez :

- dans Invite de commandes / PowerShell sur Windows,
```bash
python.exe -m resa <N>
```
- dans Terminal sur Linux / macOS.
```bash
python3 -m resa <N>
```

Le programme repose sur le module `resa`. Son script principal dans `resa\__main__.py` lit le nombre de participants sur la ligne de commandes et appelle la fonction de réservation de salle `bookMeetingRoom` implémentée dans le fichier `resa\resa.py`. La classe `Room` définie dans ce même fichier représente les salles disponibles à la réservation.

## Tests

Le script `tests\unit_tests.py` implémente une suite de tests unitaires (grâce au module `unittest` de Python) du programme Résa. Vous pouvez lancer ces tests en exécutant :

- dans Invite de commandes / PowerShell sur Windows,
```bash
python.exe -m unittest tests/unit_tests.py
```
- dans Terminal sur Linux / macOS.
```bash
python3 -m unittest tests/unit_tests.py
```
