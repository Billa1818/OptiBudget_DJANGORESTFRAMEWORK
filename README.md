# 🧮 OptiBudget / SmartBudget - Backend

## 🚀 Présentation

OptiBudget (aussi appelé SmartBudget) est une API backend complète pour la gestion de budgets personnels et d'entreprise, développée avec Django et Django REST Framework. Elle inclut :  
- Authentification sécurisée (JWT, gestion des appareils, sécurité avancée)
- Gestion multi-comptes (particulier/entreprise)
- Budgets, dépenses, entrées, notifications, conseils IA, gestion des employés et salaires
- Tâches asynchrones avec Celery et Redis
- Documentation interactive via Swagger (drf-yasg)

## 🏗️ Structure du projet

- `accounts/` : Authentification, gestion des utilisateurs, sécurité, appareils
- `budgetManager/` : Budgets, dépenses, entrées, notifications, IA, employés, salaires
- `smartbudget_admin/` : Interface et endpoints d'administration
- `SmartBudget/` : Paramétrage principal Django, Celery, middlewares
- `tasks/` : Tâches asynchrones (emails, gestion de tokens)
- `testEndpoint/` : Clients de test automatisés pour l'API

## ⚙️ Installation

1. **Cloner le dépôt**
   ```bash
   git clone <url_du_repo>
   cd OptiBudget-BACK-END
   ```

2. **Créer et activer un environnement virtuel**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement**  
   Crée un fichier `.env` à la racine avec :
   ```
   SECRET_KEY=...
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_ENGINE=django.db.backends.sqlite3
   DB_NAME=db.sqlite3
   EMAIL_HOST=...
   EMAIL_PORT=...
   EMAIL_HOST_USER=...
   EMAIL_HOST_PASSWORD=...
   DEFAULT_FROM_EMAIL=SmartBudget@site.com
   FRONTEND_URL=http://localhost:3000
   CELERY_BROKER_URL=redis://localhost:6379/0
   GEMINI_API_KEY=...
   ```

5. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

6. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

7. **Lancer le serveur**
   ```bash
   python manage.py runserver
   ```

8. **Lancer le worker Celery**
   ```bash
   celery -A SmartBudget worker -l info
   ```

## 🧪 Tests

Des clients de test sont disponibles dans `testEndpoint/`.  
Voir le fichier `testEndpoint/README.md` pour les instructions détaillées.

## 📚 Documentation API

- Swagger : `/swagger/`
- Redoc : `/redoc/`

## 🔒 Authentification & Sécurité

- Authentification JWT (avec blacklist, rotation, gestion avancée)
- Gestion des appareils et des sessions
- Sécurité renforcée (verrouillage, traçage, vérification email)
- Permissions avancées selon le type de compte

## 📊 Fonctionnalités principales

- Budgets, catégories, dépenses, entrées
- Notifications, conseils IA (intégration Gemini)
- Gestion des employés et salaires (pour entreprises)
- Exports CSV/JSON, rapports, statistiques détaillées
- Tâches asynchrones (emails, gestion de tokens, etc.)

## 🛠️ Technologies principales

- Python 3.12+
- Django 5.2
- Django REST Framework
- Celery & Redis
- drf-yasg (Swagger)
- Python Decouple (gestion .env)
- Google Gemini API (conseils IA)

## 📁 Exemples d'endpoints

Voir les fichiers `accounts/README.md` et `budgetManager/README.md` pour le détail des endpoints et modèles.

## 📝 Notes

- Le projet est prêt pour le déploiement (voir checklist Django)
- Les middlewares personnalisés ajoutent des couches de sécurité et de traçabilité
- Les tâches asynchrones nécessitent un broker Redis opérationnel


## Support

Pour toute question ou problème, veuillez   me  contacter mail billaassouma@188gmail.com ou +229 53400160.
# OptiBudget_BACKEND


