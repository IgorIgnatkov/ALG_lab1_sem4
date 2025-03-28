import math
from collections import Counter

def calculate_entropy(input_data: bytes) -> float:
    if not input_data:
        return 0.0

    frequency = Counter(input_data)
    total_bytes = len(input_data)

    entropy_value = -sum(
        (count / total_bytes) * math.log2(count / total_bytes)
        for count in frequency.values()
    )

    return entropy_value
