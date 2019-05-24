from django.http import JsonResponse
from django.shortcuts import render
import webbrowser
import venky


# from django.core.context_processors import csrf

# Create your views here.

def index(request):
    return render(request, 'main.html')


def event_cmd_json(request):
    jsonResponse = {}

    if request.is_ajax():
        if request.method == 'GET':
            data = request.GET.dict()

            if data['cmd'] == 'internals':
                jsonResponse['internals'] = []
                jsonResponse['internals'].append("<b class='out-label'>internals:</b>")
                jsonResponse['internals'].append("<pre class='out-text'>	about 			- Summary of me</pre>")
                jsonResponse['internals'].append(
                    "<pre class='out-text'>	github 			- Explore the source code</pre>")
                jsonResponse['internals'].append(
                    "<pre class='out-text'>	techstack 		- tech stack for this website</pre>")

            if data['cmd'] == 'about_us':
                jsonResponse['about_us'] = []
                jsonResponse['about_us'].append("<b class='out-label'>about</b>")
                jsonResponse['about_us'].append("<pre class='out-text'>	Name: 			Eswar Praphul V</pre>")
                jsonResponse['about_us'].append("<pre class='out-text'>	DOB: 			12.05.1990</pre>")
            if data['cmd'] == 'github':
                jsonResponse['github'] = []
                jsonResponse['github'].append("<b class='out-label'>github:</b>")
                jsonResponse['github'].append("<pre class='out-text'>	<a href='https://github.com/eswarpraphul1'\
												style='color: white'>https://github.com/eswarpraphul1</a></pre>")

            if data['cmd'] == 'techstack':
                jsonResponse['techstack'] = []
                jsonResponse['techstack'].append("<b class='out-label'>techstack:</b>")
                jsonResponse['techstack'].append("<pre class='out-text'>	Using:</pre>")
                jsonResponse['techstack'].append(
                    "<pre class='out-text'>	 * Jquery Terminal Emulator: <a href='http://terminal.jcubic.pl' style='color: white'>http://terminal.jcubic.pl</a></pre>")
                jsonResponse['techstack'].append("<pre class='out-text'>	 * Django 2.0</pre>")

    return JsonResponse(jsonResponse)


def event_wed_json(request):
    jsonResponse = {}

    if request.is_ajax():
        if request.method == 'GET':
            data = request.GET.dict()
            print (data)
            if data['wedding'] == 'wedding' and not data.get('param[]'):
                jsonResponse['wedding'] = []
                jsonResponse['wedding'].append("<b class='out-label'>wedding commands</b>")
                jsonResponse['wedding'].append(
                    "<pre class='out-text'>	wedding invite			- Print the wedding invite</pre>")
                jsonResponse['wedding'].append(
                    "<pre class='out-text'>	wedding venue			- Locate at the venue in maps</pre>")
                jsonResponse['wedding'].append(
                    "<pre class='out-text'>	wedding bride			- Know the bride</pre>")
                jsonResponse['wedding'].append(
                    "<pre class='out-text'>	wedding groom			- Know the groom</pre>")
                jsonResponse['wedding'].append(
                    "<pre class='out-text'>	wedding rsvp			- RSVP for the event</pre>")

            if data['wedding'] == 'wedding' and data.get('param[]'):
                if data['param[]'] == 'invite':
                    jsonResponse['wedding'] = []
                    jsonResponse['wedding'].append("<b class='out-label'>Wedding Invite</b>")
                    jsonResponse['wedding'].append(venky.image)
                    jsonResponse['wedding'].append("<pre class='out-text'>	We are getting married on AUG 07</pre>")

                if data['param[]'] == 'venue':
                    jsonResponse['wedding'] = []
                    jsonResponse['wedding'].append("<b class='out-label'>Wedding Venue</b>")
                    jsonResponse['wedding'].append("<pre class='out-text'>	<a href='https://www.google.com/maps/place/Jayachandran+Mahal/@12.9611977,80.185193,17z/data=!3m1!4b1!4m5!3m4!1s0x3a525e7589fb1173:0x399abec0e6e1f70a!8m2!3d12.9611977!4d80.1873817'\
                    												style='color: white' target='_blank'>Open Maps</a></pre>")

                if data['param[]'] == 'bride':
                    jsonResponse['wedding'] = []
                    jsonResponse['wedding'].append("<b class='out-label'>Wedding Bride</b>")
                    jsonResponse['wedding'].append("<pre class='out-text'>	She is awesome, my perfect partner</pre>")

                if data['param[]'] == 'groom':
                    jsonResponse['wedding'] = []
                    jsonResponse['wedding'].append("<b class='out-label'>Wedding Groom</b>")
                    jsonResponse['wedding'].append("<pre class='out-text'>	Lazy fellow</pre>")

                if data['param[]'] == 'rsvp':
                    jsonResponse['wedding'] = []
                    jsonResponse['wedding'].append("<b class='out-label'>wedding RSVP</b>")
                    jsonResponse['wedding'].append("<pre class='out-text'>	Comming soon</pre>")

    return JsonResponse(jsonResponse)


def event_init_json(request):
    jsonResponse = {}

    if request.is_ajax():
        if request.method == 'GET':
            jsonResponse = {
                'cmd_list': ['internals', 'about_us', 'github', 'techstack'],
                'wed_list': ['wedding'],
            }

    return JsonResponse(jsonResponse)
