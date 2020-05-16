#Solution from stack overflow  https://stackoverflow.com/questions/39715457/any-faster-way-to-find-the-number-of-lucky-triples
# Time complexity: O(n^2)
# Space complexity: O(n)
#Paradigm :Dynamic Programming
#Intution -
'''
Why DP? 
We have something that can clearly be modeled as having a left to right order (DP orange flag), and it feels like reusing previously computed values could be interesting, because the brute force algorithm does the exact same computations a lot of times.
How to get from that to a solution? 
Run a simple example (hint: it should better be by treating input from left to right). At step i, compute what you can compute from this particular point (ignoring everything on the right of i), and try to pinpoint what you compute over and over again for different i's: this is what you want to cache. Here, when you see a potential triple at step k (L[k] % L[j] == 0), you have to consider what happens on L[j]: "does it have some divisors on its left too? Each of these would give us a new triple. Let's see... But wait! We already computed that on step j! Let's cache this value!" And this is when you jump on your seat.
'''
def getlucky(inp):
  c=[0]*len(inp) #A cache which stores how many divisors for that indice exist
  triples=0 #return value
  #For i,j,k we check if inp[k]%inp[j]==0 then c[j] will be our current triplet count

  for k in range(0,len(inp)):
    for j in range(0,k): 
      if inp[k]%inp[j]==0:
        print(inp[k],inp[j])
        c[k]+=1
        triples+=c[j]
      
  return triples

#print(getlucky([1,2,3,4,5,6]))
print(getlucky([1,2,3,4,5,6]))