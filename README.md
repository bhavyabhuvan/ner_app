# Named Entity Recognition (NER) using spaCy

## 🔍 Project Overview

This project implements a Named Entity Recognition (NER) pipeline using the spaCy library. NER is an NLP technique used to locate and classify named entities in text into predefined categories such as person names, organizations, locations, dates, etc.

## 🧠 Features

- Extract named entities from text
- Display entity labels and values
- Support for English language using spaCy's pretrained model (`en_core_web_sm`)
- Easily extendable for custom models and domains

## 🛠 Tech Stack

- Python 3.8+
- spaCy


## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/ner-project.git
cd ner-project
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python run.py

