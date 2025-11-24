p1 = '''
<!DOCTYPE html>
<html>
<body>
'''

#<h1>My First Heading</h1>

#<p>My first paragraph.</p>

p2 = '''
</body>
</html>
'''

filin = open('lista_png.txt', 'r')
datos = filin.readlines()
filin.close()

filon = open('p2.html', 'w')

filon.write(p1)

for ss in datos:
  ss = ss.replace('\n','')
  ss2 = '<img src=' + ss + ' alt="sujeto" width="25%">'
  filon.write(ss2)

filon.write(p2)
filon.close()


