import json

from langchain_ollama import ChatOllama


class Bond:
    def __init__(self, model="llama3.2:1b", config=None, structured=False):
        self.model = ChatOllama(model=model, temperature=0, format="json")

    def __str__(self):
        return f"Bond({self.model})"

    def ask(self, prompt):
        return json.loads(self.model.invoke(prompt.get()).content)


if __name__ == "__main__"
    idea = """Data Science is a multidisciplinary field that combines various techniques, algorithms, and systems to extract insights and knowledge from structured and unstructured data. It involves a blend of mathematics, statistics, computer science, and domain expertise to analyze and interpret complex data.
                At its core, data science includes several key processes:
                Data Collection: Gathering raw data from various sources such as databases, online platforms, sensors, or other technologies.
                Data Cleaning: Removing or correcting inaccuracies, inconsistencies, or missing values in the data to ensure reliability and accuracy.
                Data Analysis: Applying statistical techniques and algorithms to identify patterns, correlations, and trends in the data. This step often involves machine learning models, which enable systems to learn from data and make predictions.
                Data Visualization: Representing data in a visual format such as charts, graphs, or dashboards to make it easier to understand and communicate findings to stakeholders.
                Modeling and Prediction: Creating models that can predict outcomes or make decisions based on input data. This involves using techniques like regression analysis, classification, or clustering.
                Deployment: Implementing the data science model into a real-world application where it can provide actionable insights or automation.
                Data science is applied in various fields, including healthcare, finance, marketing, and technology, to solve complex problems, drive innovation, and make data-driven decisions."""
    format = {
        "point1": {
            "title": "***point1_title***",
            "description": "***point1_description***"
        },
        "point2": {
            "title": "***point2_title***",
            "description": "***point2_description***"
        },
        "point3": {
            "title": "***point3_title***",
            "description": "***point3_description***"
        },
        "point4": {
            "title": "***point4_title***",
            "description": "***point4_description***"
        },
        "point5": {
            "title": "***point5_title***",
            "description": "***point5_description***"
        }
    }

    from .prompt import Prompt

    prompt = Prompt(idea, format)

    bond = Bond()

    response = bond.ask(prompt)
