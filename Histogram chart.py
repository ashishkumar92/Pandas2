import matplotlib.pyplot as plt

year = [1980,1990,2000,2010,2020]
birth_year = [1990,1980,1988,2020,1993,2004,2009,1992,1987,2003,2004,2007]

plt.hist(birth_year, bins=year)

# xticks and yticks are used to define any range as per demand.


plt.show()
