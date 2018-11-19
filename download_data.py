import urllib.request
from pathlib import Path


def download(url, file):
    if Path(file).exists():
        print(f"{file} already exists")
    else:
        print(f"Downloading {file}")
        Path(file).parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, file)


print("Topic 1")
print("Manually download from Kaggle: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv")

print("\nTopic 2")
download("http://stat-computing.org/dataexpo/2009/2008.csv.bz2", "topic-2/data/2008.csv.bz2")

print("\nTopic 3")
download("https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/mlbootcamp5_train.csv", "topic-3/data/mlbootcamp5_train.csv")

print("\nTopic 4")
print("Manually download from Kaggle: https://www.kaggle.com/c/catch-me-if-you-can-intruder-detection-through-webpage-session-tracking2/data")


print("\nTopic 5")
download("https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/credit_scoring_sample.csv", "topic-5/data/credit_scoring_sample.csv")
print("Manually download: https://d.pr/f/W0HpZh")

print("\nTopic 6")
print("Manually download from Kaggle: https://www.kaggle.com/c/how-good-is-your-medium-article/data")
