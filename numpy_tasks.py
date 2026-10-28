import numpy as np

#1
def sum_prod(matrices, vectors):
  return np.sum(matrices @ vectors, axis=0)
#2
def binarize(M, threshold):
  return (M > threshold).astype(int)
#3
def unique_rows(M):
  return [np.unique(row) for row in M]

def unique_columns(M):
  return [np.unique(col) for col in M.T]
#5
def chess(m, n, a, b):
  row_indices = np.arange(m)[:, None]
  col_indices = np.arange(n)
  mask = (row_indices + col_indices) % 2
  result = np.where(mask == 0, a, b)
  return result
#6
def draw_rectangle(m, n, width, height, bg_color, rect_color):
  img = np.full((m, n, 3), bg_color, dtype=np.uint8)

  x0, y0 = n // 2, m // 2  # центр изображения
  xmin = max(0, x0 - width // 2)
  xmax = min(n, x0 + width // 2)
  ymin = max(0, y0 - height // 2)
  ymax = min(m, y0 + height // 2)

  img[ymin:ymax, xmin:xmax] = rect_color
  return img
def draw_ellipse(m, n, a, b, bg_color, ellipse_color):
  img = np.full((m, n, 3), bg_color, dtype=np.uint8)

  y0, x0 = m / 2.0, n / 2.0
  y, x = np.ogrid[:m, :n]
  mask = ((x - x0) ** 2 / (a ** 2)) + ((y - y0) ** 2 / (b ** 2)) <= 1

  img[mask] = ellipse_color
  return img

#7
class TimeSeriesStatistics:
    def __init__(self, mean, variance, std_dev, max_indices, min_indices, moving_average):
        self.mean = mean
        self.variance = variance
        self.std_dev = std_dev
        self.max_indices = max_indices
        self.min_indices = min_indices
        self.moving_average = moving_average
def analyze_time_series(data, window_size=3):
    mean_value = np.mean(data)
    variance_value = np.var(data)
    std_dev_value = np.std(data)

    n = len(data)
    max_indices = []
    min_indices = []

    for i in range(1, n - 1):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            max_indices.append(i)
        elif data[i] < data[i - 1] and data[i] < data[i + 1]:
            min_indices.append(i)

    padded_data = np.pad(data, (window_size // 2, window_size // 2), mode='edge')
    conv_result = np.convolve(padded_data, np.ones(window_size), mode='valid') / window_size

    return TimeSeriesStatistics(
        mean=mean_value,
        variance=variance_value,
        std_dev=std_dev_value,
        max_indices=np.array(max_indices),
        min_indices=np.array(min_indices),
        moving_average=conv_result[:n]
    )

#8
def one_hot(labels, class_count=None):
    if class_count is None:
        class_count = int(np.max(labels)) + 1
    result = np.zeros((labels.size, class_count))
    result[np.arange(len(labels)), labels.astype(int)] = 1
    return result