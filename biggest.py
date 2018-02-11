def biggest(arg):
  maxx=0
  for b in arg:
    if len(arg[b])>maxx:
        maxx=len(arg[b])
        key=b
  if maxx==0:
      return None
  return b
