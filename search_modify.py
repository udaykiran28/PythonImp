# This code helps you execute search queries on Google using Python terminal
menu= ["1.Google","2.Yahoo","3.Dogpile","4.DuckDuckGo","5.Ecosia","6.Exit()","7.All()"]
#menu[1]="Google"
#menu[2]="Yahoo"
#menu[3]="Dogpile"
#menu[4]="DuckDuckGo"
#menu[5]="Ecosia"
#menu[6]="Exit()"
#menu[7]="All()"
print ("#################################")
print (" Choose Search Engine - > Fire Query")
print (" By Shashi Prakash Agarwal\n")
import webbrowser

for i in menu:
        print (i)

while True:
    #options=menu.keys()
    #menu.sort()
    #for i in menu:
     #   print (menu)
    selection=input("\nPlease select Engine number from the above list:")
    search_query=input("Please enter Search Query:")
    if selection =='1':
        webbrowser.open('http://google.com/search?q='+search_query)
    elif selection == '2':
        webbrowser.open('http://yahoo.com/search?p='+search_query)
    elif selection == '3':
        webbrowser.open('http://dogpile.com/search/web?q='+search_query)
    elif selection == '4':
        webbrowser.open('http://duckduckgo.com/?q='+search_query)
    elif selection == '5':
        webbrowser.open('http://ecosia.com/search?q='+search_query)
    elif selection == '6':
        print ("Bye Bye!")
        break
    elif selection == '7':
        webbrowser.open('http://google.com/search?q='+search_query)
        webbrowser.open('http://yahoo.com/search?p='+search_query)
        webbrowser.open('http://dogpile.com/search/web?q='+search_query)
        webbrowser.open('http://duckduckgo.com/?q='+search_query)
        webbrowser.open('http://ecosia.com/search?q='+search_query)
    else:
        print ("Unknown Option Selected!")
