import math
import os
import uuid
import matplotlib.pyplot as plt


def gerar_grafico_euler(beta=2.0):
    # ==========================================================
    # Configuração gráfica da fonte (qualidade para artigo)
    # ==========================================================
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 12
    })

    # ==================================================
    # Definição da equação e Método de Euler
    # ==================================================
    # Equação diferencial: y'(t) = -beta * y + exp(-t)
    def f(t, y):
        return -beta * y + math.exp(-t)

    def euler(f, t0, y0, tf, h):
        t = t0
        y = y0
        ts = [t]
        ys = [y]
        while t < tf - 1e-12:
            y = y + h * f(t, y)
            t = round(t + h, 12)  # Corrigido: usava 'dt' em vez de 'h'
            ts.append(t)
            ys.append(y)
        return ts, ys

    # ==================================================
    # Condições do Problema
    # ==================================================
    t0, y0, tf = 0.0, 1.0, 2.4
    dts = [0.4, 0.2, 0.1, 0.05]  # Passos utilizados

    # ==================================================
    # Solução exata analítica dependente de beta
    # ==================================================
    def y_exact(t):
        if math.isclose(beta, 1.0):
            return (t + 1.0) * math.exp(-t)
        else:
            return (1.0 / (beta - 1.0)) * (math.exp(-t) + (beta - 2.0) * math.exp(-beta * t))

    # ==================================================
    # Gráfico da solução
    # ==================================================
    cores = ['red', 'blue', 'orange', 'green']
    estilos = ['dashed', 'dashdot', 'dotted', ':']
    marcadores = ['o', 's', '^', 'D']  # Nome da lista ajustado para o plural

    plt.figure(figsize=(7, 5))

    # Corrigido: desestruturação usando 'estilo' no singular no loop
    for dt, cor, estilo, marcador in zip(dts, cores, estilos, marcadores):
        ts, ys = euler(f, t0, y0, tf, dt)
        plt.plot(
            ts, ys,
            color=cor,
            linestyle=estilo,
            marker=marcador,
            linewidth=1.5,
            label=f"Euler δt ={dt}"
        )

    t_plot = [t0 + i * 0.001 for i in range(int((tf - t0) / 0.001) + 1)]
    plt.plot(t_plot, [y_exact(t) for t in t_plot], 'k-', linewidth=2, label='Solução exata')

    # ==========================================================
    # Eixos e Legenda
    # ==========================================================
    plt.xlabel("$t$", fontsize=18)
    plt.ylabel("$y(t)$", fontsize=18)
    plt.xlim([-0.05, 2.5])
    plt.grid(True, alpha=0.3)
    plt.legend(
        fancybox=True,
        edgecolor='black',
        framealpha=1,
        borderpad=1.2,
        fontsize=12
    )
    plt.tight_layout()

    # ==========================================================
    # Salvar gráfico
    # ==========================================================
    nome_arquivo = f"{uuid.uuid4()}.png"

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    nome_pasta = os.path.join(pasta_atual, "static", "img", 'euler')

    # Garante que as pastas de destino existam antes de salvar
    os.makedirs(nome_pasta, exist_ok=True)

    caminho_final = os.path.join(nome_pasta, nome_arquivo)

    plt.savefig(caminho_final, dpi=300, bbox_inches="tight")
    plt.close()

    return nome_arquivo