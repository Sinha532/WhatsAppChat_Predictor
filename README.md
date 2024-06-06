# Chat Authenticator Using LSTM

## Project Overview
This project aims to determine whether a chat participant is a known or unknown person by analyzing their texting style. By leveraging Natural Language Processing (NLP) and Long Short-Term Memory (LSTM) models, we can predict the sender of a message based on their unique texting patterns.

## Problem Statement
In today's digital communication landscape, ensuring the authenticity of the person we are chatting with is crucial for both personal security and professional integrity. This project addresses this issue by developing a model that can identify the texting style of chat participants.

## Solution Developed
### Data Collection and Preprocessing
- **Source:** WhatsApp chat file.
- **Extraction:** Extracted sender and message data.
- **Preprocessing:** Converted messages to lowercase and saved them in a CSV file for further processing.

### Tokenization and Sequence Padding
- **Tokenizer:** Used Keras Tokenizer to convert text messages into sequences.
- **Padding:** Applied sequence padding to ensure uniform input size for the model.

### Label Encoding
- Transformed sender labels into numerical values using `LabelEncoder` from `sklearn`.

### Model Development
- **Architecture:** Built an LSTM model using Keras.
  - Embedding layer
  - LSTM layer
  - Dense layer with sigmoid activation
- **Compilation:** Compiled the model with `binary_crossentropy` loss and `adam` optimizer.

### Model Training and Evaluation
- **Dataset:** Split the dataset into training and testing sets.
- **Training:** Trained the model on the training set.
- **Evaluation:** Evaluated the model on the test set, achieving a promising accuracy.

### Model Deployment
- **Saving:** Saved the trained model using `pickle`.
- **Testing:** Tested the model with new messages to validate its performance.

## Future Goals
- **Integration with Messaging Apps:** Integrate this solution into various messaging platforms to enhance user security.
- **Improvement and Scalability:** Improve the model by incorporating more diverse datasets and advanced NLP techniques.
- **Real-time Analysis:** Develop a real-time monitoring system for instant feedback on chat authenticity.

