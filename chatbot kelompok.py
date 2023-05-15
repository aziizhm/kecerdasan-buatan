import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of input and output for the chatbot
pairs = [
    ["hi|hai|hello|hey", ["Hello!", "Hai!"]],
    ["siapa nama kamu", ["Nama saya Chatbot.", "saya Chatbot."]],
    ["apa kabar?", ["sangat baik.", "baik-baik saja"]],
    ["apakah kamu tau unpam?", ["Ya aku tau, Univeristas Pamulang  merupakan perguruan tinggi swasta (PTS) "]],
    ["dimana lokasi unpam?", ["Terletak di Jl Surya Kencana No 1 Pamulang, Kota Tangerang Selatan."]],
    ["bye|dadah", ["Goodbye!", "Senang berbicara denganmu."]]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Run the chatbot
print("Hello! Saya ChatBot, Ada yang bisa dibantu?")
chatbot.converse()