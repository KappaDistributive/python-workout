def mysum(*args):
  if not args:
    return args
  x = args[0]
  for y in args[1:]:
    x += y
  return x
