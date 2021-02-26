cpdef int loop(dict f_x_sent, list image_list_sent):
	cpdef dict f_x = f_x_sent
	cpdef list image_list = image_list_sent
	for i in range(256):
		f_x[i] = image_list.count(i)
	return f_x