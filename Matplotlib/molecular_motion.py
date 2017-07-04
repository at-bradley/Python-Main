import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walks, as long as the program is active.
while True:
	#Make a random walk, and plot the points.
	rw = RandomWalk(5000)
	rw.fill_walk()

	#Set the size of the plotting window.
	plt.figure(dpi=116, figsize=(9, 5))

	#Plot the points, ande show the plot.
	points_numbers = list(range(rw.num_points))
	plt.plot(
		rw.x_values, 
		rw.y_values, 
		linewidth=1,
	)

		#Emphasize the first and last points.
	plt.plot(0, 0, linewidth=10)
	plt.plot(
		rw.x_values[-1], 
		rw.y_values[-1], 
		linewidth=1,
	)

	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Generate another walk? (y/n): ")
	if keep_running == 'n':
		break