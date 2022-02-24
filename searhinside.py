import speech_recognition as sr
import urllib
import urllib.request
import re




page = urllib.request.urlopen("https://mail.google.com/mail/u/0/?ogbl").read().decode("utf-8") 



def find_words(text, search):
    """Find exact words"""
    dText   = text.split()
    dSearch = search.split()

    found_word = 0

    for text_word in dText:
        for search_word in dSearch:
            if search_word == text_word:
                found_word += 1

    if found_word == len(dSearch):
        return lenSearch
    else:
        return False



r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something: ")
    audio = r.listen(source)



flag = False


try:
    print("you said: " + r.recognize_google(audio,))



    flag = True



except sr.UnknownValueError:
    print("error")
except sr.RequestError as e:
    print("error; {0}".format(e))



if flag:
	re.findall(r.recognize_google(audio), page)
	page.find(r.recognize_google(audio))
	print(page)
	print(find_words(page,r.recognize_google(audio)))



else:
	print("error")
	
		

	

		
