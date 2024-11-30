from collections import Counter
from decimal import Decimal, getcontext
import math

getcontext().prec = 100

text = "тевелевартёмдмитриевич"
text = text.replace(" ", "").lower()
freq = Counter(text)
total = sum(freq.values())
prob = {ch: Decimal(cnt) / Decimal(total) for ch, cnt in freq.items()}

sorted_chars = sorted(prob.keys())
cumul_prob = {}
cum = Decimal('0')
for ch in sorted_chars:
    cumul_prob[ch] = cum
    cum += prob[ch]

low, high = Decimal('0'), Decimal('1')
intervals = []

for ch in text:
    r = high - low
    high_new = low + r * (cumul_prob[ch] + prob[ch])
    low_new = low + r * cumul_prob[ch]
    intervals.append({'char': ch, 'low': low_new, 'high': high_new})
    low, high = low_new, high_new

code = math.log(1 / (high - low), 2)

print("Интервалы:")
for i, interval in enumerate(intervals):
    print(f"{i + 1}: {interval['char']} [{interval['low']:.40f}, {interval['high']:.40f}]")

power = Decimal(2) ** 72
low_scaled = low * power
scaled_result = int(low_scaled.to_integral_value(rounding='ROUND_CEILING'))
result = Decimal(scaled_result) / power

print(f"Число из итогового интервала: {result}")
binary = bin(int(result * 2**72))[2:]
print(binary)
