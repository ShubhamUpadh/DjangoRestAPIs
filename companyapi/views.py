from django.http import HttpResponse, JsonResponse


def home_page(request):
    friends = ['abc','def','efg']
    strs = '''<h1>Home Page</h1>
            <br>
            <p>This page has been created using django</p>'''
    print("Home Page Requested")
    return JsonResponse(friends,safe=False)
