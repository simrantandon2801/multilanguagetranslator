import streamlit as st     #it is a library used to develop web app using python like Flask.

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator      #it is library which is used to import ibm cloud services

from ibm_watson import LanguageTranslatorV3        #here we import language translate

from textblob import TextBlob             # for processing textual data

#emoji
import emoji    #for inserting emoji



def main():
            """Sentiment Analysis Emoji App """

            st.title("Language Translator and Sentiment Analysis")

            activities = ["translator", "Sentiment", "About"]
            choice = st.sidebar.selectbox("Choice", activities)


            if choice == 'translator':
            # key information for language translator service
               api_key = 'mgoyPQIeStPtQSK1pX5R_fJeOGUz9WAKG8mU72150g7b'
               url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d8058fa3-d68f-4946-b4fd-d9561633bdb9'

            # we connect the api in this code

               authenticator = IAMAuthenticator(apikey=api_key)
               langtranslator = LanguageTranslatorV3(version='2020-02-01', authenticator=authenticator)
               langtranslator.set_service_url(url)
               st.title("language Translator ")                                       # title of the page

               option = st.selectbox('which language would you choose to type',
                                  ('English', 'Arabic', 'Hindi', 'German', 'Spanish',
                                   'Korean'))                                         # used for selection box1

               option1 = st.selectbox('which language would you like to translate to',
                                   ('English', 'Arabic', 'Hindi', 'German', 'Spanish',
                                    'Korean'))                                           # used for selection box2

               sent = "Enter the text in " + option + " language in the text-area provided below"  # selected langauge

               language_lib = {'English': 'en', 'Arabic': 'ar', 'Hindi': 'hi', 'Spanish': 'es', 'German': 'de',
                            'korean': 'ko'}  # used for language which can be convert using ibm cloud
               sentence = st.text_area(sent, height=250)  # text area



               if st.button("Translate"):                                            # translate button

                 try:

                    if option == option1:  # if language was not selected
                        st.write("PLease Select different Language For translation")
                    else:
                        translate_code = language_lib[option] + '-' + language_lib[option1]
                        translation = langtranslator.translate(
                            text=sentence, model_id=translate_code
                        )
                        ans = translation.get_result()['translations'][0]['translation']
                        sent1 = 'Translated text in' '+option1+' 'language is shown below'
                        st.markdown(sent1)
                        st.write(ans)
                 except:
                        st.write(
                        "please do cross check if text-area is filled with sentence or not")  # if we left blank in the sentence area it work



            if choice == 'Sentiment':                                       #for sentiment analysis
                st.subheader("Sentiment Analysis")                          #subheading
                             #for emoji
                raw_text = st.text_area("Enter Your Text", "Type Here")                                   #for inserting text
                if st.button("Analyze"):
                    blob = TextBlob(raw_text)
                    result = blob.sentiment.polarity
                    if result > 0.0:                                              # if the senetence is positive it will show score =+0.0
                        custom_emoji = ':smile:'
                        st.write(emoji.emojize(custom_emoji, use_aliases=True))
                    elif result < 0.0:                                            #if the senetence is negative it will show score =-0.0
                        custom_emoji = ':disappointed:'
                        st.write(emoji.emojize(custom_emoji, use_aliases=True))
                    else:
                        st.write(emoji.emojize(':expressionless:', use_aliases=True))
                    st.info("Polarity Score is:: {}".format(result))



            if choice == 'About':                                                     #about:
                st.subheader("About:Sentiment Analysis Emoji App")
                st.info("Built with Streamlit,Textblob and Emoji")
                st.text("Project by ")
                st.text("Sakshi Dwivedi(19020004072)")
                st.text("Simran (19020004078)")


if __name__ == '__main__':
    main()