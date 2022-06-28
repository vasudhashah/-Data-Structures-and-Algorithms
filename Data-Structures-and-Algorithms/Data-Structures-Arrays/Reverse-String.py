def Reverse(str):
  ans=[]
  for i in range(len(str)-1,-1,-1):
    ans.append(str[i])

  ans = "".join(ans)
  print(ans)

Reverse("I am vasudha")

#or str[::-1]