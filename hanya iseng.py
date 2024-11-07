ayang = {
        "nama": "Suci Aulia Ramadhani",
        "umur": 17,
        "gender": "wanita cantik",
        "betina": True,
        "hobi": ["marah marah", "cemberut", "makan", "tidur"]}

ayang.update({"umur":18})
ayang.update({"tingkah":["sangat sangat menggemaskan"]})
ayang.pop("betina")
print(ayang)