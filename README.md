# surfs_up

## Ovierview
Our analysis is to gain some knowledge on whether or not it would be worthwhile to build surf shops in a specific city. In order to do that, we need to view the temperature data to see if a surf shop and ice cream shop could have sustained success year round. We will have to read the data gathered in our SQLIte file and come up with some statistical data to help us solve this problem. 

## Results
![June Data](https://github.com/Aceofhearts1/surfs_up/blob/main/Resources/june_DF.png)
![Dec Data](https://github.com/Aceofhearts1/surfs_up/blob/main/Resources/Dec_DF.png)

1. We see that that average temperature is identical in both June and December. The temp stays around mid 70s. Which is great for ice cream and surfing weather.
2. The minimum temperature for December is fairly lower than the minimum temperature for June. So there may be days in December that we won't do much business due to the temperature. However, that should be few are far in between since the average temperature is still in the mid 70s. The standard deviation is around 3 for both months so we should not expect the temperature to go past 3 standard devations away from the minimum too often. 64 and 56 seems to be an outliers.
3. The max temps are good numbers for ice cream and surfing. They are actually identical. So we see that December mostly effects the minimum temperature and not too much changing of the max temperature.

## Summary
We can see that a surf shop and ice cream shop would be a good business to get into if temperature was your only worry. For the most part, those would be your biggest worries. Howver, wether has a few other tricks can pull a rug from underneath you. 
- In our data, we have access to precipitation. It would be best to add that in our dataframes. Rain can change the attitudes of customers who want ice cream. 
- One other suggestion would be to add a few more months into our analysis. Since we are aiming for a yearlong business plan, it is best to see how most, if not all, the moinths behave.

![Extra data within the SQLite](https://github.com/Aceofhearts1/surfs_up/blob/main/Resources/SQLite_file_view.png)