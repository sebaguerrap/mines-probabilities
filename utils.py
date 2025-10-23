import json


def load_payouts():
    with open("payouts_mines.json", "r", encoding="utf-8") as f:
        payouts = json.load(f)
    return payouts
