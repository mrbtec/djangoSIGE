# -*- coding: utf-8 -*-

import locale

def format_currency(value):
    """
    Formata um valor numérico como moeda brasileira.
    Substitui o locale.format() que foi removido no Python 3.12+
    """
    try:
        # Tenta usar locale.currency() se disponível
        return locale.currency(value, symbol=False, grouping=True)
    except:
        # Fallback para formatação manual
        return "{:.2f}".format(float(value)).replace('.', ',')

def format_decimal(value, decimals=2):
    """
    Formata um valor numérico com número específico de casas decimais.
    Substitui o locale.format() que foi removido no Python 3.12+
    """
    try:
        # Configura locale brasileiro se possível
        locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')
    except:
        pass
    
    try:
        # Tenta usar locale para formatação
        format_str = f"%.{decimals}f"
        return locale.format_string(format_str, float(value), grouping=True)
    except:
        # Fallback para formatação manual brasileira
        format_str = f"{{:.{decimals}f}}"
        formatted = format_str.format(float(value))
        # Converte ponto para vírgula (padrão brasileiro)
        return formatted.replace('.', ',')