from flask import Flask, redirect, render_template, request, url_for, jsonify
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import model_training as mt
import pandas as pd
import re
import model_training as mt

app = Flask(__name__)

def process_chat_file(file):
    if file:
        content=file.read().decode('utf-8')
        chat_messages = []
        chat_data = content.splitlines()
        for line in chat_data:
            match = re.match(r"(\d{2}/\d{2}/\d{2}, \d{2}:\d{2}) - (.+?): (.+)", line)
            if match:
                sender = match.group(2)
                message = match.group(3)
                chat_messages.append({'Sender': sender, 'Message': message})

        data = pd.DataFrame(chat_messages)
        data["Message"] = data["Message"].str.lower()
        return data.head(20).to_html()

@app.route('/')
def upload_chat():
    return render_template('upload.html')

@app.route('/analyze', methods=['POST'])
def analyze_chat():
    if 'chat_file' not in request.files:
        return redirect(url_for('upload_chat'))

    file = request.files['chat_file']
    processed_data = process_chat_file(file)

    return render_template('analyze.html', data=processed_data)

@app.route('/train_model',methods=["POST"])
def train_model():
    messages = request.form['messages']
    senders = request.form['senders']
    train = request.form['train']
    
    file=request.files['chat_file']
    chat_data=process_chat_file(file)


    accuracy=mt.train_data(chat_data)
    return render_template('model_train.html',accuracy=accuracy)

if __name__ == '__main__':
    app.run(debug=True)


    
