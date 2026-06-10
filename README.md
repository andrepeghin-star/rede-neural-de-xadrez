# 🎮 Chess Neural Evolution System

## Visão Geral
Sistema de inteligência artificial que aprende a jogar xadrez através de duas redes neurais que competem entre si, evoluindo continuamente de forma consistente e observável em tempo real.

### Características Principais
- ✅ Engine de xadrez funcional com validação completa de movimentos
- ✅ Duas redes neurais independentes (Brancas vs Pretas)
- ✅ Treinamento por auto-jogo com mutação genética
- ✅ Visualização em tempo real do tabuleiro
- ✅ Controle de velocidade de simulação (0.5x até 5x)
- ✅ Gráficos de evolução de desempenho
- ✅ Sistema de pontuação Elo
- ✅ Histórico de partidas

## Instalação

```bash
pip install -r requirements.txt
```

## Como Executar

```bash
python app.py
```

Abra no navegador: `http://localhost:5000`

## Estrutura do Projeto

```
rede-neural-de-xadrez/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── chess_engine/
│   ├── __init__.py
│   ├── board.py          # Lógica do tabuleiro
│   ├── rules.py          # Regras do xadrez
│   ├── move_generator.py # Gerador de movimentos
│   └── piece_values.py   # Valores das peças
├── neural_network/
│   ├── __init__.py
│   ├── model.py          # Arquitetura da rede
│   ├── trainer.py        # Sistema de treinamento
│   └── evaluation.py     # Função de avaliação
├── game_engine/
│   ├── __init__.py
│   ├── game.py           # Controlador do jogo
│   ├── evolution.py      # Sistema evolutivo
│   └── stats.py          # Estatísticas
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── board.js      # Renderização do tabuleiro
│       ├── game.js       # Lógica do jogo
│       └── charts.js     # Gráficos
└── templates/
    └── index.html        # Interface
```

## Tecnologia
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: TensorFlow/Keras
- **Gráficos**: Chart.js, Plotly
- **Real-time**: WebSockets

## Como Funciona a Evolução

1. **Inicialização**: Duas redes neurais começam com pesos aleatórios
2. **Auto-Jogo**: As redes jogam uma contra a outra
3. **Avaliação**: Vitórias/Derrotas determinam fitness
4. **Mutação**: Pequenas variações nos pesos das redes vencedoras
5. **Iteração**: Processo repetido continuamente

## Controles da Interface

- ⏯️ **Play/Pause**: Iniciar ou pausar simulação
- ⏩ **Velocidade**: Controle deslizante (0.5x até 5x)
- 🔄 **Reset**: Reiniciar as redes do zero
- 📊 **Gráficos**: Visualizar evolução em tempo real
- 📋 **Histórico**: Ver partidas anteriores

## Performance

A IA deve evoluir de forma consistente:
- **Jogos 1-100**: Aprende movimentos básicos
- **Jogos 100-500**: Tática simples emerge
- **Jogos 500+**: Estratégia mais complexa

## Autor

André Peghin

---

**Divirta-se observando a evolução artificial!** 🧠♟️
