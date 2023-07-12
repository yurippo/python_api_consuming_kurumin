from datetime import datetime, timedelta

class DatesBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self):
        return self.formatted_date()
 
 #in this class we worked with dates What are the main Python libraries we use we used the libray and it's methods to create our
 #own methods to return to portuguese speakers a date for example using a bultin method of python
        
    def month_cadastro(self):
        
        months_of_year = [
            "January", "February","March",
            "April","May","June","July",
            "August","September","October","November","December"
        ]
                     
        month_cadastro = self.momento_cadastro.month -1 #I used -1 to fix the index problem on my list
        return months_of_year[month_cadastro]
    
    def day_cadastro(self):
        
        days_of_week = [
            "Sunday","Monday","Tuesday",
            "Wednesday","Thursday","Friday",
            "Saturday","Sunday"
        ]
        
        day_cadastro = self.momento_cadastro.weekday() +1
        return days_of_week[day_cadastro]
    
    
    def formatted_date(self):
        formatted_date = self.momento_cadastro.strftime("%d/%m/%Y %H:%M") #To Format Date To Brazil's Style
        return formatted_date
    
    def time_cadastro(self):
        time_cadastro = datetime.today() + timedelta(days=30) - self.momento_cadastro
        return time_cadastro