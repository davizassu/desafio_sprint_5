import csv
import re

# ==========================================
# 1. EXCEÇÃO PERSONALIZADA
# ==========================================
# Crei uma  classe de erro herdando de Exception
# Isso ajuda a identificar erros específicos das nossas regras de negócio.
class FormatoInvalidoError(Exception):
    pass

# ==========================================
# 2. FUNÇÕES DE VALIDAÇÃO COM REGEX (re)
# ==========================================
def validar_dados(linha):
    """
    Usa Expressões Regulares (Regex) para validar o formato de cada campo.
    r"..." significa raw string, o que evita problemas com a barra invertida (\).
    """
    # ^ começa a string. \w significa letras/números. + significa um ou mais. $ termina a string.
    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    
    # \d{3} significa 3 dígitos. Os \. e \- escapam os caracteres literais.
    padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    
    # \(\d{2}\) busca o DDD entre parênteses. \s é um espaço.
    padrao_telefone = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    
    # \d{2}/\d{2}/\d{4} valida o formato dd/mm/aaaa
    padrao_data = r"^\d{2}/\d{2}/\d{4}$"

    # re.match tenta encontrar o padrão exato na string fornecida
    if not re.match(padrao_email, linha['email']):
        raise FormatoInvalidoError(f"E-mail inválido: {linha['email']}")
    
    if not re.match(padrao_cpf, linha['cpf']):
        raise FormatoInvalidoError(f"CPF inválido (use o formato 000.000.000-00): {linha['cpf']}")
        
    if not re.match(padrao_telefone, linha['telefone']):
        raise FormatoInvalidoError(f"Telefone inválido: {linha['telefone']}")
        
    if not re.match(padrao_data, linha['data_nascimento']):
        raise FormatoInvalidoError(f"Data inválida: {linha['data_nascimento']}")
    
    # Gerando um ValueError de propósito se o dia não for número válido (ex: 'xx')
    # O split divide a data pela barra: '15/05/1995' vira ['15', '05', '1995']
    dia = int(linha['data_nascimento'].split('/')[0])
    if dia < 1 or dia > 31:
        raise ValueError("O dia da data de nascimento deve estar entre 1 e 31.")

# ==========================================
# 3. LEITURA DE ARQUIVOS E TRATAMENTO DE ERROS
# ==========================================
registros_validos = []
registros_invalidos = []

print("Iniciando análise de dados...\n")

# try tentará executar o código perigoso (que pode dar erro)
try:
    # with open cuida de abrir e FECHAR o arquivo automaticamente no final
    with open("dados.csv", mode="r", encoding="utf-8") as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        
        for num_linha, linha in enumerate(leitor_csv, start=1):
            try:
                # Vamos forçar a checagem das chaves para gerar KeyError se faltar coluna no CSV
                _ = linha['nome']
                _ = linha['email']
                _ = linha['cpf']
                
                # Chamamos a função que pode disparar o FormatoInvalidoError
                validar_dados(linha)
                
                # Se passou por todas as validações sem "gritar" um erro, é válido!
                registros_validos.append(linha)
                
            except FormatoInvalidoError as erro:
                # Captura o erro customizado que criamos lá em cima
                registros_invalidos.append((num_linha, linha['nome'], str(erro)))
                
            except ValueError as erro:
                # Captura erros de conversão (ex: tentar transformar texto em int)
                registros_invalidos.append((num_linha, linha['nome'], f"Erro de valor: {erro}"))
                
            except KeyError as erro:
                # Captura erros se a coluna do CSV não existir
                registros_invalidos.append((num_linha, "Desconhecido", f"Coluna ausente no CSV: {erro}"))

except FileNotFoundError:
    print(" ERRO CRÍTICO: O arquivo 'dados.csv' não foi encontrado. Verifique o caminho.")
    
except Exception as erro_geral:
    # Um "pega tudo" para qualquer outro erro inesperado que não previmos
    print(f" ERRO INESPERADO: Ocorreu um problema -> {erro_geral}")

else:
    # O 'else' só é executado se o 'try' principal terminar SEM NENHUM ERRO
    print(" Leitura do arquivo concluída com sucesso! Gerando relatório...\n")
    
    # ==========================================
    # 4. RELATÓRIO FINAL FORMATADO (f-strings)
    # ==========================================
    total_linhas = len(registros_validos) + len(registros_invalidos)
    
    print("="*50)
    print(" RELATÓRIO DE ANÁLISE DE DADOS")
    print("="*50)
    print(f"Total de registros processados: {total_linhas}")
    print(f"Registros Válidos: {len(registros_validos)} ({(len(registros_validos)/total_linhas)*100:.1f}%)")
    print(f"Registros Inválidos: {len(registros_invalidos)} ({(len(registros_invalidos)/total_linhas)*100:.1f}%)\n")
    
    if registros_invalidos:
        print(" DETALHES DOS ERROS ENCONTRADOS:")
        for num, nome, motivo in registros_invalidos:
            print(f"  - Linha {num} ({nome}): {motivo}")
            
finally:
    # O 'finally' SEMPRE executa, dando erro ou não. Ótimo para fechar bancos de dados ou logs.
    print("\n" + "="*50)
    print("Fim do processo. O bloco 'finally' foi executado.")
    print("="*50)