# Charans LLM

Simple Streamlit app with a Gemini API input and response.

## Streamlit Cloud Secrets

In **Manage app → Settings → Secrets**, add:

```toml
GEMINI_API_KEY = "YOUR_NEW_API_KEY_HERE"
```

Do NOT put the real API key in `app.py` or commit it to GitHub.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model

The app uses:

`gemini-3.6-flash`
