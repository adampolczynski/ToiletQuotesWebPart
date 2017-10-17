from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .forms import ToiletQuotes
from bson.json_util import dumps
from pymongo import MongoClient
from django.template import loader
import os

url = 'mongodb://xxxxxxxxxx/xxxxx'
client = MongoClient(url)

def home(request):
    return render(request, "home.html", {})
def addQuote(request):

    return render(request, "add_quote.html",{})
def getQuotes(request):
    output = client.xxx.ToiletQuotes.find({})
    return HttpResponse(dumps(output))
def showQuotes(request):
    output = client.xxx.ToiletQuotes.find({})
    return render(request, "show_quotes.html", {"quotes":output})
def insertQuote(request):
    if (request.method=='POST'):
        form = ToiletQuotes(request.POST)
        if form.is_valid():
            highest = client.xxx.ToiletQuotes.find_one(sort=[("quote_id",-1)])#.distinct("worker_id") # get highest worker ID element
            highest_id = highest['quote_id']+1
            client.xxx.ToiletQuotes.insert_one({
                "quote_id":int(highest_id),
                "user":form.cleaned_data['user'],
                "lang":form.cleaned_data['lang'],
                "quote":form.cleaned_data['quote']+"\r\n\r\n ~"+form.cleaned_data['author'],
                "category":form.cleaned_data['category'],
                "confirmed":0
                })
            return render(request, "add_quote.html", {"info":"Dodano"})
        #return render(request, "error.html", {"form":form})
        return render(request, "add_quote.html", {"form":form})
    return HttpResponse("nothing to GET")
        
def stats(request):
    length = {}
    length['length'] = client.xxx.ToiletQuotes.find({}).count()
    length['lengthpl'] = client.xxx.ToiletQuotes.find({"lang":"pl"}).count()
    length['lengthen'] = client.xxx.ToiletQuotes.find({"lang":"en"}).count()
    length['lengthcat0'] = client.xxx.ToiletQuotes.find({"category":0}).count()
    length['lengthcat1'] = client.xxx.ToiletQuotes.find({"category":1}).count()

    output = list()
    output.insert(0, length)
    return render(request, "stats.html", {"data":output})
def confirm(request, quote_id, act_pass):
    if act_pass!="admin666":
        return redirect("/showQuotes/")
    else:
        client.xxx.ToiletQuotes.update_one({"quote_id":int(quote_id)},{"$set": {"confirmed":1}}, upsert=False)
        return redirect("/showQuotes/")
def delete(request, quote_id, act_pass):
    if act_pass!="admin666":
        return redirect("/showQuotes/")
    else:
        client.xxx.ToiletQuotes.remove({"quote_id":int(quote_id)})
        return redirect("/showQuotes/")
