from django.http import HttpResponse


def IndexView(request):
    return HttpResponse(
        """
<h1>Welcome to our car rental!</h1>
<a href='http://localhost:8000/catalog/list/'>What cars do we have?</a><br>
<h2>About us</h2>
<p>Our rental shop was established in 2011 and today offers approximately 30 cars.</p>
"""
    )


def ListView(request):
    return HttpResponse("Here will be list of cars")
