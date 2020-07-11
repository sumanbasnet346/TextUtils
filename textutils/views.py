
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return render(request,'index.html')
#Anaalysing text:
def analyze(request):
    #get the text to be analysed
     djtext = request.POST.get('text','default')
  #get the response what things should be analysed
     removepunc = request.POST.get('removepunc','off')
     fullcaps = request.POST.get('fullcaps','off')
     newlineremover = request.POST.get('new','off')
     exspace = request.POST.get('exspaceremover','off')
     counter = request.POST.get('counter','off')
# Check which response is on and perform according to it
     if removepunc =="on":
         punctuations = '''!()-[];:'"\/,<>.?@#$%^&*_~'''
         analyzed=""
         for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char
         params = {'num':'','purpose':'Removed punctuations', 'analyzed_text':analyzed}
         print (analyzed)
         djtext = analyzed


     if newlineremover =="on":
         analyzed = ""
         for char in djtext:
             if char !="\n" and char!="\r":
                analyzed = analyzed + char
         params = {'purpose': 'Newline remover', 'analyzed_text': analyzed}
         print(analyzed)
         djtext = analyzed


     if fullcaps =="on":
         analyzed=""
         for char in djtext:
             analyzed = analyzed + char.upper()
         params = {'purpose': 'Changed into Uppercase', 'analyzed_text': analyzed}
         print(analyzed)
         djtext = analyzed


     if exspace == "on":
         analyzed = ""
         for index,char in enumerate(djtext):
             if not(djtext[index] ==" " and djtext[index+1] == " "):
                analyzed = analyzed + char
         params = {'purpose': 'Extra-Space Remover', 'analyzed_text': analyzed}
         djtext=analyzed



     if counter == "on":

               analyzed = "No Of Character is {}".format(len(djtext))
               params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}


     if (counter == "off" and removepunc == "off" and exspace == "off" and newlineremover == "off" and fullcaps =="off"):
         return HttpResponse("Error!!!")
     return render(request, 'analyze.html', params)



