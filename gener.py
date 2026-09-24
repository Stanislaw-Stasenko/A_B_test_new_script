import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n = 2000
dates = [datetime(2026, 8, 1) + timedelta(days=i) for i in range(14)]
dates = np.random.choice(dates, n)

# Группы: 50/50
group = np.random.choice(['A', 'B'], n, p=[0.5, 0.5])

# FCR: в группе B выше на 6 процентных пунктов (с учётом шума)
fcr_base = np.where(group == 'A', 0.62, 0.68)
fcr = np.random.binomial(1, fcr_base)

# AHT: в группе B ниже на 15 секунд (с учётом шума)
aht_base = np.where(group == 'A', 310, 295)
aht = aht_base + np.random.normal(0, 35, n)
aht = np.round(np.maximum(aht, 120), 0)

# Дополнительные факторы (чтобы потом искать скрытые влияния)
hour = np.random.randint(8, 22, n)
operator_experience = np.random.choice(['junior', 'middle', 'senior'], n, p=[0.3, 0.4, 0.3])

df = pd.DataFrame({
    'date': dates,
    'hour': hour,
    'group': group,
    'operator_experience': operator_experience,
    'fcr': fcr,
    'aht_sec': aht,
    'day_of_week': [d.weekday() for d in dates]
})

df.to_csv('ab_test_results.csv', index=False)
print("Файл ab_test_results.csv создан. 2000 записей.")