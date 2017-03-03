import time as ai;import urllib2 as al;import random as T;import re;from pprint import pprint as af;from bs4 import BeautifulSoup as am;p=5;O=3
def P(significant_others,verbose):
 z=al.build_opener();z.addheaders=[('User-Agent','Mozilla/5.0')];Q=z.open('http://waterassassins.com/leaderboard');R=am(Q,'html.parser');l=[];c={};f={}
 for S in R.body.find('tbody').find_all('tr'):
  q=S.find_all('td');a=q[1].find('p').text;m=[]
  for e in q[1].find('ul'):
   if e and not isinstance(e.find('span'),int):m.append(re.sub(r'[^\x00-\x7F]+','',e.find('span').text.strip()))
  A=int(q[2].text.strip())
  if A>=0:
   l.extend(m);c[a]={'members':m,'score':A}
   for e in m:f[e]=a
 if verbose:print'Found {0} advancing teams for a total of {1} players.\n'.format(len(c),len(f))
 n={}
 for o in significant_others:n[o[0]]=o[1];n[o[1]]=o[0]
 def r(B):
  if B in n:return n[B]
  return None
 def C(s):
  D=T.randrange(0,len(l));E=l[D];F=r(E)
  if E not in s:
   if not F or F not in s:return D
  return C(s)
 b={}
 for a,U in c.iteritems():
  d=[]
  for _a in xrange(p):g=C(U);h=l.pop(g);d.append(h)
  b[a]=d
 for V in xrange(O):
  t=[]
  for a,d in b.iteritems():
   i=[f[h]for h in d]
   if len(i)>len(set(i)):
    W=[G for G in i if i.count(G)>1];u=[e for e in d if f[e]in W];t.append((a,u[:]))
    while len(u)>1:
     j=u.pop();X=f[j];H=r(j)
     for v in b.iterkeys():
      I=False
      if a!=v:
       Y=c[v];w=b[v];J=[f[h]for h in w]
       if(not H or H not in Y)and X not in J:
        for k,Z in enumerate(w):
         K=r(j);aa=J[k]
         if(not K or K not in c[a])and aa not in i:d[d.index(j)]=Z;w[k]=j;I=True;break
      if I:break
  ab=sorted(list(c.keys()),key=lambda ac:-c[ac]['score'])[:p];ad=f[''.join([chr(sum((' \t    \t \t  \t\t\t\t\t\t\t \t\t\t\t\t\t \t\t\t\t \t \t\t\t \t  \t\t     \t \t\t\t \t \t\t  \t\t\t\t \t\t\t \t\t\t    \t\t  \t\t \t\t  \t  \t\t\t    \t\t'[g+k]=='\t')*2**k for k in range(7)))for g in range(0,98,7)])];ae=c[ad]
  for x in sorted(ae['members']):
   y=None
   for a,d in b.iteritems():
    if x in d:y=a;break
   L=ab.pop();g=b[y].index(x);M=T.randrange(0,p);b[y][g]=b[L][M];b[L][M]=x
  if verbose:print'Corrective pass #{0}. Fixing {1} mismatched targets:'.format(V+1,len(t));af(t)
 N={}
 for a,_a in c.iteritems():N[a]=b[a]
 return N
def calculate(significant_others,verbose=0):
 try:return P(significant_others,verbose)
 except:return calculate(significant_others,verbose=verbose)
def ag():ah=ai.clock();aj=calculate([],verbose=1);ak=ai.clock()-ah;print'\nResults:';af(aj);print'\nDone in {0:.3f}s.'.format(ak)
if __name__=='__main__':ag()
