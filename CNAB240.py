import os
from pick import pick

def process_file(file_path):
    """
    Lê um arquivo de texto, verifica a coluna 8 e soma os números entre as colunas 24 e 48
    para as linhas onde a coluna 8 contém o número 5.

    Args:
        file_path (str): Caminho para o arquivo de texto.

    Returns:
        float: Soma total dos valores encontrados.
    """
    total_sum = 0.0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Verifica se a linha tem comprimento suficiente para evitar erros
                if len(line) >= 41:
                    # Verifica se a coluna 8 contém o número '5'
                    if line[7] == '5':
                        # Extrai os números entre as colunas 24 e 48 (índices 23 a 47)
                        value_str = line[23:41].strip()

                        # Remove os zeros à esquerda, até encontrar o primeiro número significativo
                        value_str = value_str.lstrip('0')

                        if value_str:  # Verifica se o valor extraído não está vazio
                            try:
                                # Converte o valor para float e soma ao total
                                total_sum += int(value_str)
                            except ValueError:
                                print(f"Valor inválido encontrado na linha: {line.strip()}")

        # Agora, dividimos a soma por 100 para tratar centavos corretamente
        total_sum /= 100

        # Formata o valor total com "R$"
        formatted_sum = f"R$ {total_sum:,.2f}"
        print(f"Soma total dos valores: {formatted_sum}")
        return formatted_sum  # Retorna o valor formatado
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
    return None

if __name__ == "__main__":
    while True:
        # Define um caminho padrão para os arquivos
        default_path = "C:/cnab/remessa/"

        # Lista os arquivos disponíveis no diretório
        try:
            files = [f for f in os.listdir(default_path) if os.path.isfile(os.path.join(default_path, f))]
            if not files:
                print("Nenhum arquivo encontrado no diretório padrão.")
                break
            else:
                # Exibe um menu interativo para escolher o arquivo
                title = "Selecione o arquivo para processar (use as setas para navegar):"
                option, index = pick(files, title)

                # Concatena o caminho padrão com o nome do arquivo escolhido
                file_path = os.path.join(default_path, option)

                # Processa o arquivo escolhido e armazena a soma
                formatted_sum = process_file(file_path)

                if formatted_sum:
                    # Exibe um menu para perguntar se o usuário deseja continuar
                    continue_title = f"Resultado do arquivo anterior: {formatted_sum}\nDeseja verificar outro arquivo?"
                    continue_options = ["Sim", "Não"]
                    continue_option, _ = pick(continue_options, continue_title)

                    if continue_option == "Não":
                        print("Encerrando o programa. Até mais!")
                        break
        except Exception as e:
            print(f"Erro ao listar os arquivos no diretório padrão: {e}")
            break
