
from django.shortcuts import render


# Create your views here.
def chart(request):
	context = {}
	temlates = 'chart.html'
	return render(request,temlates,context)

