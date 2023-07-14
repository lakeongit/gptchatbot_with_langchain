# Import required libraries  
import streamlit as st  
import openai  
import langchain  
  
# Set up OpenAI API key  
openai.api_key = "YOUR_OPENAI_API_KEY"  
  
# Set up LangChain API key  
langchain_api_key = "YOUR_LANGCHAIN_API_KEY"  
langchain_client = langchain.Client(langchain_api_key)  
  
# Define chatbot function  
def chatbot(prompt, model, lang="en"):  
    # Generate response using OpenAI  
    response = openai.Completion.create(  
        engine=model,  
        prompt=prompt,  
        max_tokens=1024,  
        n=1,  
        stop=None,  
        temperature=0.7,  
    )  
    # Get text from OpenAI response  
    text = response.choices[0].text.strip()  
    # Translate text to specified language using LangChain  
    translated_text = langchain_client.translate(text, source="en", target=lang)  
    # Return translated text  
    return translated_text  
  
# Create Streamlit app  
def app():  
    # Set app title and description  
    st.set_page_config(page_title="Chatbot Demo", page_icon=":robot_face:", layout="wide")  
    st.title("Chatbot Demo")  
    st.write("This is a simple demo of a chatbot that integrates with LangChain.")  
      
    # Get user input  
    prompt = st.text_input("User: ", "")  
      
    # Generate chatbot response  
    if prompt:  
        response = chatbot(prompt, "davinci")  
        st.text_area("Chatbot: ", value=response, height=200)  
          
# Run Streamlit app  
if __name__ == "__main__":  
    app()  
