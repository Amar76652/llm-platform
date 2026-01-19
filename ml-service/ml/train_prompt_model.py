from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

#Training data
prompts = [
    "Hi",
    "Tell me about java",
    "Explain microservice architecture",
    "Explain microservices with pros and cons and scalability",
    "Describe distributed systems in details with examples"
]

labels = [
    "LOW QUALITY",
    "LOW QUALITY",
    "MEDIUM QUALITY",
    "HIGH QUALITY",
    "HIGH QUALITY"
]

# Pipeline = vectorizer + model
pipeline = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

#Train model
pipeline.fit(prompts, labels)

#Save Model
joblib.dump(pipeline, "ml/prompt_quality_model.joblib")

print("Model trained and saved")
