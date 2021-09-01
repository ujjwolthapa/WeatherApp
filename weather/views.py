from django.shortcuts import redirect, render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=9f4c824d68c982a139ea6419878b9fe2').read()
            json_data=json.loads(res)
            data={
                "country_code":str(json_data['sys']['country']),
                "coordinate":str(json_data['coord']['lon'])+''+
                str(json_data['coord']['lat']),
                "k_temp":int(json_data['main']['temp']),
                "pressure":str(json_data['main']['pressure']),
                "humidity":str(json_data['main']['humidity']),

            }
            temp= str(round((data['k_temp'])-273.15)) + '°C'
        except :
            messages=str(city)
            return render(request,'index.html',{'messages':messages})

    else:
        data={}
        city=''
        temp=''

    return render(request,'index.html',{'city':city,'data':data,'temp':temp})