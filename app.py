from flask import Flask,render_template, session, jsonify, request
from boggle import Boggle

app = Flask(__name__)
app.secret_key = 'okan'  
boggle_game = Boggle()

@app.route('/')
def index():
    """Render the main game page."""
    board = boggle_game.make_board()
    session['board'] = board
    session['score'] = 0
    session['games_played'] = session.get('games_played', 0)
    session['highest_score'] = session.get('highest_score', 0)
    return render_template('index.html', board=board)

@app.route('/check-word', methods=['POST'])
def check_word():
    """Check if the submitted word is valid."""
    word = request.json.get('word')
    board = session.get('board')
    result = boggle_game.check_valid_word(board, word)
    return jsonify({"result": result})

@app.route('/end-game', methods=['POST'])
def end_game():
    """Update game statistics at the end of a game."""
    score = request.json.get('score')


    session['games_played'] += 1
    if score > session['highest_score']:
        session['highest_score'] = score

    
    return jsonify({
        "games_played": session['games_played'],
        "highest_score": session['highest_score']
    })

if __name__ == '__main__':
    app.run(debug=True)  
