#filcher2011's source code

#Importing the necessary libraries
import telebot as tb
import requests as rq

#Writting token
bot = tb.TeleBot("YOUR-TOKEN")

#Create function
@bot.message_handler(commands=['start'])
def greating(message):
    bot.send_message(message.chat.id, "Welcome to IP Helper bot! Enter /getinfo to get ip's info")

#Create function
@bot.message_handler(commands=['getinfo'])
def inputInfo(message):
    msg = bot.send_message(message.chat.id, "Please, enter your IP-Address")
    bot.register_next_step_handler(msg, getipinfo)

#Create function for get ip's info
def getipinfo(message):
    try:
        ip = message.text
        url = f"https://ipinfo.io/{ip}/geo"
        ipURL = rq.get(url).json()['ip']
        cityURL = rq.get(url).json()['city']
        regionURL = rq.get(url).json()['region']
        countryURL = rq.get(url).json()['country']
        locationURL = rq.get(url).json()['loc']
        indexURL = rq.get(url).json()['postal']
        tmURL = rq.get(url).json()['timezone']
        orgURL = rq.get(url).json()['org']
        msgResult = f"The bot received the information! \nIP - {ipURL} \nCity - {cityURL} \nRegion - {regionURL} \nCountry - {countryURL} \nYour coordinates - {locationURL} \nYour index - {indexURL} \nTimezone - {tmURL} \nOrganization - {orgURL}"
        bot.reply_to(message, msgResult)
    except KeyError:
        bot.send_message(message.chat.id, "Please, enter your IP-Address!!!")

#Run bot
if __name__ == '__main__':
    bot.infinity_polling()