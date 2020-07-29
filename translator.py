from googletrans import Translator
def google_trans():#Unofficial Google Translator
    response=input("Enter the text: ")
    translator = Translator() # Create object of Translator.
    Arabic      ='ar'
    Assamese    ='as'
    Bengali     ='bn'
    Bihari      ='bh'
    Bulgarian   ='bg'
    Burmese     ='my'
    Chinese     ='zh'
    Dutch       ='nl'
    English     ='en'
    Finnish     ='fi'
    French      ='fr'
    German      ='de'
    Greek       ='el'
    Gujarati    ='gu'
    Hindi       ='hi'
    Irish       ='ga'
    Italian     ='it'
    Japanese    ='ja'
    Kannada     ='kn'
    Kashmiri    ='ks'
    Kongo       ='kg'
    Korean      ='ko'
    Latin       ='la'
    Malayalam   ='ml'
    Marathi     ='mr'
    Nepali      ='ne'
    Oriya       ='or'
    Punjabi     ='pa'
    Persian     ='fa'
    Polish      ='pl'
    Portuguese  ='pt'
    Russian     ='ru'
    Sanskrit    ='sa'
    Samoan      ='sm'
    Spanish     ='es'
    Swedish     ='sv'
    Tamil       ='ta'
    Telugu      ='te'
    Tibetan     ='bo'
    Urdu        ='ur'
    text=response
    text=text.split()
    n=len(text)
    lang=text[n-1]
    text[n-2]=''
    text[n-1]=''
    data=' '.join(text)
    translated = translator.translate(data,dest='%s'%lang)
    data=(translated.text)
    print(data)
google_trans()
