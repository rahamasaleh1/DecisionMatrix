# Decision Matrix

A simple Streamlit app I built to decide which feature a product should build first.

**[Try the live app](https://pantrypal-matrix.streamlit.app/)**

The example product is **PantryPal**, a food app that helps people waste less. The app compares five possible features and ranks them using a weighted decision matrix.

## How it works

Each feature is scored from 1 (weak) to 5 (strong) against five criteria. Each criterion has a weight based on how much it matters:

| Criterion | Weight |
|---|---|
| User impact | 30% |
| Less waste | 25% |
| Ease to build | 20% |
| Revenue | 15% |
| Confidence | 10% |

The app multiplies each score by its weight, adds them up and ranks the features on a scoreboard. The top feature is shown as the one to build first.

You can edit the scores in the table and the ranking updates straight away.

## Features compared

- Expiry alerts
- Receipt scanning
- Recipe ideas
- Shared shopping list
- Barcode scanner

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Built with

- Python
- Streamlit
- pandas

## Why I made it

I am studying product management and wanted to turn a prioritisation method into something interactive. A decision matrix makes trade offs visible, so the choice of what to build first is based on clear criteria rather than gut feeling.
