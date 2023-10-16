import matplotlib.pyplot as plt
import seaborn as sns


def show_null(dataset):
  missing_values = dataset.isnull().sum()
  num_rows, _ = dataset.shape

  plt.figure(figsize=(12, 6))
  sns.barplot(x=missing_values.values, y=missing_values.index, palette='viridis')
  plt.xlabel('Number of Missing Values')
  plt.title('Missing Values in DataFrame')
  plt.grid(axis='x', linestyle='--', alpha=0.7)
  plt.xlim(0, num_rows)

  for i, count in enumerate(missing_values):
    if(count == 0):
      continue
    plt.text(count + 10, i, str(count), va='center', fontsize=12)
  plt.show()