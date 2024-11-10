from transformers import pipeline 

# Load a pre-trained text classification pipeline 
classifier = pipeline('sentiment-analysis') 

# Classify text 
result = classifier('I love using the transformers library')

print(result)