from django.http import HttpResponse


def home_page(request):
    strs = '''<h1>Home Page</h1>
            <br>
            <p>This page has been created using django</p>'''
    print("Home Page Requested")
    return HttpResponse(strs)
