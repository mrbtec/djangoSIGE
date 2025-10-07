#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Lê o arquivo
with open('/home/moises/gitlocal/djangoSIGE/djangosige/apps/vendas/models/vendas.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Substitui todas as ocorrências de locale.format
# Padrão: locale.format(u'%.2f', valor, 1) -> format_decimal(valor)
content = re.sub(r"locale\.format\(u?['\"]%.2f['\"],\s*([^,)]+),\s*1\)", r'format_decimal(\1)', content)

# Escreve o arquivo modificado
with open('/home/moises/gitlocal/djangoSIGE/djangosige/apps/vendas/models/vendas.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Arquivo corrigido com sucesso!")