#!/usr/bin/env python3.2

#MAtt was here

import time
import os
import sys
import datetime
import webbrowser

from tkinter import *
import tkinter.messagebox

__version__ = 1.01

if os.name =='nt': # if windows
    os.environ['HOME'] = os.path.join(os.environ['HOMEDRIVE'], 
                                      os.environ['HOMEPATH'])
    
dir_path = os.environ['HOME'] + os.sep + '.Quit Smoking'
full_path =  dir_path + os.sep + 'quit_smoking_details.txt'

def create_path(dir_path, full_path):
    '''create if not exists, full_path and dir_path'''
    if os.path.exists(full_path):
        return
    else:
        if os.path.isdir(dir_path):
            default = create_file(full_path)
            return default
        else:
            os.mkdir(dir_path)
            default = create_file(full_path)
            return default
       
def create_file(full_path):
    file = open(full_path, 'a')
    file.close()
    if os.stat(full_path).st_size == 0:
        #create default stats 
        time_format = time.time()
        price = 0.00
        amount = 0
        save_detail(full_path, time_format, price, amount)
        default = 'yes'
        return default
    else:
        return

def save_detail(full_path, time, price, amount):
    '''save detail to file'''
    file = open(full_path, 'w')
    file.write('time_stamp={0}\nprice={1}\namount={2}'.format(time, price, amount))
    file.close()

def view_detail(full_path, returns='no'):
    '''view detail from file'''
    #detail_list = []
    file = open(full_path, 'r')
    for line in file.readlines():
        if 'time_stamp' in line:
            num = line.find('=') + 1
            time_stamp = line[num:]
        if 'price' in line:
            num = line.find('=') + 1
            price = line[num:]
        if 'amount' in line:
            num = line.find('=') + 1
            amount = line[num:]
        #detail_list.append(line)
 
    #time_stamp = detail_list[0]
    #price = detail_list[1]
    #amount = detail_list[2]
    time_format = time.asctime(time.localtime(float(time_stamp)))
    if returns == 'return_only':
        return (time_stamp, price, amount, time_format)
       
    #print('quitdate:\t\t', time_format)
    #print('cigarettes daily:\t', amount)
    #print('pack price:\t\t', price)
   
    if returns == 'both':
        return (time_stamp, price, amount)
    
def view_stats(full_path, returns='no'):
    mysep = '-' *60
    tuples = (view_detail(full_path,returns='return_only'))
   
    time_stamp = tuples[0]
    amount = tuples[2]
    price = tuples[1]
    time_format = tuples[3]
    '''
    dt1 = datetime.datetime.fromtimestamp(time.time()) #current time
    dt2 = datetime.datetime.fromtimestamp(float(time_stamp)) #time stamp
   
    seconds = (dt1 - dt2).seconds'''
    seconds = time.time() - float(time_stamp)
    
    if returns == 'ach':
        return seconds
    
    minutes = seconds / 60 #add one minute for every 60 sec
    
    try: #catch if users input a string not a number
        float(amount)
        float(price)
    except ValueError:
        amount = 0
        price = 0
    
    
    hr_cig = float(amount) / 24
    min_cig = hr_cig /60
    total_cig = minutes * min_cig
    #print(total_cig)
    
    hr_ = 1.00 / 24
    min_ = hr_ / 60
    total_day = minutes * min_
    #print(total_day)
    
    packs = float(amount) / 20 #packs per day
    price = packs * float(price)
    hr_price = price / 24
    min_price = hr_price / 60
    total_price = minutes * min_price
    #print(total_price)
    
    hr_life = (float(amount) * 11) /24
    min_life = hr_life /60
    total_life = minutes * min_life
    #print(total_life)
    
    if returns == 'yes':
        return 'Quitdate: {0}\nDays without smoking: {1:.2f}\nCigarettes not smoked: {2:.2f}\nMoney saved: ${3:.2f}\nLife saved: {4:.2f} minutes'.format(time_format, total_day, total_cig, total_price, total_life)

def acheivements(seconds):
    achlist = []
    
    #test all
    #seconds = 622080001
    
    sepsep = ('-' * 230) + '\n'
    if seconds > 1200: #20 minutes
        ach1 = sepsep + 'ACHIEVEMENT 20 minutes: Your blood pressure, pulse rate, and the temperature of your hands and feet are returned to normal.'
        achlist.append(ach1)
    if seconds > 28800: #8 hours
        ach2 = sepsep + 'ACHIEVEMENT 8 Hours: Remaining nicotine in your bloodstream has fallen to 6.25% of normal peak daily levels, a 93.25% reduction.'
        achlist.append(ach2)
    if seconds > 43200: #12 hours
        ach3 = sepsep + 'ACHIEVEMENT 12 Hours: Your blood oxygen level has increased to normal and carbon monoxide levels has dropped to normal.'
        achlist.append(ach3)
    if seconds > 86400: #24 hours
        ach4 = sepsep + 'ACHIEVEMENT 24 Hours: Anxieties peak in intensity and within two weeks should return to near pre-cessation levels.'
        achlist.append(ach4)
    if seconds > 172800: #48 hours
        ach5 = sepsep + 'ACHIEVEMENT 48 Hours: Damaged nerve endings have started to regrow and your sense of smell and taste are beginning to return to normal. \nCessation anger and irritability peaks.'
        achlist.append(ach5)
    if seconds > 259200: #72 hours
        ach6 = sepsep + 'ACHIEVEMENT 72 Hours: Your entire body will test 100% nicotine-free and over 90% of all nicotine metabolites \n(the chemicals it breaks down into) will now have passed from your body via your urine. \n Symptoms of chemical withdrawal have peaked in intensity, including restlessness. \nThe number of cue induced crave episodes experienced during any quitting day will peak for the "average" ex-user. \nLung bronchial tubes leading to air sacs (alveoli) are beginning to relax in recovering smokers. \nBreathing is becoming easier and the lungs functional abilities are starting to increase. '
        achlist.append(ach6)
    if seconds > 432000: #5-8 days
        ach7 = sepsep + 'ACHIEVEMENT 5-8 days: The "average" ex-smoker will encounter an "average" of three cue induced crave episodes per day. \nAlthough we may not be "average" and although serious cessation time distortion can make minutes feel like hours, \nit is unlikely that any single episode will last longer than 3 minutes. Keep a clock handy and time them.'
        achlist.append(ach7)
    if seconds > 864000: #10 days
        ach8 = sepsep + 'ACHIEVEMENT 10 days: The "average ex-user is down to encountering less than two crave episodes per day, each less than 3 minutes. \n10 Days - 2 Weeks: Recovery has likely progressed to the point where your addiction is no longer doing the talking. \nBlood circulation in our gums and teeth are now similar to that of a non-user. \n10 days - 2 weeks: Recovery has likely progressed to the point where your addiction is no longer doing the talking. \nBlood circulation in our gums and teeth are now similar to that of a non-user.'
        achlist.append(ach8)
    if seconds > 1209600: #2 weeks
        ach9 = sepsep + 'ACHIEVEMENT 2-4 Weeks: Cessation related anger, anxiety, difficulty concentrating, impatience, insomnia, restlessness and depression have ended. \n21 Days: Brain acetylcholine receptor counts up-regulated in response to nicotine\'s presence have now down-regulated \nand receptor binding has returned to levels seen in the brains of non-smokers. \n2 Weeks - 3 Months: Your heart attack risk has started to drop. Your lung function is beginning to improve.'
        achlist.append(ach9)
    if seconds > 1814400:# 3 weeks
        ach10 = sepsep + 'ACHIEVEMENT 3 Weeks - 3 Months: Your circulation has substantially improved. Walking has become easier. \nYour chronic cough, if any, has likely disappeared. \n1-9 Months: Any smoking related sinus congestion, fatigue or shortness of breath have decreased. \nCilia have regrown in your lungs thereby increasing their ability to handle mucus, keep your lungs clean, and reduce infections. \nYour body\'s overall energy has increased.'
        achlist.append(ach10)
    if seconds > 31104000: #1 year
        ach11 = sepsep + 'ACHIEVEMENT 1 Year: Your excess risk of coronary heart disease, heart attack and stroke has dropped to less than half that of a smoker.'
        achlist.append(ach11)
    if seconds > 155520000: #5 years
        ach12 = sepsep + 'ACHIEVEMENT 5-15 Years: Your risk of stroke has declined to that of a non-smoker. \n10 Years: Your risk of being diagnosed with lung cancer is between 30% and 50% of that for a continuing smoker (2005 study). \nRisk of death from lung cancer has declined by almost half if you were an average smoker (one pack per day).  \nYour risk of pancreatic cancer has declined to that of a never-smoker (2011 study), \nwhile risk of cancer of the mouth, throat and esophagus has also declined. \nYour risk of developing diabetes is now similar to that of a never-smoker '
        achlist.append(ach12)
    if seconds > 404352000: #13 years
        ach13 = sepsep + 'ACHIEVEMENT 13 Years: Your risk of smoking induced tooth loss has declined to that of a never-smoker'
        achlist.append(ach13)
    if seconds > 466560000: #15 years
        ach14 = sepsep + 'ACHIEVEMENT 15 Years: Your risk of coronary heart disease is now that of a person who has never smoked. '
        achlist.append(ach14)
    if seconds > 622080000:# 20 years
        ach15 = sepsep + 'ACHIEVEMENT 20 Years: Female excess risk of death from all smoking related causes, including lung disease and cancer, \nhas now reduced to that of a never-smoker. Risk of pancreatic cancer reduced to that of a never-smoker. '
        achlist.append(ach15)
    return achlist

def set_detail_win(root, full_path):
    top = Toplevel()
    positionlevel(top, root)
    top.title('Details')
    top.minsize(300,85)
    top.maxsize(300,85)
    
    label = Label(top, text='Cigs smoked daily:\nPrice per pack:', justify='right')
    label.config(padx=10, pady=30)
    label.pack(side=LEFT)
    
    boxvalue = IntVar()
    checkbox = Checkbutton(top, variable=boxvalue, text='Reset quit date to now?')
    checkbox.pack()
    

    tuples = (view_detail(full_path,returns='both'))
    times = tuples[0]
    amount = tuples[2]
    price = tuples[1]
    
    smoked = Entry(top)
    smoked.insert(0, amount)
    smoked.pack()
    smoked.focus()
    
    packprice = Entry(top)
    packprice.insert(0, price[:-1]) #get rid of EOF
    packprice.pack()
    packprice.focus()
    
    #print('checkbox recieved is', type(boxvalue.get()))
    clock = boxvalue.get()
    new_amount = smoked.get()
    new_price = packprice.get()
    

    
    #print('old values: '+  times + amount + price)
    if clock == 1:
        times = time.time()
    
    #print('new values: '+ times + new_amount + new_price)
    
    btn = Button(top, text='Cancel', command=top.destroy)
    btn.pack(side=RIGHT)
    save_btn = Button(top, text='Save', command=lambda:format_save(full_path, top, boxvalue, smoked, packprice, times))
    save_btn.pack(side=LEFT)
    root.protocol('WM_DELETE_WINDOW', top.quit)
    top.focus_set() #take over input focus
    top.grab_set() #disable other windows while im open
    top.wait_window() #and wait here until win destroyed

def format_save(full_path, top, boxvalue, smoked, packprice, times):
    #tuples = (view_detail(full_path,returns='both'))
    #times = tuples[0]
    #amount = tuples[2]
    #price = tuples[1]
    #print('old values:' + times +' '+ price + ' ' + amount)
    #if new_time == 1:
        #times = new_time
    #price = new_price
    #amount = new_amount
    #print('old values:',tuples)
    #print('new values:' + str(times) +' '+ price + ' ' + amount)
    clock = boxvalue.get()
    if clock == 1:
        times = time.time()
    else:
        times = times
    new_amount = smoked.get()
    new_price = packprice.get()
    save_detail(full_path, times, new_price, new_amount)
    top.destroy()
    
def ach_win(root):
    top = Toplevel()
    positionlevel(top, root)
    top.title('Achievements')
    top.minsize(250,120)
    seconds = view_stats(full_path, 'ach') # return stats as string formated for label
    achlist = acheivements(seconds)
    if achlist == []:
        stats = 'You have not yet attained any Achievements.'
    else:
        #for index in achlist:
        stats = '\n'.join(achlist)
    #print('achlist is', achlist)
    display = Label(top, text=stats, justify='left')
    display.pack()
    close_btn = Button(top, text='OK', command=top.destroy)
    close_btn.pack()
    root.protocol('WM_DELETE_WINDOW', top.quit)
    top.focus_set() #take over input focus
    top.grab_set() #disable other windows while im open
    top.wait_window() #and wait here until win destroyed
        
def view_stats_win(root, default):
    top = Toplevel()
    positionlevel(top, root)
    top.title('Stats')
    top.minsize(250,120)
    stats = view_stats(full_path, 'yes') # return stats as string formated for label
    #if default == 'yes':
        #display = Label(top, text='Please "Set Details" to change the default values\n' + stats)
    #else:
    display = Label(top, text=stats, justify='left')
    display.pack()
    close_btn = Button(top, text='OK', command=top.destroy)
    close_btn.pack()
    root.protocol('WM_DELETE_WINDOW', top.quit)
    top.focus_set() #take over input focus
    top.grab_set() #disable other windows while im open
    top.wait_window() #and wait here until win destroyed
    
def view_timeline_web():
    webbrowser.open('http://whyquit.com/whyquit/a_benefits_time_table.html')
    
def positionlevel(win, root):
    win.geometry('+{0}+{1}'.format(
        root.winfo_rootx()+50, root.winfo_rooty()+50))
    
def notdone():
    print('not done yet')
    
default = create_path(dir_path, full_path)
    
root = Tk()
root.title('Quit Smoking')
root.minsize(200, 200)



menubar = Menu(root)
menubar.config(background='white')
filemenu = Menu(menubar,tearoff=0)

filemenu.add_separator()

filemenu.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)

#helpmenu = Menu(menubar, tearoff=0)
#helpmenu.add_cascade(label='About', command=notdone)
#menubar.add_cascade(label='Help',menu=helpmenu)

root.config(menu=menubar)



if default == 'yes':
    display = Label(root, text='Please change "Settings" from the default values')
    display.pack()
view_stats_btn = Button(root, text='Stats', command=lambda:view_stats_win(root, default))
view_stats_btn.config(width=10)
view_stats_btn.pack()

set_deatail_btn = Button(root, text='Settings', command=lambda:set_detail_win(root, full_path))
set_deatail_btn.config(width=10)
set_deatail_btn.pack()

view_timeline = Button(root, text='Timeline', command=lambda:view_timeline_web())
view_timeline.config(width=10)
view_timeline.pack()

view_ach_btn = Button(root, text='Achievements', command=lambda: ach_win(root))
view_ach_btn.config(width=10)
view_ach_btn.pack()

sep = Label(root, text='').pack()

quit_btn = Button(root, text='Quit', command=lambda:root.quit())
quit_btn.config(width=10,fg='red')
quit_btn.pack()

root.mainloop()
