class SimpleClassifier:
    def predict(self, text: str):
        if any(word in text.lower() for word in ["good", "great", "excellent"]):
            return "positive"
        elif any(word in text.lower() for word in ["bad", "terrible", "poor"]):
            return "negative"
        return "neutral"

model = SimpleClassifier()