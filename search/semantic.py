from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticSearch:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = None

    def build(self, commands):
        corpus = [
            f"{c.command} {c.description} {c.usage}"
            for c in commands
        ]

        self.matrix = self.vectorizer.fit_transform(corpus) if corpus else None

    def search(self, query, commands):
        if not query or self.matrix is None:
            return commands

        q_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(q_vec, self.matrix)[0]

        ranked = sorted(
            zip(commands, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [cmd for cmd, score in ranked if score > 0.05]
