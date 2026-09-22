import os
import numpy as np
import matplotlib.pyplot as plt
import uuid
import math
# Código para gerar figura, para vários passos, comparativa no método de Euler 18 de julho de 2026





def gerar_grafico_euler(beta):
# ==========================================================
# Configuração gráfica pa fonte (qualidade para artigo científico)
# ==========================================================
    plt.rcParams.update({ "font.family": "serif", "mathtext.fontset": "cm", "font.size": 12})

    # ==================================================
    # Definição da equação e Método de Euler
    # ==================================================

    def f(t, y):
        return -2*y + math.exp(-t)

    def euler(f, t0, y0, tf, h):
        t = t0
        y = y0
        ts = [t]
        ys = [y]
        while t < tf - 1e-12:
            y = y + h * f(t, y)
            t = round(t + dt, 12)
            ts.append(t)
            ys.append(y)
        return ts, ys

    # ==================================================
    # Condições do Problema
    # ==================================================

    t0, y0, tf = 0.0, 1.0, 2.4
    #dts = [0.4, 0.3, 0.2, 0.1]
    #dts = [0.5, 0.25, 0.125, 0.0625]
    dts = [0.4, 0.2, 0.1, 0.05] #Passos utilizados

    # ==================================================
    # Solução exata
    # ==================================================

    def y_exact(t):
        return math.exp(-t)

    # ==================================================
    # Gráfico da solução
    # ==================================================

    cores = ['red', 'blue', 'orange', 'green']
    estilos  = ['dashed', 'dashdot', 'dotted', ':']
    marcador = ['o', 's', '^', 'D']

    plt.figure(figsize=(7, 5))

    for dt, cor, estilos,marcador in zip(dts, cores, estilos,marcador):
        ts, ys = euler(f, t0, y0, tf, dt)
        plt.plot(ts, ys, color=cor, linestyle=estilos, marker=marcador, linewidth=1.5,
                label=f"Euler δt ={dt}")

    t_plot = [t0 + i*0.001 for i in range(int((tf - t0)/0.001) + 1)]
    plt.plot(t_plot, [y_exact(t) for t in t_plot], 'k-', linewidth=2, label='Solução exata')

    # ==========================================================
    # Eixos e Legenda
    # ==========================================================

    plt.xlabel("$t$",fontsize=18)
    plt.ylabel("$y(t)$",fontsize=18)
    plt.xlim([-0.05, 2.5])
    plt.ylim([-0.01, 1.1])
    #plt.title("Método de Euler: efeito do tamanho do passo")
    plt.grid(True, alpha=0.3)
    plt.legend(fancybox=True, edgecolor='black', framealpha=1,
    borderpad=1.2, fontsize=12)
    plt.tight_layout()

    # ==========================================================
    # Salvar gráfico
    # ==========================================================
    nome_arquivo = f"{uuid.uuid4()}.png"

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    nome_pasta = os.path.join(pasta_atual, "static", "img", 'euler')
    caminho_final = os.path.join(nome_pasta, nome_arquivo)

    plt.savefig(caminho_final, dpi=300,  bbox_inches="tight"
    )


    plt.close()

    return nome_arquivo
