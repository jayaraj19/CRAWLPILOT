from app import app, db
from sentence_transformers import SentenceTransformer
from transformers import pipeline


from app import views

# Define the local directory where the model is stored
local_model_path = './models/paraphrase-MiniLM-L6-v2'

# Load the model from the local path
model = SentenceTransformer(local_model_path)

# model_dir = "app/models/sshleifer/distilbart-cnn-12-6"
model_dir = "./models/t5-small"
summarizer = pipeline("summarization", model=model_dir, tokenizer=model_dir)

if __name__ == '__main__':
    app.run(debug=True)