# Importation des modules nécessaires
import logging  # Module pour la gestion des logs
import os       # Module pour les opérations système comme le chemin des dossiers/fichiers
from datetime import datetime  # Module pour obtenir la date et l'heure actuelles

# Définir le nom du fichier de log en utilisant la date et l'heure actuelles pour éviter les conflits de noms
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Définir le chemin complet du répertoire où les logs seront stockés
# os.getcwd() obtient le répertoire de travail actuel
# "logs" est le nom du sous-répertoire où les logs seront stockés
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Créer le répertoire de logs si celui-ci n'existe pas
# exist_ok=True signifie qu'aucune erreur ne sera levée si le répertoire existe déjà
os.makedirs(logs_path, exist_ok=True)

# Définir le chemin complet du fichier de log en combinant le chemin du répertoire des logs et le nom du fichier de log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configurer le module de logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Définir le fichier de sortie des logs
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Définir le format des messages de log
    level=logging.INFO,  # Définir le niveau de log (INFO dans ce cas)
)