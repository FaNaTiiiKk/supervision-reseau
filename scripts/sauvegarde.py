import shutil
import os
from datetime import datetime

def effectuer_sauvegarde():
    # Définition des chemins
    sources = ['Configurations/switch-cisco.txt', 'Configurations/firewall.txt']
    destination_dir = 'sauvegardes/'
    
    # Création du dossier de destination s'il n'existe pas
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        
    # Obtention de la date du jour pour le nom du fichier
    date_jour = datetime.now().strftime("%Y-%m-%d")
    
    for source in sources:
        if os.path.exists(source):
            # Construction du nom de fichier : nom_date.txt
            nom_base = os.path.basename(source).replace('.txt', '')
            dest_path = f"{destination_dir}{nom_base}_{date_jour}.txt"
            
            # Copie du fichier
            shutil.copy2(source, dest_path)
            print(f"Confirmation : {source} a été sauvegardé sous {dest_path}")
        else:
            print(f"Erreur : Le fichier source {source} n'existe pas.")

if __name__ == "__main__":
    effectuer_sauvegarde()