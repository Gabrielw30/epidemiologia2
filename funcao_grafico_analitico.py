import os
import uuid

import matplotlib

matplotlib.use('Agg')  # Define o backend não interativo antes de importar pyplot
import matplotlib.pyplot as plt
import numpy as np


def gerar_grafico_analitico(beta):
    beta = float(beta)  # Garante tipo numérico
    dt = 0.5
    D_max = 100  # Número de dias
    t = np.arange(0, D_max, dt)

    # Condições iniciais
    I0 = 0.01  # Infectados iniciais (1%)
    S0 = 1.0 - I0  # Suscetíveis iniciais (99%)

    # Solução Analítica Exata (Modelo SI Sem Dinâmica Vital)
    Ian = I0 / (I0 + S0 * np.exp(-beta * t))
    San = 1.0 - Ian

    # Configuração do gráfico
    plt.figure(figsize=(8, 5))

    # Plotagem apenas da Solução Analítica
    plt.plot(t, San, color='blue', label='Suscetíveis - Sol. Analítica', lw=2)
    plt.plot(t, Ian, color='red', label='Infectados - Sol. Analítica', lw=2)

    # Legenda com o parâmetro Beta
    plt.plot(0, 0, color='none', label=f'β = {beta}')

    plt.grid(True)
    plt.legend(loc='best')
    plt.xlabel('Dias')
    plt.ylabel('População')
    plt.title('Modelo SI - Solução Analítica')
    plt.xlim([-0.01, 50.5])
    plt.ylim([-0.01, 1.1])

    # Criação do diretório de destino se não existir
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    nome_pasta = os.path.join(pasta_atual, 'static', 'img', 'analitico')
    os.makedirs(nome_pasta, exist_ok=True)

    nome_arquivo = f'{uuid.uuid4()}.png'
    caminho_final = os.path.join(nome_pasta, nome_arquivo)

    # Salva e fecha a figura
    plt.savefig(caminho_final, dpi=300, bbox_inches='tight')
    plt.close()

    return nome_arquivo