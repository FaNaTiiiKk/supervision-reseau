import socket

def scan_ports():
    # 1. Demander à l'utilisateur une adresse IP ou un nom de serveur
    cible = input("Entrez l'adresse IP ou le nom du serveur à scanner : ")
    
    # 2. Liste des ports à tester
    ports_a_tester = [22, 80, 443, 3306]
    
    print(f"\nDébut du scan sur la cible : {cible}")
    print("-" * 40)
    
    # Boucle pour tester chaque port
    for port in ports_a_tester:
        # Création d'un objet socket
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # On définit un timeout (ex: 2 secondes) pour ne pas attendre indéfiniment si le port est fermé
        s.settimeout(2.0)
        
        # 3. Tentative de connexion au port
        resultat = s.connect_ex((cible, port))
        
        # connect_ex renvoie 0 si la connexion a réussi
        if resultat == 0:
            print(f"Port {port} : ouvert")
        else:
            print(f"Port {port} : fermé")
            
        # Fermeture de la connexion socket pour libérer les ressources
        s.close()

    print("-" * 40)
    print("Scan terminé.")

# Exécution du script en local
if __name__ == "__main__":
    scan_ports()
