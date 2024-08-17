from transformers import pipeline

# Create a pipeline for summarization
summarizer = pipeline("summarization", model="t5-small")
# summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
# Save the model and tokenizer to a local directory
# model_dir = "./app/models/sshleifer/distilbart-cnn-12-6"
model_dir = "./models/t5-small"
summarizer.save_pretrained(model_dir)


from sentence_transformers import SentenceTransformer

# Define the local directory to store the model
local_model_path = './models/paraphrase-MiniLM-L6-v2'

# Create a model object
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Save the model to the local path
model.save(local_model_path)

print(f"Model saved to {local_model_path}")
