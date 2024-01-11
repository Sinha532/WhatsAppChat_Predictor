from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def train_data(data):
    tokenizer=Tokenizer(lower=True)
    tokenizer.fit_on_texts(data['Message'])
    X=tokenizer.texts_to_sequences(data['Message'])
    X=pad_sequences(X)

    label_encoder=LabelEncoder()
    y=label_encoder.fit_transform(data['Sender'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    vocab_size = len(tokenizer.word_index) + 1
    max_length = X.shape[1]

    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=100, input_length=max_length))
    model.add(LSTM(100))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))
    loss,accuracy=model.evaluate(X_test,y_test)

    return accuracy


