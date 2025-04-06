import matplotlib.pyplot as plt
import math


def lancamento_obliquo():
    print("=== Simulação de Lançamento Oblíquo ===")
    
    
    v0 = float(input("Digite a velocidade inicial (m/s): "))
    angulo = float(input("Digite o ângulo de lançamento (graus): "))
    y0 = float(input("Digite a altura inicial (em metros, pode ser 0): "))
    
    # Conversão do ângulo para radianos
    theta = math.radians(angulo)
    
    # Componentes da velocidade
    v0x = v0 * math.cos(theta)
    v0y = v0 * math.sin(theta)
    
    # Aceleração da gravidade
    g = 9.8

    # Cálculo do tempo total de voo com fórmula alternativa
    t_total = (v0y + math.sqrt(v0y**2 + 2 * g * y0)) / g

    # Criando listas de pontos da trajetória
    tempos = [t/100 for t in range(int(t_total * 100) + 1)]
    x = [v0x * t for t in tempos]
    y = [y0 + v0y * t - 0.5 * g * t**2 for t in tempos]

    # Plotando o gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color='blue')
    plt.title('Lançamento Oblíquo - Trajetória')
    plt.xlabel('Distância (m)')
    plt.ylabel('Altura (m)')
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.show()

lancamento_obliquo()
