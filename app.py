import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
import numpy as np
from threading import Thread
import time

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Estado global da evolução
evolution_state = {
    'running': False,
    'paused': False,
    'speed': 1.0,
    'generation': 0,
    'games_played': 0,
    'white_wins': 0,
    'black_wins': 0,
    'draws': 0,
    'white_rating': 1000,
    'black_rating': 1000,
    'game_history': [],
    'evolution_thread': None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    return jsonify({
        'generation': evolution_state['generation'],
        'games_played': evolution_state['games_played'],
        'white_wins': evolution_state['white_wins'],
        'black_wins': evolution_state['black_wins'],
        'draws': evolution_state['draws'],
        'white_rating': evolution_state['white_rating'],
        'black_rating': evolution_state['black_rating'],
        'game_history': evolution_state['game_history'][-50:]
    })

@app.route('/api/start', methods=['POST'])
def start_evolution():
    if not evolution_state['running']:
        evolution_state['running'] = True
        evolution_state['paused'] = False
        evolution_state['evolution_thread'] = Thread(target=evolution_loop, daemon=True)
        evolution_state['evolution_thread'].start()
    return jsonify({'status': 'started'})

@app.route('/api/pause', methods=['POST'])
def pause_evolution():
    evolution_state['paused'] = not evolution_state['paused']
    return jsonify({'paused': evolution_state['paused']})

@app.route('/api/reset', methods=['POST'])
def reset_evolution():
    evolution_state['running'] = False
    evolution_state['generation'] = 0
    evolution_state['games_played'] = 0
    evolution_state['white_wins'] = 0
    evolution_state['black_wins'] = 0
    evolution_state['draws'] = 0
    evolution_state['white_rating'] = 1000
    evolution_state['black_rating'] = 1000
    evolution_state['game_history'] = []
    return jsonify({'status': 'reset'})

@app.route('/api/speed/<float:speed>', methods=['POST'])
def set_speed(speed):
    evolution_state['speed'] = min(5.0, max(0.5, speed))
    return jsonify({'speed': evolution_state['speed']})

def evolution_loop():
    while evolution_state['running']:
        if evolution_state['paused']:
            time.sleep(0.2)
            continue
        
        play_game()
        delay = 0.8 / evolution_state['speed']
        time.sleep(delay)

def play_game():
    evolution_state['generation'] += 1
    evolution_state['games_played'] += 1
    
    # Simula um jogo com probabilidades realistas
    rand = np.random.random()
    if rand < 0.4:
        result = 'white'
        evolution_state['white_wins'] += 1
        evolution_state['white_rating'] += np.random.randint(5, 15)
        evolution_state['black_rating'] -= np.random.randint(3, 10)
    elif rand < 0.8:
        result = 'black'
        evolution_state['black_wins'] += 1
        evolution_state['black_rating'] += np.random.randint(5, 15)
        evolution_state['white_rating'] -= np.random.randint(3, 10)
    else:
        result = 'draw'
        evolution_state['draws'] += 1
        evolution_state['white_rating'] += np.random.randint(1, 5)
        evolution_state['black_rating'] += np.random.randint(1, 5)
    
    # Evita ratings abaixo de 800
    evolution_state['white_rating'] = max(800, evolution_state['white_rating'])
    evolution_state['black_rating'] = max(800, evolution_state['black_rating'])
    
    # Adiciona ao histórico
    evolution_state['game_history'].append({
        'game': evolution_state['games_played'],
        'result': result,
        'white_rating': evolution_state['white_rating'],
        'black_rating': evolution_state['black_rating']
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
