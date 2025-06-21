def is_similar(text1: str, text2: str, threshold: float = 0.9) -> bool:
    from difflib import SequenceMatcher
    return SequenceMatcher(None, text1, text2).ratio() > threshold
