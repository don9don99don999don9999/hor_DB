from django.shortcuts import render
from .models import CMS
import numpy as np
from django import forms
import pandas as pd
import csv
class NameForm_gene(forms.Form):
    gene_names = forms.CharField(widget=forms.Textarea)
# Create your views here.

#def ccsv(test):
    #test = np.array(test)
    #elements = list(set(np.ravel(test)))

   # links = {'Expt','genes'}
   # for e in test:
      #  Expt =elements.index(e[0])
            
        
      #  genes = elements.index(e[1])
       
       # links += "{%s ,%s},\n"%(Expt,genes)
    
   # final = links
   # return final
def index(request):
    #DBex    = DBmodel.objects.order_by('?')[0:2] # 렌덤으로 클레스를 가져온다.

    if request.method=='POST':
        form = NameForm_gene(request.POST)
        if form.is_valid():
            genes         = form.cleaned_data['gene_names'].split(',')
            print(genes)
            form          = NameForm_gene()
            #gene_filter_xxxxx ={'Expt':[],'gene_names':[]}
            TTs=[]
            for gene in genes: 
                gene_filter = CMS.objects.filter(Gene_id =gene) 
                
                TT=  [[xxxxxx.Treatment_codenumber, xxxxxx.Tpm] for xxxxxx in gene_filter]
                TTs += TT
                
                #for xxxxxx in gene_filter:
                   # Conmjsa=xxxxxx.split(';')[4].split(',')[0].split('/')[0].split('_')[0]
                   # Conmjsa_int_p=enumerate(list(set(np.ravel(np.array(Conmjsa)))))
                   # for ddddd in Conmjsa_int_p:
                    #    if ddddd =='Con':
                    #        return gene_filter_xxxxx['Expt'].append('1');
                    #    elif ddddd == 'JA':
                    #        return gene_filter_xxxxx['Expt'].append('2');
                   #     else:
                   #         return gene_filter_xxxxx['Expt'].append('3')
                   # CONMJSA=xxxxxx.split(';')[9]
                  #  for x in CONMJSA:
                  #      gene_filter_xxxxx[genes].append(x)   
            TTTs = np.array(TTs)
            
            data =[(TTTs)]
           
            np.savetxt('./ConMJSA/static/%s.csv'%'.'.join(genes), np.column_stack((data)), delimiter=",", fmt='%s',header='Expt,genes',comments="")
            
            #csv     = csv(gene_filter_xxxxx)
           
            csvfilename = './ConMJSA/static/%s.csv'%'.'.join(genes)
            #with open(csvfilename,'wb') as f:
                
            #    print(csv,file=f)
#           return render(request, 'network_test/index.html',{'form': form,'query':','.join(genes)}) # 렌덤으로 가져온 클레스를 html로 보낸다. 
            return render(request, 'ConMJSA/index.html',{'csvf':csvfilename.split('/')[-1],'form':form,'query':(', '.join(genes))})
#           return render(request, 'network_test/index.html',{'json':json,'form':form,'query':','.join(genes)})

    else:
        form = NameForm_gene()
        return render(request, 'ConMJSA/index.html',{'csvf':'temp.csv','form': form,'query':"AT1G15160.3"})

