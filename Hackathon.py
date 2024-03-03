from openai import OpenAI
import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()


# inputs from user
name=("Name of the student : ")
engine.say(name)
engine.runAndWait()


#sr creation
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say your name : ")
        audio=r.listen(source)

        try:
            print("Name :  \n " + r.recognize_google(audio))



        except Exception as e:
            print("Error:" + str(e))





if __name__ == "__main__":
    main()



age=("age of the student : ")
engine.say(age)
engine.runAndWait()

#sr creation
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say your age : ")
        audio=r.listen(source)

        try:
            print("Age :  \n " + r.recognize_google(audio))



        except Exception as e:
            print("Error:" + str(e))





if __name__ == "__main__":
    main()


Gender=(" Male or Female : ")
engine.say(Gender)
engine.runAndWait()


#sr creation
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say your Gender : ")
        audio=r.listen(source)

        try:
            print("Gender :  \n " + r.recognize_google(audio))



        except Exception as e:
            print("Error:" + str(e))





if __name__ == "__main__":
    main()


F_O_I=(" What is your field of interest : ")
engine.say(F_O_I)
engine.runAndWait()


#sr creation
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say your hobby : ")
        audio=r.listen(source)

        try:
            print("Hobby :  \n " + r.recognize_google(audio))



        except Exception as e:
            print("Error:" + str(e))





if __name__ == "__main__":
    main()



Dream=("Who do you want to become as , type the answer ")
engine.say(Dream)
engine.runAndWait()
drm=input("I want to become : ")


if drm == "civil engineer":
    y=("You have a wide dream , bravo!")
    engine.say(y)
    engine.runAndWait()
    z=(" You have to work really hard for it")
    engine.say(z)
    engine.runAndWait()
    ques=input(" Are you interested in making your dream a true one : ")

    if ques == "yes":
        w=(" The U will be your guidance to help you become a " + Dream)
        engine.say(w)
        engine.runAndWait()


        a=input(" Are you ready to see the future you :  ")

        if a == "yes":
            repl=("civil engineer working in building")
            response = client.images.generate(
                model="dall-e-2",
                prompt=repl,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            print(image_url)



        else:
            v=(" I am not sure I can understand that")
            engine.say(v)
            engine.runAndWait()

        x=input(" I hope you were staisfied with your future self . Do you want it to be a reality : ")
        if x=="yes":
            u=(" Oh , great , then you must connect with THE U APP  . But before that , Today's THE U suggestion is to perform well in your academic subjects of Mathematics and Physics so that you can improvise your knowledge and become a civil engineer soon . Good luck my friend ! ")
            engine.say(u)
            engine.runAndWait()
        else:
            t=(" I am not sure I can understand that")
            engine.say(t)
            engine.runAndWait()



    else:
        s=(" Ok " + name + " , Maybe you should try improvising your efforts towards acheiving your goals")
        engine.say(s)
        engine.runAndWait()

elif drm == "doctor":
    r=("You have a life saving dream , fantastic!")
    engine.say(r)
    engine.runAndWait()
    q=(" You have to put a lot of efforts for it")
    engine.say(q)
    engine.runAndWait()

    ques = input(" Are you interested in making your dream a true one : ")

    if ques == "yes":
        g=(" The U will be your guidance to help you become a " + Dream)
        engine.say(g)
        engine.runAndWait()
        a = input(" Are you ready to see the future you :  ")

        if a == "yes":
            rep = (" doctor working in a hospital ")
            response = client.images.generate(
                model="dall-e-2",
                prompt=rep,
                size="1024x1024",
                quality="standard",
                n=1,
            )

            image_url = response.data[0].url
            print(image_url)

        else:
            l=(" I am not sure I can understand that")
            engine.say(l)
            engine.runAndWait()

        x = input(" I hope you were staisfied with your future self . Do you want it to be a reality : ")
        if x == "yes":
            n=(
                " Oh , great , then you must connect with THE U APP  . But before that , Today's THE U suggestion is to perform well in your academic subjects of Biology and Chemistry so that you can improvise your knowledge and become a doctor soon . Good luck my friend !")
            engine.say(n)
            engine.runAndWait()
        else:
            p=(" I am not sure I can understand that")
            engine.say(p)
            engine.runAndWait()

    else:
        print(" Ok " + name + " , Maybe you should try improvising your efforts towards acheiving your goals")

elif drm == ("scientist"):
    i=("You have a bombastic dream , amazing!")
    engine.say(i)
    engine.runAndWait()
    j=(" You have research a lot for it")
    engine.say(j)
    engine.runAndWait()
    ques = input(" Are you interested in making your dream a true one : ")

    if ques == "yes":
        k=(" The U will be your guidance to help you become a " + Dream)
        engine.say(k)
        engine.runAndWait()
        a = input(" Are you ready to see the future you :  ")

        if a == "yes":
            repli = ("scientist working with chemicals")
            response = client.images.generate(
            model="dall-e-2",
            prompt=repli,
            size="1024x1024",
            quality="standard",
            n=1,
            )

            image_url = response.data[0].url
            print(image_url)

        else:
            m=("I am not sure I can understand that ")
            engine.say(m)
            engine.runAndWait()

        x = input(" I hope you were staisfied with your future self . Do you want it to be a reality : ")
        if x == "yes":
            o=(
                " Oh , great , then you must connect with THE U APP  . But before that , Today's THE U suggestion is to perform well in your academic subjects of Chemistry and Physics so that you can improvise your knowledge and become a scientist soon . Good luck my friend ! ")
            engine.say(o)
            engine.runAndWait()
        else:
            (" I am not sure I can understand that")


    else:
        print(" Ok " + name + " , Maybe you should try improvising your efforts towards acheiving your goals")

else:
    print("I am not sure I can understand that")
