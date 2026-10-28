import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


class BrainDataInput:
    def __init__(self, path: str):
        self.path = path


class BrainCorrelationSummary:
    def __init__(self, male_correlations: dict, female_correlations: dict,
                 strongest_mri_feature: str):
        self.male_correlations = male_correlations      # dict: feature -> corr
        self.female_correlations = female_correlations  # dict: feature -> corr
        self.strongest_mri_feature = strongest_mri_feature  # str


def analyze_brain_correlations(brain_input: BrainDataInput) -> BrainCorrelationSummary:
    df = pd.read_csv(brain_input.path, sep='\t', na_values='NA')

    gender_col = 'Gender' if 'Gender' in df.columns else 'Sex'

    males = df[df[gender_col].str.strip().str.lower() == 'male']
    females = df[df[gender_col].str.strip().str.lower() == 'female']

    features = ['FSIQ', 'VIQ', 'PIQ', 'Weight', 'Height']
    target = 'MRI_Count'

    male_correlations = {}
    female_correlations = {}

    for feat in features:
        male_corr = males[feat].corr(males[target])
        female_corr = females[feat].corr(females[target])
        male_correlations[feat] = float(male_corr)
        female_correlations[feat] = float(female_corr)

    all_correlations = {}
    for feat in features:
        all_correlations[feat] = max(
            abs(male_correlations[feat]),
            abs(female_correlations[feat])
        )

    strongest_mri_feature = max(all_correlations, key=all_correlations.get)

    fig, axes = plt.subplots(2, 5, figsize=(20, 8))
    for i, feat in enumerate(features):
        axes[0, i].scatter(males[feat], males[target], alpha=0.5, label='Male')
        axes[0, i].set_title(f'Male: {feat} vs MRI_Count')
        axes[1, i].scatter(females[feat], females[target], alpha=0.5, color='red', label='Female')
        axes[1, i].set_title(f'Female: {feat} vs MRI_Count')
    plt.tight_layout()
    plt.show()

    corr_df = pd.DataFrame({
        'Male': male_correlations,
        'Female': female_correlations
    }).T
    plt.figure(figsize=(8, 4))
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Pearson correlations with MRI_Count')
    plt.tight_layout()
    plt.show()

    return BrainCorrelationSummary(
        male_correlations=male_correlations,
        female_correlations=female_correlations,
        strongest_mri_feature=strongest_mri_feature,
    )

brain_input = BrainDataInput(path="brainsize.txt")

result = analyze_brain_correlations(brain_input)

print("=== Корреляции для мужчин ===")
for feature, corr in result.male_correlations.items():
    print(f"  {feature} vs MRI_Count: {corr:.4f}")

print("\n=== Корреляции для женщин ===")
for feature, corr in result.female_correlations.items():
    print(f"  {feature} vs MRI_Count: {corr:.4f}")

print(f"\nПризнак с максимальной корреляцией с MRI_Count: {result.strongest_mri_feature}")