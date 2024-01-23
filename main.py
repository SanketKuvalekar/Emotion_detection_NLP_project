import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import joblib

pipe_clf = joblib.load(open("models/Emotion_intensity_SVM.pkl", "rb"))

emotions_emoji_dict = {"angriness": "😠", "happiness": "😀", "sadness": "😞"}


def predict_emotion(text):
    result = pipe_clf.predict([text])
    return result[0]


def get_prediction_prob(text):
    result = pipe_clf.predict_proba([text])
    return result


def main():
    st.title("Text_Emotion_Detector")
    st.subheader("Detection of emotion in text")

    with st.form(key="my_form"):
        raw_text = st.text_area("Enter your text to be analyzed")
        submit_text = st.form_submit_button(label="Submit")

    if submit_text:
        col1, col2 = st.columns(2)

        prediction = predict_emotion(raw_text)
        probability = get_prediction_prob(raw_text)

        with col1:
            st.success("Original Text")
            st.write(raw_text)

            st.success("Prediction")
            emoji_icon = emotions_emoji_dict[prediction]
            st.write("{}:{}".format(prediction, emoji_icon))
            st.write("Confidence: {}".format(np.max(probability)))

        with col2:
            st.success("Prediction Probability")
            # st.write(probability)
            prob_df = pd.DataFrame(probability, columns=pipe_clf.classes_)
            # st.write(prob_df.T)
            prob_df_clean = prob_df.T.reset_index()
            prob_df_clean.columns = ["emotions", "probability"]

            fig = alt.Chart(prob_df_clean).mark_bar().encode(x="emotions", y="probability", color="emotions")
            st.altair_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
