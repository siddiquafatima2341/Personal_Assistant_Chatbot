# Personal Assistant Chatbot

A simple rule-based personal assistant chatbot built with **Python**, **JSON**, and **Streamlit**.

## Features

- Chat-style interface in the browser
- Responses driven by a JSON knowledge base (easy to edit, no code changes needed)
- Matches exact phrases first, then falls back to keyword matching
- Clear chat button in the sidebar

## Project structure

```
personal-assistant-chatbot/
├── app.py              # Streamlit app (UI + matching logic)
├── responses.json       # Knowledge base of questions and answers
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repo:
   ```
   git clone https://github.com/YOUR_USERNAME/personal-assistant-chatbot.git
   cd personal-assistant-chatbot
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python -m streamlit run app.py
   ```

   It opens at `http://localhost:8501`.

## Usage

Type a message in the chat box. Try:

- `hello`
- `what can you do`
- `help`
- `bye`

## Customizing responses

Open `responses.json` and add new key-value pairs — the key is the phrase to match, the value is the reply:

```json
{
  "your new phrase": "Your new response here"
}
```

No code changes required — just save the file and rerun the app.

## Tech stack

- Python 3
- Streamlit (chat UI)
- JSON (knowledge base / storage)
