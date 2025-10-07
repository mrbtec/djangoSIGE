#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosige.configs')
django.setup()

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_users():
    """Cria usuários de teste para o sistema DjangoSIGE"""
    
    print("=== Criando usuários de teste para DjangoSIGE ===\n")
    
    # Definir senha do admin (já foi criado)
    try:
        admin = User.objects.get(username='admin')
        admin.set_password('admin123')
        admin.save()
        print("✓ Admin: senha definida como 'admin123'")
    except User.DoesNotExist:
        print("✗ Usuário admin não encontrado")
    
    # Criar usuário gerente
    try:
        gerente, created = User.objects.get_or_create(
            username='gerente',
            defaults={
                'email': 'gerente@djangosige.com',
                'is_staff': True,
                'first_name': 'Gerente',
                'last_name': 'Sistema'
            }
        )
        gerente.set_password('gerente123')
        gerente.save()
        status = "criado" if created else "atualizado"
        print(f"✓ Gerente: {status} com senha 'gerente123'")
    except Exception as e:
        print(f"✗ Erro ao criar gerente: {e}")
    
    # Criar usuário vendedor
    try:
        vendedor, created = User.objects.get_or_create(
            username='vendedor',
            defaults={
                'email': 'vendedor@djangosige.com',
                'is_staff': True,
                'first_name': 'Vendedor',
                'last_name': 'Sistema'
            }
        )
        vendedor.set_password('vendedor123')
        vendedor.save()
        status = "criado" if created else "atualizado"
        print(f"✓ Vendedor: {status} com senha 'vendedor123'")
    except Exception as e:
        print(f"✗ Erro ao criar vendedor: {e}")
    
    # Criar usuário financeiro
    try:
        financeiro_user, created = User.objects.get_or_create(
            username='financeiro',
            defaults={
                'email': 'financeiro@djangosige.com',
                'is_staff': True,
                'first_name': 'Financeiro',
                'last_name': 'Sistema'
            }
        )
        financeiro_user.set_password('financeiro123')
        financeiro_user.save()
        status = "criado" if created else "atualizado"
        print(f"✓ Financeiro: {status} com senha 'financeiro123'")
    except Exception as e:
        print(f"✗ Erro ao criar financeiro: {e}")
    
    print("\n=== Resumo dos usuários criados ===")
    print("Username: admin     | Senha: admin123     | Tipo: Superusuário")
    print("Username: gerente   | Senha: gerente123   | Tipo: Staff")
    print("Username: vendedor  | Senha: vendedor123  | Tipo: Staff")
    print("Username: financeiro| Senha: financeiro123| Tipo: Staff")
    print("\nTodos os usuários têm acesso ao admin do Django.")
    print("As permissões específicas podem ser configuradas no admin.")

def configure_permissions():
    """Configura permissões básicas para os usuários"""
    
    print("\n=== Configurando permissões básicas ===")
    
    try:
        # Buscar usuários
        gerente = User.objects.get(username='gerente')
        vendedor = User.objects.get(username='vendedor')
        financeiro_user = User.objects.get(username='financeiro')
        
        # Dar todas as permissões para o gerente (exceto superuser)
        all_permissions = Permission.objects.all()
        gerente.user_permissions.set(all_permissions)
        print("✓ Gerente: todas as permissões atribuídas")
        
        # Permissões do vendedor (vendas e cadastro)
        vendas_perms = Permission.objects.filter(content_type__app_label='vendas')
        cadastro_perms = Permission.objects.filter(content_type__app_label='cadastro')
        vendedor.user_permissions.set(list(vendas_perms) + list(cadastro_perms))
        print("✓ Vendedor: permissões de vendas e cadastro atribuídas")
        
        # Permissões do financeiro
        financeiro_perms = Permission.objects.filter(content_type__app_label='financeiro')
        fiscal_perms = Permission.objects.filter(content_type__app_label='fiscal')
        financeiro_user.user_permissions.set(list(financeiro_perms) + list(fiscal_perms))
        print("✓ Financeiro: permissões financeiras e fiscais atribuídas")
        
    except Exception as e:
        print(f"✗ Erro ao configurar permissões: {e}")

if __name__ == '__main__':
    create_users()
    configure_permissions()
    print("\n✓ Configuração de usuários concluída!")