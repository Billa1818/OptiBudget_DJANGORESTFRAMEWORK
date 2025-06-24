# Changelog - Renommage SmartBudget vers OptiBudget

## Résumé des modifications

Ce document décrit toutes les modifications effectuées lors du renommage de l'application SmartBudget vers OptiBudget.

## Modifications de structure

### Dossiers renommés
- `SmartBudget/` → `OptiBudget/`
- `smartbudget_admin/` → `optibudget_admin/`

## Modifications de fichiers

### Fichiers de configuration Django

#### `manage.py`
- Changé `'SmartBudget.settings'` → `'OptiBudget.settings'`

#### `OptiBudget/settings.py`
- Changé `'smartbudget_admin'` → `'optibudget_admin'` dans INSTALLED_APPS
- Changé `'SmartBudget.middleware'` → `'OptiBudget.middleware'` dans MIDDLEWARE
- Changé `'SmartBudget.urls'` → `'OptiBudget.urls'` dans ROOT_URLCONF
- Changé `'SmartBudget.wsgi.application'` → `'OptiBudget.wsgi.application'` dans WSGI_APPLICATION
- Changé `'SmartBudget@site.com'` → `'OptiBudget@site.com'` dans DEFAULT_FROM_EMAIL

#### `OptiBudget/urls.py`
- Changé `title="SmartBudget API"` → `title="OptiBudget API"`
- Changé toutes les références à "SmartBudget" → "OptiBudget" dans la documentation Swagger
- Changé `'SmartAdmin/'` → `'OptiAdmin/'` dans les URLs
- Changé `'smartbudget_admin.urls'` → `'optibudget_admin.urls'`

#### `OptiBudget/wsgi.py`
- Changé `"WSGI config for SmartBudget project"` → `"WSGI config for OptiBudget project"`
- Changé `'SmartBudget.settings'` → `'OptiBudget.settings'`

#### `OptiBudget/asgi.py`
- Changé `"ASGI config for SmartBudget project"` → `"ASGI config for OptiBudget project"`
- Changé `'SmartBudget.settings'` → `'OptiBudget.settings'`

#### `OptiBudget/celery.py`
- Changé `'SmartBudget.settings'` → `'OptiBudget.settings'`
- Changé `app = Celery('SmartBudget')` → `app = Celery('OptiBudget')`

#### `OptiBudget/middleware.py`
- Changé `from smartbudget_admin.models import ClientKey` → `from optibudget_admin.models import ClientKey`
- Changé toutes les références `'smartbudget_admin:'` → `'optibudget_admin:'` dans les URLs exemptées

### Application optibudget_admin

#### `optibudget_admin/apps.py`
- Changé `class SmartbudgetAdminConfig` → `class OptibudgetAdminConfig`
- Changé `name = 'smartbudget_admin'` → `name = 'optibudget_admin'`

#### `optibudget_admin/urls.py`
- Changé `app_name = 'smartbudget_admin'` → `app_name = 'optibudget_admin'`

### Application accounts

#### `accounts/views.py`
- Changé `from SmartBudget.settings import DEFAULT_FROM_EMAIL` → `from OptiBudget.settings import DEFAULT_FROM_EMAIL`
- Changé `from SmartBudget.swagger_config import JWT_SECURITY` → `from OptiBudget.swagger_config import JWT_SECURITY`
- Changé `'SmartBudget'` → `'OptiBudget'` dans les sujets d'emails

#### `accounts/utils.py`
- Changé `'SmartBudget Email System'` → `'OptiBudget Email System'`
- Changé `'SMARTBUDGET'` → `'OPTIBUDGET'` dans les sujets d'emails

### Application budgetManager

#### `budgetManager/views.py`
- Changé `from SmartBudget.swagger_config import JWT_SECURITY, common_responses` → `from OptiBudget.swagger_config import JWT_SECURITY, common_responses`

#### `budgetManager/reports.py`
- Changé `'SmartBudget'` → `'OptiBudget'` dans les en-têtes de rapports

### Templates

#### `templates/accounts/base.html`
- Changé `SmartBudget` → `OptiBudget` dans le titre et le logo

#### `templates/accounts/signup.html`
- Changé `SmartBudget` → `OptiBudget` dans les textes

#### `templates/accounts/login.html`
- Changé `SmartBudget` → `OptiBudget` dans le titre

#### `templates/emails/email_verification.html`
- Changé `SMARTBUDGET` → `OPTIBUDGET` dans tous les textes

### Documentation

#### `README.md`
- Changé `SmartBudget-BACK-END` → `OptiBudget-BACK-END`

#### `accounts/README.md`
- Changé `SMARTBUDGET` → `OPTIBUDGET` dans le titre et la description
- Changé `SMARTBUDGET@site.com` → `OPTIBUDGET@site.com`

#### `testEndpoint/README.md`
- Changé `SMARTBUDGET` → `OPTIBUDGET` dans le titre et la description
- Changé `SMARTBUDGET-TestClient/1.0` → `OPTIBUDGET-TestClient/1.0`

#### `testEndpoint/test_accounts_client.py`
- Changé `SmartbudgetAccountsClient` → `OptibudgetAccountsClient`
- Changé `SMARTBUDGET-TestClient/1.0` → `Optibudget-TestClient/1.0`

## URLs modifiées

- `/SmartAdmin/` → `/OptiAdmin/`

## Vérifications effectuées

- ✅ `python manage.py check` - Aucune erreur détectée
- ✅ Structure des dossiers mise à jour
- ✅ Tous les imports et références mis à jour
- ✅ Configuration Django fonctionnelle

## Notes importantes

1. **Base de données** : Aucune migration de base de données n'était nécessaire car seuls les noms d'applications ont été modifiés, pas la structure des modèles.

2. **Environnement virtuel** : L'environnement virtuel reste inchangé.

3. **Fichiers de configuration** : Les fichiers `.env` ou de configuration externe peuvent nécessiter des mises à jour si ils contiennent des références aux anciens noms.

4. **Déploiement** : Les scripts de déploiement devront être mis à jour pour refléter les nouveaux noms.

## Prochaines étapes recommandées

1. Mettre à jour les fichiers de configuration d'environnement (.env)
2. Mettre à jour les scripts de déploiement
3. Mettre à jour la documentation de déploiement
4. Tester l'application en profondeur
5. Mettre à jour les URLs dans les applications frontend 