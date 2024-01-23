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
  
You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html) and to deploy trained model [PyCharm Professional](https://www.jetbrains.com/pycharm/download/?section=windows) is necessary.

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python. 

### Code

Template code is provided in the `emotion-detection-nlp-project.ipnyb` notebook file. You will also require to use 3 csv file datasets in `emotion-detection-nlp-project/data` folder named `happiness.csv`, `angriness.csv` and `sadness.csv`.

### Run

In a terminal or command window, navigate to the top-level directory `emotion_detection_nlp_project/` (that contains this README) and run one of the following commands:

```bash
ipython notebook boston_housing.ipynb
```  
or
```bash
jupyter notebook boston_housing.ipynb
```
or open with Juoyter Lab
```bash
jupyter lab
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The Data used in the project consist of 3 csv files for happy, sad and angry text reviews from people.

**Features**
1.  `content`: Contains actual review from people in text format
  
**Target Variable**
1. `intensity`: Contains 3 different sentiments such as happiness, sadness, angriness

### Model Deployment

Deployment of model needs `PyCharm Professional`, `Anaconda Navigator` and `Anaconda Prompt`

- Open `PyCharm` and start new project by clicking on `New Project`
- For setting of environment for project select `conda` as it will run project in Anaconda and select appropriate location for project storage.
- Create a new directory in project by right clicking on project name New-> Directory give it name as model.
- When model directory is created copy `Emotion_intensity_SVM.pkl` pickle file provided in model folder of this project in github repository.
- Create new python file in project by right clicking on project name New-> Python File give it name main.py
- Now copy code given in main.py file of this project in github repository.
- When running the main.py file you will need to change pickle file path in `pipe_clf` and copy the path of pickle file in your local machine. Put `r` before pathname if there is error while running code eg r"pathname".
- After successful execution of code you will get message saying o view this Streamlit app on a browser, run it with the following
  command: `streamlit run C:\Users\ksank\OneDrive\Desktop\Emotion-detection-NLP-project\emotion-detection-nlp-project\main.py` this will be different in your case.
- Copy this command and paste it in `Anaconda prompt` and press enter.
- This will open the streamlit app where you can enter text and get prediction for sentiment contained in it. 
