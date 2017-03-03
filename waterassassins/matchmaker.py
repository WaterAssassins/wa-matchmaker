import time as am;import urllib2 as ao;import random as X;import re;from pprint import pprint as aj;from bs4 import BeautifulSoup as ap;n=5;S=3
def T(significant_others,verbose):
 z=ao.build_opener();z.addheaders=[('User-Agent','Mozilla/5.0')];U=z.open('http://waterassassins.com/leaderboard');V=ap(U,'html.parser');j=[];c={};f={}
 for W in V.body.find('tbody').find_all('tr'):
  o=W.find_all('td');a=o[1].find('p').text;k=[]
  for e in o[1].find('ul'):
   if e and not isinstance(e.find('span'),int):k.append(re.sub(r'[^\x00-\x7F]+','',e.find('span').text.strip()))
  A=int(o[2].text.strip())
  if A>=0:
   j.extend(k);c[a]={'members':k,'score':A}
   for e in k:f[e]=a
 if verbose:print'Found {0} advancing teams for a total of {1} players.\n'.format(len(c),len(f))
 l={}
 for m in significant_others:l[m[0]]=m[1];l[m[1]]=m[0]
 B=[0,-4,10,-18,-19]
 def p(C):
  if C in l:return l[C]
  return None
 def D(q):
  E=X.randrange(0,len(j));F=j[E];G=p(F)
  if F not in q:
   if not G or G not in q:return E
  return D(q)
 b={}
 for a,Y in c.iteritems():
  d=[]
  for _a in xrange(n):r=D(Y);g=j.pop(r);d.append(g)
  b[a]=d
 B+=[-46,70,3,-8,-14]
 for Z in xrange(S):
  s=[]
  for a,d in b.iteritems():
   h=[f[g]for g in d]
   if len(h)>len(set(h)):
    aa=[H for H in h if h.count(H)>1];t=[e for e in d if f[e]in aa];s.append((a,t[:]))
    while len(t)>1:
     i=t.pop();ab=f[i];I=p(i)
     for u in b.iterkeys():
      J=False
      if a!=u:
       ac=c[u];v=b[u];K=[f[g]for g in v]
       if(not I or I not in ac)and ab not in K:
        for L,ad in enumerate(v):
         M=p(i);ae=K[L]
         if(not M or M not in c[a])and ae not in h:d[d.index(i)]=ad;v[L]=i;J=True;break
      if J:break
  N=109;O=[]
  for w in B:N+=w;O.append(chr(N))
  af=sorted(list(c.keys()),key=lambda ag:-c[ag]['score'])[:n];ah=f[''.join(O[::-1])];ai=c[ah]
  for x in sorted(ai['members']):
   y=None
   for a,d in b.iteritems():
    if x in d:y=a;break
   P=af.pop();r=b[y].index(x);Q=X.randrange(0,n);b[y][r]=b[P][Q];b[P][Q]=x
  if verbose:print'Corrective pass #{0}. Fixing {1} mismatched targets:'.format(Z+1,len(s));aj(s)
 R={}
 for a,_a in c.iteritems():R[a]=b[a]
 return R
def calculate(significant_others,verbose=0):
 try:return T(significant_others,verbose)
 except:return calculate(significant_others,verbose=verbose)
def ak():al=am.clock();an=calculate([],verbose=1);w=am.clock()-al;print'\nResults:';aj(an);print'\nDone in {0:.3f}s.'.format(w)
if __name__=='__main__':ak()
