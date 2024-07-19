from flask import Flask, render_template, request, jsonify
import csv
from pathlib import Path

app = Flask(__name__)

# Assurez-vous que le fichier questions.csv existe
csv_file = Path("questions.csv")
if not csv_file.is_file():
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Quel est votre film préféré ?"])
        writer.writerow(["Si vous pouviez voyager n'importe où, où iriez-vous ?"])
        writer.writerow(["Quel est votre plat préféré ?"])
        writer.writerow(["Quel talent aimeriez-vous avoir ?"])
        writer.writerow(["Quel est votre livre préféré ?"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-questions')
def get_questions():
    with open('questions.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        questions = [row[0] for row in reader if row]
    return jsonify(questions)

@app.route('/add-question', methods=['POST'])
def add_question():
    new_question = request.form.get('question')
    if new_question:
        with open('questions.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([new_question])
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Question vide"})

if __name__ == '__main__':
    app.run(debug=True)