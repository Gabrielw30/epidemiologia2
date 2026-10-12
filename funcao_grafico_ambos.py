import os
import uuid

import matplotlib

matplotlib.use('Agg')  # Define o backend não interativo antes de importar pyplot
import matplotlib.pyplot as plt
import numpy as np


def gerar_grafico_ambos(beta):
    beta = float(beta)  # Garante tipo numérico
    dt = 0.5
    D_max = 100  # Número de dias
    t = np.arange(0, D_max, dt)

    # Inicialização das listas para o Método de Euler
    N = np.zeros(len(t))
    S = np.zeros(len(t))
    I = np.zeros(len(t))

    # Condições iniciais
    N[0] = 1  # Total de indivíduos (1 = 100%)
    I[0] = 0.01  # Infectados iniciais
    S[0] = N[0] - I[0]  # Suscetíveis iniciais

    # Solução Analítica Exata (SI Sem Dinâmica Vital)
    Ian = I[0] / (I[0] + S[0] * np.exp(-beta * t))
    San = 1 - Ian

    # Loop - Método de Euler (Sem termos de nascimento/mortalidade)
    for i in range(len(t) - 1):
        dS = -beta * S[i] * I[i]
        dI = beta * S[i] * I[i]

        # Método de Euler
        S[i + 1] = S[i] + dS * dt
        I[i + 1] = I[i] + dI * dt

    # Nova figura limpa
    plt.figure(figsize=(8, 5))

    # Plotagem das curvas
    plt.plot(
        t,
        S,
        color='blue',
        linestyle='dashed',
        label='Suscetíveis - Mét. de Euler',
        lw=2,
    )
    plt.plot(
        t,
        I,
        color='red',
        linestyle='dashed',
        label='Infectados - Mét. de Euler',
        lw=2,
    )
    plt.plot(t, San, color='blue', label='Suscetíveis - Sol. Analítica', lw=2)
    plt.plot(t, Ian, color='red', label='Infectados - Sol. Analítica', lw=2)

    # Legenda com o parâmetro Beta
    plt.plot(0, 0, color='none', label=f'β = {beta}')

    plt.grid(True)
    plt.legend(loc='best')
    plt.xlabel('Dias')
    plt.ylabel('População')
    plt.title('Modelo SI - Sem Dinâmica Vital')
    plt.xlim([-0.01, 50.5])
    plt.ylim([-0.01, 1.1])

    # Criação do diretório de destino se não existir
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    nome_pasta = os.path.join(pasta_atual, 'static', 'img', 'ambos')
    os.makedirs(nome_pasta, exist_ok=True)

    nome_arquivo = f'{uuid.uuid4()}.png'
    caminho_final = os.path.join(nome_pasta, nome_arquivo)

    # Salva e fecha a figura
    plt.savefig(caminho_final, dpi=300, bbox_inches='tight')
    plt.close()

    return nome_arquivo