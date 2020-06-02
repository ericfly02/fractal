import numpy 
from pyfiglet import Figlet

custom_fig = Figlet(font='starwars')
print(custom_fig.renderText('E.G.D fractal'))
def generate_julia():

	print('================================Eric.GD===================================')
	w = int(input('Introduzca la anchura:'))
	h = int(input('Introduzca la altura:'))
	f = float(input('Introduzca un numero entre 0 i 1 (po ejemplo 0.37):'))
	name_input = input('Introduzca el nombre que le quiere otorgar al archivo, por ejemplo <fractal>')

	re_min = -2.0
	re_max = 2.0
	im_min = -2.0
	im_max = 2.0
	name = (str(name_input)+ '.jpg')
	c = complex(0.0, f)
	real_range = numpy.arange(re_min, re_max, (re_max-re_min) / w)
	image_range = numpy.arange(im_min, im_max, (im_max-im_min) / h)


	output = open(name, 'w')
	output.write('P2\n# Julia Set Image\n' + str(w) + ' ' + str(h) + '\n255\n')

	for im in image_range:
		for re in real_range:
			z = complex(re, im)
			n = 255
			while abs(z) < 10 and n >= 5:
				z = z * z + c
				n -= 5
			output.write(str(n) + ' ')
		output.write('\n')
	output.close()

	print('Ya has creado la foto' '--> ' + name)
	print('================================Eric.GD===================================')

generate_julia()
