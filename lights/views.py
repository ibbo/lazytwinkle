from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import zmq

# Create your views here.
def index(request):
    template = loader.get_template('lights/index.html');
    context = {}
    return render(request, 'lights/index.html', context)

def on(request):
    port = "5556"
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://localhost:%s" % port)
    socket.send("1: true")
    socket.close()
    return HttpResponseRedirect('/lights')

def off(request):
    port = "5556"
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://localhost:%s" % port)
    socket.send("1: false")
    socket.close()
    return HttpResponseRedirect('/lights')
