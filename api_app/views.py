from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from overpy import Overpass

class IndexView(generic.base.TemplateView):
	template_name = "api_app/index.html"
	

	def get_context_data(self, **kwargs):
		countries = []
		result = Overpass().query("""relation["admin_level"="2"];out;""")
		for r in result.relations:
			try:
				countries.append(r.tags['name:en'])
			except (UnicodeEncodeError, KeyError):
				pass
		context = super(IndexView, self).get_context_data(**kwargs)
		context['countries'] = countries
		return context

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")