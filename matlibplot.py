import matlibplot.pyplot as plt

# create a line plot
plt.plot(year, plot)
plt.show()

# create a scatterplot
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.show()

# plot a histogram
plt.hist(life_exp, bins = 5) # default is 10

plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.grid(True)

plot.show()
