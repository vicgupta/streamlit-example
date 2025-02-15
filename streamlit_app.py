import streamlit as st
import openai
import pyperclip
import requests

def createImageFromPrompt(prompt):
    response = openai.Image.create(
        prompt=prompt, 
        n=3,
        model="image-alpha-001", 
        size="512x512")
    return response['data'][0]["url"]

def createTextFromPrompt(contentSelect, prompt):
        msg = []
        roleType = '''
        I want you to act as a content writer very proficient in spoken and written English.
        Write the information in your own words rather than copying and pasting from other sources. The content must be plagiarism free and unique.
        Write the content in a formal and conversational style as if it were written by a human using the "we" form.
        The content should be detailed, rich and comprehensive.
        Do not repeat or remind me what I asked you for.  Do not apologize. Do not self-reference. Do now use generic filler phrases.
        Get to the point precisely and accurately without explaining to me what and why.
        '''
        role = {"role": "system", "content": roleType}
        msg.append(role)

        msg.append({"role": "user", "content": 'Create ' + contentSelect + ' on ' + prompt})
        completions = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=msg
        )
        response = completions.choices[0].message.content
        msg.append({"role": "assistant", "content": response})
        return response

api_key = st.text_input ("Enter the API Key", type="password")
contentSelect = st.selectbox('Select one to create:', ['A tweet of at least 140 words with hashtags',
                                                       'A paragraph of at least 200 words', 
                                                       'A blog post of at least 1000 words', 
                                                       'An article of at least 2000 words', 
                                                       'An outline with at least 10 bullet points'])
#ai code programmer
prompt = st.text_input ("Enter the subject or heading:")
submit_btn = st.button("Submit")
cancel_btn = st.button("Cancel")

if cancel_btn:
    st.write("")
elif submit_btn:
    if api_key:
        openai.api_key = api_key
        response = createTextFromPrompt(contentSelect, prompt)
        st.write(response)
    else:
        st.write("No API Key")


