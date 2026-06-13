
import joblib
import numpy as np
import pandas as pd

# ── LOAD MODELS ──────────────────────────────────────────────
model  = joblib.load("models/birthorder_model_region.pkl")
scaler = joblib.load("models/birthorder_scaler_region.pkl")

# ── REGION MAPPING ───────────────────────────────────────────
REGION_MAP = {
    'US': 'north_america', 'CA': 'north_america', 'MX': 'north_america',
    'GB': 'europe', 'DE': 'europe', 'FR': 'europe', 'SE': 'europe',
    'DK': 'europe', 'NL': 'europe', 'NO': 'europe', 'FI': 'europe',
    'BE': 'europe', 'CH': 'europe', 'AT': 'europe', 'IE': 'europe',
    'IT': 'europe', 'ES': 'europe', 'PT': 'europe', 'PL': 'europe',
    'CZ': 'europe', 'HU': 'europe', 'RO': 'europe', 'GR': 'europe',
    'IN': 'asia', 'MY': 'asia', 'PH': 'asia', 'ID': 'asia',
    'SG': 'asia', 'PK': 'asia', 'BD': 'asia', 'LK': 'asia',
    'CN': 'asia', 'JP': 'asia', 'KR': 'asia', 'TH': 'asia',
    'VN': 'asia', 'HK': 'asia', 'TW': 'asia',
    'AU': 'oceania', 'NZ': 'oceania',
    'BR': 'latin_america', 'AR': 'latin_america', 'CL': 'latin_america',
    'CO': 'latin_america', 'PE': 'latin_america', 'VE': 'latin_america',
    'ZA': 'africa', 'NG': 'africa', 'KE': 'africa', 'GH': 'africa', 'EG': 'africa',
}

# regions model is trained on
REGION_COLS = [
    'region_asia', 'region_europe', 'region_latin_america',
    'region_north_america', 'region_oceania', 'region_other'
]

Q_COLS    = [f"Q{i}" for i in range(1, 26)]
BIG5_COLS = [f"{t}{i}" for t in ["EXT","EST","AGR","CSN","OPN"] for i in range(1, 11)]

# ── REVERSE SCORING ──────────────────────────────────────────
NEGATIVE_Qs = [f"Q{i}" for i in range(21, 26)]

def predict(answers: dict, country: str) -> dict:
    """
    answers: dict of {question_id: score} e.g. {"Q1": 4, "Q2": 3, ...}
    country: country code string e.g. "US"
    returns: dict with prediction and confidence
    """

    # ── 1. BUILD FEATURE ROW ─────────────────────────────────
    row = {}

    # Q1-Q25
    for q in Q_COLS:
        val = int(answers.get(q, 3))      # default to 3 if missing
        if q in NEGATIVE_Qs:
            val = 6 - val                 # reverse score
        row[q] = val

    # Big Five
    for q in BIG5_COLS:
        row[q] = int(answers.get(q, 3))

    # ── 2. REGION ONE-HOT ────────────────────────────────────
    region = REGION_MAP.get(country.upper(), 'other')
    for col in REGION_COLS:
        row[col] = 0
    region_col = f"region_{region}"
    if region_col in REGION_COLS:
        row[region_col] = 1

    # ── 3. ASSEMBLE + SCALE ──────────────────────────────────
    feature_cols = Q_COLS + BIG5_COLS + REGION_COLS
    X = np.array([[row[col] for col in feature_cols]])
    X_scaled = scaler.transform(X)

    # ── 4. PREDICT ───────────────────────────────────────────
    prediction    = model.predict(X_scaled)[0]
    probabilities = model.predict_proba(X_scaled)[0]
    confidence    = round(float(max(probabilities)) * 100, 1)

    label = "firstborn" if prediction == 1 else "later-born"

    return {
        "prediction": label,
        "confidence": confidence,
        "firstborn_probability":  round(float(probabilities[1]) * 100, 1),
        "laterborn_probability":  round(float(probabilities[0]) * 100, 1),
    }