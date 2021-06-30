#import packages 
from plyer import notification


#specify the parameters 
title="Hello Good Morning"



#specify the task
message="Complete the internship task for today!" 


#Formulating the code
notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)

