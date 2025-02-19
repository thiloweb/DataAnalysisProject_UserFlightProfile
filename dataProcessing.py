import fetchData
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = fetchData.my_data
color_data = {
    "OneCategory":"#00008B", #Darkblue
    "BarChartBG":"#E5E4E2", # Platinum
    "FigureBG":"#FFFFFF",
    "Transatlantic":"#87CEEB", #Skyblue
    "Continental":"#CD7F32", #Bronze
    "Europe":"#32CD32", #Lime green
    "Americas":"#DAA520", #Goldenrod
    "National":"#FF7F50" #Coral
}

# CHART - NUMBER OF AIRPORTS USED BY COUNTRIES
# Getting the country name (3rd value of each tuple) from the first data set as inner list 
countries_by_airports = [tup_val[2] for tup_val in list(data[0].values())[0]]
# Creating a pd series and count value occurrence for top 10 values 
pd_top10_countries_by_airports = pd.Series(countries_by_airports).value_counts()[:10]
# Data visualization in a bar chart
plt.figure(facecolor=color_data["FigureBG"])
plt.bar(pd_top10_countries_by_airports.keys(),pd_top10_countries_by_airports,color=color_data["OneCategory"], edgecolor="#000000")
ax = plt.subplot()
bars = ax.bar(pd_top10_countries_by_airports.keys(), pd_top10_countries_by_airports)
ax.bar_label(bars, color=color_data["OneCategory"])
ax.set_facecolor(color_data["BarChartBG"])
plt.suptitle("NUMBER OF AIRPORTS USED IN", fontsize=18)
plt.xticks(rotation=40, horizontalalignment="center",fontsize=12)
# Override decimal numbers
y_values = np.arange(0,13,1)
ax.set_ylim([0,max(y_values)])
plt.yticks(y_values, fontsize=12)
plt.margins(0.05,1)
plt.subplots_adjust(bottom=0.2)
plt.show()
plt.close()


# CHART - TOP 5 AIRLINES USED
# Getting the airline name (=1rd value of each tuple) from the second data set as inner list 
airlines = [tup_val[0] for tup_val in list(data[1].values())[0]]
# Store values in a series and count value occurrence for top 5 values
pd_top5_airlines = pd.Series(airlines).value_counts()[:5]
# Data visualization in a bar chart
plt.figure(facecolor=color_data["FigureBG"])
plt.bar(pd_top5_airlines.keys(),pd_top5_airlines,color=color_data["OneCategory"], edgecolor="#000000")
ax = plt.subplot()
bars = ax.bar(pd_top5_airlines.keys(), pd_top5_airlines)
ax.bar_label(bars, color=color_data["OneCategory"])
ax.set_facecolor(color_data["BarChartBG"])
plt.suptitle("TOP 5 AIRLINES USED", fontsize=18)
plt.ylabel("Frequency of Use", fontsize=15, labelpad=15)
plt.xticks(rotation=40, horizontalalignment="center", fontsize=13)
plt.margins(0.05,0.1)
plt.subplots_adjust(bottom=0.2)
plt.show()
plt.close

# CHART FLIGHT TYPES PROPORTION/PERCENTAGE
# Getting the total number of all flights   
totalnumber_flights_all = [tup_val[0] for tup_val in list(data[2].values())[0]][0]
# Getting the total number of national flights
totalnumber_flights_national = [tup_val[0] for tup_val in list(data[6].values())[0]][0]
# Getting the total number of transatlantic flights
totalnumber_flights_transatlantic = [tup_val[0] for tup_val in list(data[3].values())[0]][0]
# Calculating the total number of continental flights
totalnumber_flights_continental = totalnumber_flights_all - totalnumber_flights_national - totalnumber_flights_transatlantic
# Store values in a series with customized index
totalflights_pie_data = pd.Series([totalnumber_flights_continental,totalnumber_flights_transatlantic,totalnumber_flights_national], index=["Continental","Transatlantic","Domestic"])
# Data visualization in a pie chart
totalflights_pie_colors = {"Continental":color_data["Continental"],"Transatlantic":color_data["Transatlantic"],"Domestic":color_data["National"]}
plt.figure(facecolor=color_data["FigureBG"])
plt.pie(
    totalflights_pie_data, 
    colors=[totalflights_pie_colors[key] for key in totalflights_pie_colors.keys()], 
    labels=totalflights_pie_data.keys(), 
    textprops={"fontsize":14},
    wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'}, 
    autopct=lambda x:f"{x:.1f}%\n ({x*sum(totalflights_pie_data)/100 :.0f})",
    startangle=90,
    )
plt.suptitle(f"FLIGHT TYPES", fontsize=18)
plt.show()
plt.close()

# CHART FLIGHT DISTANCE
# Getting total number of all flights   
totalnumber_flights_europe = [tup_val[1] for tup_val in list(data[4].values())[0]][0]
# Getting total number of national flights
totalnumber_flights_americas = [tup_val[1] for tup_val in list(data[5].values())[0]][0]
# Getting total number of transatlantic flights
totalnumber_flights_transatlantic = [tup_val[1] for tup_val in list(data[6].values())[0]][0]
# Data visualization in a pie chart
totalflightdistance_pie_data = pd.Series([totalnumber_flights_europe,totalnumber_flights_americas,totalnumber_flights_transatlantic], index=["Europe","Americas","Transatlantic"])
totalflightdistance_pie_colors = {"Europe":color_data["Europe"],"Americas":color_data["Americas"],"Transatlantic":color_data["Transatlantic"]}
plt.figure(facecolor=color_data["FigureBG"])
plt.pie(
    totalflightdistance_pie_data, 
    colors=[totalflightdistance_pie_colors[key] for key in totalflightdistance_pie_colors.keys()], 
    labels=totalflightdistance_pie_data.keys(), 
    textprops={"font":"Ubuntu","fontsize":15},
    wedgeprops={'linewidth': 2.0, 'edgecolor': '#FFFFFF'}, 
    autopct=lambda x:f"{x*float(sum(totalflightdistance_pie_data)/100) :,.0f} \nkm", # without percentage
    startangle=90,
    )
plt.suptitle(f"TOTAL FLIGHT DISTANCE", fontsize=18)
plt.show()
plt.close()

# CHART TOTAL FLIGHT TIMES
# Getting the total flight time in minutes (3rd value of each tuple) from the second data set as inner list and store looped valued in new list
flighttime_values = []
for q in range(len(data))[3:]:
     flighttime_values += [tup_val[2] for tup_val in list(data[q].values())[0]]
# Convert minutes into rounded hours and store values in new list
def convert_min_to_hrs(totalminutes):
    hours = totalminutes/60
    time_in_hours = round(hours)
    return time_in_hours
flighttime_values_converted = []
for x in range(len(flighttime_values)):
    flighttime_values_converted.append(convert_min_to_hrs(flighttime_values[x]))
flighttime_series = pd.Series(flighttime_values_converted, index=["National","Europe","Americas","Transatlantic"])
# Data visualization in a bar chart
colors_regional_flighttime = {"National":color_data["National"],"Europe":color_data["Europe"],"Americas":color_data["Americas"],"Transatlantic":color_data["Transatlantic"]}
plt.figure(facecolor=color_data["FigureBG"])
plt.bar(flighttime_series.keys(),flighttime_series,color="#00008b", edgecolor="#000000")
ax = plt.subplot()
bars = ax.bar(flighttime_series.keys(), flighttime_series, color=[colors_regional_flighttime[key] for key in colors_regional_flighttime.keys()])
ax.bar_label(bars, fmt="{:,.0f} hrs", fontweight="bold")
ax.set_facecolor(color_data["BarChartBG"])
plt.suptitle("TOTAL FLIGHT TIMES", fontsize=18)
plt.ylabel("Hours (Rounded)", labelpad=10, fontsize=14)
plt.xticks(rotation=0, horizontalalignment="center", fontsize=14)
plt.margins(0.05,0.1)
plt.show()
plt.close()

# CHART PROPORTION NUMBER OF FLIGHTS, FLIGHT DISTANCE, AND FLIGHT TIME FOR REGIONS AM,TA,EU 
# Getting the total number of flights for Europe, Americas, and Transatlantic, 1st element of list[flight total, distance, time] for each category
flighttotal_eu_am_ta = []
for i in range(len(data))[4:]:
    flighttotal_eu_am_ta += [tup_val[0] for tup_val in list(data[i].values())[0]]
# Getting the total flight distance for Europe, Americas, and Transatlantic, 2nd element of list[flight total, distance, time] for each category, convert from decimal to int
flightdistance_eu_am_ta = []
for i in range(len(data))[4:]:
    flightdistance_eu_am_ta += [int(tup_val[1]) for tup_val in list(data[i].values())[0]]
# Getting the total flight time for Europe, Americas, and Transatlantic, 3rd element of list[flight total, distance, time] for each category, convert from decimal to int
flighttime_eu_am_ta = []
for i in range(len(data))[4:]:
    flighttime_eu_am_ta += [int(tup_val[2]) for tup_val in list(data[i].values())[0]]
# Merge data into df and transpose categories
plotdata = pd.DataFrame(
    {"Number of Flights":flighttotal_eu_am_ta,
    "Flight Distance":flightdistance_eu_am_ta,
    "Flight Time":flighttime_eu_am_ta},
    index=["Europe","Americas","Transatlantic"]
)
plotdata = plotdata.transpose()
# Data visualization in a 100% stacked bar chart
colors_stackedplot = {"Europe":color_data["Europe"],"Americas":color_data["Americas"],"Transatlantic":color_data["Transatlantic"]}
stacked_plotdata = plotdata.apply(lambda x: x*100/sum(x), axis=1)
stacked_plotdata.plot(kind="bar",stacked=True, color=[colors_stackedplot[key] for key in stacked_plotdata])
ax = plt.subplot()
ax.set_facecolor(color_data["BarChartBG"])
for container in ax.containers: 
    # custom label calculates percent and add an empty string so 0 value bars don't have a number CHANGE!
    labels = [f'{w:0.2f}%' if (w := v.get_height()) > 0 else '' for v in container]
    ax.bar_label(container, labels=labels, label_type='center', padding=0.3, color='#000000', fontweight="bold")
plt.suptitle("TOTAL FLIGHTS, DISTANCE & TIME %", fontsize=18)
plt.legend(loc='upper right', reverse=True, bbox_to_anchor=(1,1), facecolor="#D3D3D3", fancybox=True, framealpha=0.7, prop=dict(size=13))
plt.ylabel("Percentage", fontsize=15)
plt.xticks(rotation=0, horizontalalignment="center", fontsize=13)
plt.show()
plt.close()