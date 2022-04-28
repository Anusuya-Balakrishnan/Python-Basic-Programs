def string_splosion(str):
  n=len(str)
  c=0
  string=""
  while(n>=c):
      string=string+str[:c]
      c+=1
  return string


strvalue=string_splosion("code")
print(strvalue)
