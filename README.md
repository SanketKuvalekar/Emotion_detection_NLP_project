# Project : Emotion-detection-through-text

### Installation
   This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [seaborn](https://seaborn.pydata.org/)
- [re](https://docs.python.org/3/library/re.html)
- [string](https://docs.python.org/3/library/string.html)
- [nltk](https://www.nltk.org/)
- [joblib](https://joblib.readthedocs.io/en/stable/)
- [neattext](https://pypi.org/project/neattext/)
- [streamlit](https://pypi.org/project/streamlit/)
- [altair](https://pypi.org/project/altair/)
  
You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python. 

### Code

Template code is provided in the `emotion-detection-nlp-project.ipnyb` notebook file. You will also require to use 3 csv file datasets in `emotion-detection-nlp-project/data` folder named `happiness.csv`, `angriness.csv` and `sadness.csv`.

### Run

In a terminal or command window, navigate to the top-level directory `emotion_detection_nlp_project/` (that contains this README) and run one of the following commands:

```bash
ipython notebook emotion-detection-nlp-project.ipynb
```  
or
```bash
jupyter notebook emotion-detection-nlp-project.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

- The Data used in the project consist of 3 csv files for happy, sad and angry text reviews from people.
- You will need to copy the csv file path on your local machine and paste it during execution of `Data collection` cell in `jupyter notebook`

**Features**
1.  `content`: Contains actual review from people in text format
  
**Target Variable**
1. `intensity`: Contains 3 different sentiments such as happiness, sadness, angriness

### Model Deployment

- Model is deployed as an app using Streamlit and by using main.py file
- [Streamlit app url](https://emotiondetectionnlpproject-qriyq4vfymebhqtm6v8hgd.streamlit.app/)
- User needs to enter the text that needs to be analyzed and submit it.
- The app will the predict whether the sentiment in given text is happiness, angriness or sadness.
