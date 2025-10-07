#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para corrigir automaticamente as ocorrências de locale.format() 
que foi removido no Python 3.12+
"""

import os
import re

# Lista de arquivos que precisam ser corrigidos
arquivos_para_corrigir = [
    'djangosige/tests/financeiro/test_views.py',
]

def corrigir_arquivo(caminho_arquivo):
    """Corrige um arquivo específico"""
    if not os.path.exists(caminho_arquivo):
        print(f"❌ Arquivo não encontrado: {caminho_arquivo}")
        return False
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Backup do conteúdo original
        conteudo_original = conteudo
        
        # Adicionar import se necessário
        if 'from djangosige.apps.base.utils import format_decimal' not in conteudo:
            # Procurar a linha de imports e adicionar o novo import
            if 'import locale' in conteudo:
                conteudo = conteudo.replace(
                    'import locale',
                    'import locale\nfrom djangosige.apps.base.utils import format_decimal'
                )
        
        # Substituir locale.format por format_decimal
        # Padrão: locale.format(u'%.2f', valor, 1) -> format_decimal(valor)
        padrao = r"locale\.format\(u?['\"]%.2f['\"],\s*([^,]+),\s*1\)"
        conteudo = re.sub(padrao, r'format_decimal(\1)', conteudo)
        
        # Padrão mais complexo para casos como:
        # locale.format(u'%.2f', Decimal(...), 1)
        padrao_complexo = r"locale\.format\(\s*u?['\"]%.2f['\"],\s*([^)]+)\),\s*1\)"
        conteudo = re.sub(padrao_complexo, r'format_decimal(\1))', conteudo)
        
        # Verificar se houve mudanças
        if conteudo != conteudo_original:
            # Salvar arquivo corrigido
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            print(f"✅ Arquivo corrigido: {caminho_arquivo}")
            return True
        else:
            print(f"ℹ️  Nenhuma correção necessária: {caminho_arquivo}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao corrigir {caminho_arquivo}: {e}")
        return False

def main():
    """Função principal"""
    print("=== Correção de locale.format() para Python 3.12+ ===\n")
    
    total_corrigidos = 0
    
    for arquivo in arquivos_para_corrigir:
        if corrigir_arquivo(arquivo):
            total_corrigidos += 1
    
    print(f"\n=== Resumo ===")
    print(f"📁 Total de arquivos processados: {len(arquivos_para_corrigir)}")
    print(f"✅ Arquivos corrigidos: {total_corrigidos}")
    print(f"ℹ️  Arquivos sem alterações: {len(arquivos_para_corrigir) - total_corrigidos}")
    
    if total_corrigidos > 0:
        print("\n🎉 Correções aplicadas com sucesso!")
        print("💡 Execute os testes para verificar se tudo está funcionando.")
    else:
        print("\n😊 Todos os arquivos já estavam atualizados.")

if __name__ == '__main__':
    main()