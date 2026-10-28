import pandas as pd
import numpy as np

class TitanicInput:
    def __init__(self, path: str):
        self.path = path

class TitanicSummary:
    def __init__(self, missing_counts: dict, over_30_count: int,
                 avg_age_by_class: dict, survival_rate_by_class: dict,
                 top5_fare: list):
        self.missing_counts = missing_counts
        self.over_30_count = over_30_count
        self.avg_age_by_class = avg_age_by_class
        self.survival_rate_by_class = survival_rate_by_class
        self.top5_fare = top5_fare


def analyze_titanic(titanic_input: TitanicInput) -> TitanicSummary:

    df = pd.read_csv(titanic_input.path)
    missing_counts = df.isnull().sum().to_dict()
    over_30_count = int((df['Age'] > 30).sum())

    avg_age_series = df.groupby('Pclass')['Age'].mean()

    avg_age_by_class = {int(cls): float(val) for cls, val in avg_age_series.items()}

    survival_series = df.groupby('Pclass')['Survived'].mean()
    survival_rate_by_class = {int(cls): float(val) for cls, val in survival_series.items()}

    top5_fare = df['Fare'].nlargest(5).tolist()

    return TitanicSummary(
        missing_counts=missing_counts,
        over_30_count=over_30_count,
        avg_age_by_class=avg_age_by_class,
        survival_rate_by_class=survival_rate_by_class,
        top5_fare=top5_fare,
    )

titanic_input = TitanicInput(path="titanic.csv")

result = analyze_titanic(titanic_input)

print("=== Пропуски в столбцах ===")
for col, count in result.missing_counts.items():
    print(f"  {col}: {count}")

print(f"\nПассажиров старше 30 лет: {result.over_30_count}")

print("\nСредний возраст по классам:")
for cls, age in result.avg_age_by_class.items():
    print(f"  Pclass {cls}: {age:.2f}")

print("\nДоля выживших по классам:")
for cls, rate in result.survival_rate_by_class.items():
    print(f"  Pclass {cls}: {rate:.4f} ({rate*100:.2f}%)")

print(f"\nТоп-5 значений Fare: {result.top5_fare}")