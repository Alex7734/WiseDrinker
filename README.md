DISCLAIMER !!! THIS APP SHOULD BE USED ONLY FOR ENTERTAINMENT PURPOSES I AM NOT A RESEARCHER!

HOW TO DOWNLOAD AND USE THE APP

DOWNLOAD
1. Clone and run pip install -r requirements.txt (there are 2 extra libraries there for running this on Heroku as well sorry for that).
2. Run python manage.py runserver and go to localhost port 8000 and there is your app!

USE
1. Chose the measurement unit.
2. Complete the form with details (the values are stored in sessions so as long as you are using the app it won't ask for any info again.
3. You will be faced with the main page where you can add drinks, reset your BAC, time since last drink(maybe it passed and you are still in the same session), and reset credentials.
4. When you entered your time since the first drink and all the credentials at step two in the backend I already calculated what BAC you dropped from the first drink up to this point so that is why you have to add drinks to make it change. REMEMBER!!! This means that even when you add drinks you don't need to get immediate change in your BAC as it will be listed as normal ~ 0 as long as it is less than 0 or equal to. Status changes as BAC increases on criteria taken from studies. 
5. Drink wisely!

The sources that I used to calculate the BAC were from boozelib which creator used actual research and biology to determine it! This doesn't mean the app is 100% safe to use!
I chose Django for this project as it is a great tool for building any kind of Website or Webapp and what other better way to use something rather than through the web?

Thanks for coming by,
    Alex
