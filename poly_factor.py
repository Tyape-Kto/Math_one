### this stupid script gives you all possible (factor and quotient's exponent) of any polynomial with any power. yeah but it should not miss any exponent cause that one i didn't code. i have other works.

def factor_finder(poly):
  splitted = splitter(poly)
  p = num_giver(splitted[0])
  q = num_giver(splitted[-1])
  factor_p = factor(p)
  factor_q = factor(q)
  possible_roots = p_roots(factor_p, factor_q)
  terms = [num_giver(i) for i in splitted]
  roots = []
  for i in possible_roots:
    root = e_factor(i,terms)
    if not root:
      root = e_factor(-i, terms)
    if root:
      roots.append(root)
  return roots

def splitter(func):
  """
  this splits the expression into terms,
    returns in the form of list
  """
  splitted = []
  terms = []
  for i in func:
    if i == "+":
      splitted.append("".join(terms))
      terms.clear()
    elif i == "-":
      if terms:
        splitted.append("".join(terms))
        terms.clear()
    terms.append(i)
  splitted.append("".join(terms))
  return splitted

def num_giver(s): 
  """
  this returns num from given string term
  """
  num = []
  for i in s:
    if i == "x":
      break
    else:
      num.append(i)
  return int("".join(num))

def factor(num):
  """
  this just gives the factor of the number, 
    even making negative number to positive
  """
  factors = []
  for i in range(1,abs(num)//2+1):
    if num % i == 0:
      factors.append(i)
  factors.append(abs(num))
  return factors

def p_roots(p,q):
  """
  this just gives you factors of p/ factors of q without
    dublicate cause, set()
  """
  root = set()
  for i in q:
    for j in p:
      root.add(i/j)
  return list(root)

def e_factor(f:int, ex:list):
  """
  this takes factor and exponent of try if it gives zero 
    or not
  """
  result = 0
  quotient = []
  for i in range(len(ex)):
    if i == 0:
      result += ex[i] * f
      quotient.append(ex[i])
    else:
      result += ex[i]
      quotient.append(result)
      result = result * f
  if result == 0:
    return f, quotient
  else:
    return None

poly = "6x**3+13x**2-19x-12"
print(factor_finder(poly))
