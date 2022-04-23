import streamlit as st
import time
from utils.get_nlp import get_ans
from utils.wikipedia import get_summary
from utils.summarization import get_summary_text,get_chunks

st.title("NLP Web Application")

def start_paraphrasing():
    try:
        option = st.sidebar.radio("Choose an option", ["Keyword", "Write own text","Blog or News Article"])
        if option == "Keyword":
            keyword = st.sidebar.text_input("Enter a keyword")
            summary = get_summary(keyword)
            st.write(summary)
        elif option == "Blog or News Article":
            url = st.sidebar.text_input("Paste the URL of the Blog or News Article")
            summary=get_chunks(url)
            sumc = ' '.join(summary)
            st.write(sumc)
        elif option == "Write own text":
            summary = st.sidebar.text_area("Write your own text",height=200)
            st.write(summary)
        question = st.text_input("Enter your question")
        start_time = time.time()
        answer = get_ans(question, summary)
        end_time = time.time()
        st.write(answer)
        st.write("Time taken: {} seconds".format(end_time-start_time))
    except KeyError as e:
        pass
    except ValueError as e:
        pass
    except Exception as e:
        st.write(e)
def start_summarization():
    try:
        option = st.sidebar.radio("Choose an option", ["Blog or News Article","Write own text"])
        if option == "Blog or News Article":
            url = st.sidebar.text_input("Paste the URL of the Blog or News Article")
            summary=get_chunks(url)
            sumc = ' '.join(summary)
            st.write(sumc)
        elif option == "Write own text":
            summary = st.sidebar.text_area("Write your own text",height=200)
            st.write(summary)
        start_time = time.time()
        answer = get_summary_text(summary)
        end_time = time.time()
        answer = ' '.join([summ['summary_text'] for summ in answer])
        st.write(answer)
        st.write("Time taken: {} seconds".format(end_time-start_time))
        st.write(answer)
        st.write("Time taken: {} seconds".format(end_time-start_time))
    except KeyError as e:
        pass
    except ValueError as e:
        pass
    except Exception as e:
        st.write(e)

func = st.selectbox("Choose a function", ["Paraphrasing", "Summarization"])
if func == "Paraphrasing":
    start_paraphrasing()
elif func == "Summarization":
    start_summarization()

