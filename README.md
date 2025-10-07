# DjangoSIGE [![Build Status](https://travis-ci.org/thiagopena/djangoSIGE.svg?branch=master)](https://travis-ci.org/thiagopena/djangoSIGE)

Sistema Integrado de Gestão Empresarial baseado em Django

Projeto independente open-source desenvolvido em Python 3 no Windows, testado no GNU/Linux e Windows.

## ⭐ Novidades e Melhorias (Outubro 2025)

### 🐍 **Compatibilidade Python 3.12+**
- ✅ **Corrigido problema `locale.format()`** removido no Python 3.12+
- ✅ **Nova função `format_decimal()`** para formatação brasileira
- ✅ **Suporte completo ao Python 3.12** mantendo retrocompatibilidade

### 🔧 **Melhorias na Configuração**
- ✅ **Configurações de apps corrigidas** - paths completos nos `apps.py`
- ✅ **Script de criação de usuários** - `create_users.py` para setup rápido
- ✅ **Tratamento de erro no locale** - fallback para sistemas sem locale configurado

### 🤖 **Documentação para IA**
- ✅ **Instruções para Copilot** - `.github/copilot-instructions.md`
- ✅ **Guia para agentes de IA** - padrões específicos do projeto
- ✅ **Arquitetura documentada** - facilita desenvolvimento assistido por IA

### 👥 **Usuários de Teste Pré-configurados**
Execute `python create_users.py` para criar usuários com diferentes níveis:
- `admin` / `admin123` - Superusuário com acesso total
- `gerente` / `gerente123` - Acesso de gerência  
- `vendedor` / `vendedor123` - Acesso a vendas e cadastros
- `financeiro` / `financeiro123` - Acesso financeiro e fiscal


## Dependências

- [Python](https://www.python.org/downloads/) - **Versão 3.8+ (testado até 3.12)**
- [django](http://www.djangoproject.com) == 3.2.25
- [geraldo](https://github.com/thiagopena/geraldo) - Geração de PDF para pedidos de venda/compra
- [PySIGNFe](https://github.com/thiagopena/PySIGNFe) (Opcional) - Necessário para a geração de NF-e, NFC-e, comunicação com SEFAZ, geração do DANFE, etc.
- [apache2](https://www.apache.org/) (Opcional)
- [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/) (Opcional)

## Instalação:

0. Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
```

1. Instalar dependências:

```bash
pip install -r requirements.txt
```

2. Edite o conteúdo do arquivo **djangosige/configs/configs.py**

3. Gere um `.env` local

```bash
python contrib/env_gen.py
```


4. Sincronize a base de dados:

```bash
python manage.py migrate
```

5. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

**OU** use o script de criação rápida de usuários para desenvolvimento:

```bash
python create_users.py
```
*Cria usuários de teste: admin, gerente, vendedor, financeiro (senhas iguais aos usernames + "123")*

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):

```bash
python manage.py runserver
```

## Implementações

- Cadastro de produtos, clientes, empresas, fornecedores e transportadoras
- Login/Logout
- Criação de perfil para cada usuário.
- Definição de permissões para usuários.
- Criação e geração de PDF para orçamentos e pedidos de compra/venda
- Módulo financeiro (Plano de Contas, Fluxo de Caixa e Lançamentos)
- Módulo para controle de estoque
- Módulo fiscal:
    - Geração e armazenamento de notas fiscais
    - Validação do XML de NF-e/NFC-es
    - Emissão, download, consulta e cancelamento de NF-e/NFC-es **(Testar em ambiente de homologação)**
    - Comunicação com SEFAZ (Consulta de cadastro, inutilização de notas, manifestação do destinatário)
- Interface simples e em português

## 🔧 Scripts Utilitários

- `create_users.py` - Cria usuários de teste com diferentes permissões
- `fix_locale_format.py` - Corrige compatibilidade com Python 3.12+
- `contrib/env_gen.py` - Gera arquivo `.env` para configuração

## 💡 Desenvolvimento

### Para Desenvolvedores
- Consulte `.github/copilot-instructions.md` para padrões e convenções
- Use os usuários de teste para verificar diferentes níveis de acesso
- Sistema otimizado para desenvolvimento assistido por IA

### Formatação Brasileira
- Utiliza vírgula como separador decimal
- Formatação monetária em Real (BRL)
- Datas no formato brasileiro (dd/mm/aaaa)

## 🖥️ Compatibilidade

### Versões do Python Suportadas
- ✅ Python 3.8+
- ✅ Python 3.9
- ✅ Python 3.10 
- ✅ Python 3.11
- ✅ Python 3.12+ **(com correções implementadas)**

### Sistemas Operacionais Testados
- ✅ Ubuntu 20.04+
- ✅ Windows 10/11
- ✅ macOS (parcialmente testado)

### Navegadores Suportados
- Google Chrome (recomendado)
- Mozilla Firefox
- Microsoft Edge
- Safari

## Créditos

- [AdminBSBMaterialDesign](https://github.com/gurayyarar/AdminBSBMaterialDesign)
- [geraldo](https://github.com/marinho/geraldo)
- [jQuery-Mask-Plugin](https://igorescobar.github.io/jQuery-Mask-Plugin/)
- [DataTables](https://datatables.net/)
- [JQuery multiselect](http://loudev.com/)

## Ajuda

Para relatar bugs ou fazer perguntas utilize o [Issues](https://github.com/thiagopena/djangoSIGE/issues) ou via email thiagopena01@gmail.com

Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.

### 🆕 Changelog (Outubro 2025)
- **Compatibilidade Python 3.12+**: Corrigido `locale.format()` deprecated
- **Scripts de setup**: Adicionado `create_users.py` para usuários de teste
- **Documentação IA**: Instruções para Copilot e agentes de IA
- **Melhorias na configuração**: Apps configs corrigidos
- **Formatação brasileira**: Mantida com nova implementação compatível
