# Copilot Instructions for DjangoSIGE

## Architecture Overview

DjangoSIGE is a Brazilian ERP (Enterprise Resource Planning) system built with Django 3.1.7. It's organized into modular apps following Brazilian business requirements.

### Core Apps Structure
- **base**: Custom views, mixins, permissions system, and shared utilities
- **cadastro**: Entity management (products, clients, suppliers, companies)
- **vendas**: Sales module (quotations, orders, invoices)
- **compras**: Purchase module (orders, supplier management)
- **financeiro**: Financial module (chart of accounts, cash flow)
- **estoque**: Inventory control and stock management
- **fiscal**: Brazilian tax compliance (NF-e, NFC-e integration via PySIGNFe)
- **login**: Authentication and user management

## Key Patterns & Conventions

### Custom Views Architecture
All views inherit from custom base classes in `djangosige/apps/base/custom_views.py`:
- Use `CustomCreateView`, `CustomUpdateView`, `CustomListView` instead of Django's generic views
- These include built-in permission checking via `CheckPermissionMixin`
- Always set `permission_codename` for permission-protected views

### Permission System
- Uses `CheckPermissionMixin` from `views_mixins.py` for granular permissions
- Permissions follow Django convention: `app_label.action_modelname`
- SuperUser bypass available via `SuperUserRequiredMixin`

### Model Organization
Models are split into separate files within each app's `models/` directory:
```python
# models/__init__.py imports all models
from .base import Pessoa, PessoaFisica, PessoaJuridica
from .produto import Produto, Unidade, Marca
```

### Configuration Pattern
- Settings split between `configs/settings.py` and `configs/configs.py`
- Use `configs.py` for business-specific defaults (email, database)
- Environment variables via `python-decouple` (.env file)

## Development Workflows

### Setup Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Generate .env file
python contrib/env_gen.py

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Development server
python manage.py runserver
# or use: make run
```

### Testing
```bash
# Load test fixtures
python manage.py loaddata djangosige/tests/fixtures/test_db_backup.json

# Run tests
python manage.py test
# or use: make test
```

### Brazilian Business Context
- **NF-e/NFC-e**: Electronic invoices required by Brazilian tax law
- **SEFAZ**: Brazilian tax authority integration
- **CPF/CNPJ**: Brazilian individual/company ID formats
- All forms and interfaces are in Portuguese
- Currency handling follows Brazilian Real (BRL) format

## Critical Integration Points

### PySIGNFe Integration
Optional but critical for fiscal compliance:
- Handles electronic invoice generation and SEFAZ communication
- Configured via `configs/configs.py`
- Used in `fiscal` app for NF-e/NFC-e operations

### PDF Generation
Uses custom `geraldo` fork for reports:
- Sales/purchase order PDFs
- Invoice generation
- Located in individual app's view logic

## File Patterns to Follow

### New App Creation
1. Create `models/` directory with `__init__.py`
2. Create `views/`, `forms/`, `migrations/` directories
3. Add app to `INSTALLED_APPS` in settings
4. Create URL patterns following `/app_name/` convention
5. Use custom view classes from `base.custom_views`

### Form Handling
- Forms typically in `forms/` directory, split by model category
- Use `FormValidationMessageMixin` for consistent error handling
- Follow Brazilian field validation patterns (CPF, CNPJ, CEP)

## Common Gotchas

- Always use custom view classes, not Django's generic ones
- Permission checking is automatic if you set `permission_codename`
- Test settings use `djangosige.tests.test_settings` (auto-detected in manage.py)
- Brazilian locale considerations: date formats, currency, postal codes
- PySIGNFe is optional - gracefully handle when not installed