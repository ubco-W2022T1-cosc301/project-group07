# Final Report

### Introduction

This project examines a Metacritic Video Game dataset in order to discover interesting trends in the gaming industry. These trends can involve a variety of different attributes of a game and how they relate to other attributes, such as the platform and the genre of a game. Our group has a common interest in video games, and we were excited to see what we could find out using exploratory data analysis.

### Exploratory Data Analysis


### Question 1 + Results


### Question 2 + Results

The second research question inquired if there is a specific genre that a developer tends to develop video games of, and analyzed, for this developer, whether or not the most developed genre had changed over the years. The results of the data analysis in [analysis2.ipynb](./notebooks/analysis2.ipynb) gave us an insight of the most popular genres for the chosen developer, Nintendo.

![nintendo_genre_distribution](./images/nintendo_genre_distribution.png)

***Figure 2.1 Genre Distribution of Nintendo***

Given the distribution plot of Nintendo's genres in Figure 2.1, it was apparent that their most popular genres were Miscellaneous, Action, and Platformer. Discarding the 2D, Miscellaneous, and General genres due to non-specificity, we analyzed the trend of Nintendo's top five genres: Action, Platformer, Action Adventure, Fantasy, and Simulation.

![nintendo_genre_trend](./images/nintendo_genre_trend.png)

***Figure 2.2 Trend of the Most Popular Genres for Nintendo from 1995 - 2020***

We noticed that while certain genres certainly had more attention than others as a whole, often the most developed genre in a year could differ from the most developed genre in another year, as seen in Figure 2.2. Nintendo's most popular genre overall, Action, was not always the most developed genre from 1995 to 2020. There were years where the action genre was actually less popular than the other genres, such as Simulation games peaking in 2005. We also noticed that a genre could peak in popularity more than once, at different points in time. Not only did the Action genre peak in 2009, but also in 2019, among other years.

This answers our research question, whether there is a specific genre that a developer tends to develop games of, and whether the most developed genre had changed over the years or not. Nintendo tends to develop Action games (after Miscellaneous), and it's genre trend is not stable: the Action genre is not always the most popular in a given year, and different genres will wax and wane in popularity.

### Question 3 + Results
The third research question is to analyze the trend of the gaming platform from 1995 to 2020. With the everchanging nature of technology, video game industries have been changing in terms of the services and subscriptions that they use to develop and offer to the users using the updated tools and technologies in the field. With the rapid growth in the industry, I my research will analyze the shift in the trend of platforms used in the video gaming industry, ranging from the retro-gaming to modernized-gaming consoles overtime from 1995 to 2020.

![general_count_of_platform](./images/count_of_platform.jpg)

***Figure 3.1 Count of games by Platform***

As we can see in this horizontal bar chart, there are a number of gaming platforms used in the gaming industry. From the dataset itself, we can see that there are 22 different platforms with PC being the most count at around 4000 games. This dataset however, does not tell that PC is the most popular amongst all platform. The dataset is simply a representation from 1995 to 2020. As such, 3 platforms: Stadia, XboxSeriesX and PS5 seem to be the least number, but again, not the least popular since those platforms are released in 2019, 2020 and 2020 respectively. We will see the trend better in the line chart below.

![trend of platform](./images/trend_of_platform.jpg)

***Figure 3.2 Trend of Gaming Platform by Games***

This overlapped line chart gives a better overview of the trend in each platform from 1995 to 2020. For example, we can see that Gamecube is released in 2021, and overtime, it increases in the number of games until it peaked in around 2002 with around 125 games and started falling and failed to stay in the market in around 2007. Similar to many other platforms such as Dreamcast, 3DS, DS, etc.

PC on the other hand has been very stable. Interestingly however, PC seems to have 0 game in 1995. This can be seen as a anonimity in the dataset, since we know that there are many games that were there in 1995 or even before. This might because, the dataset did not have enough sources to gather games before or in 1995. But most importantly, we can see that PC has been very popular for game developers to create game for. With the rising and falling in between 1995 to 2020, it still remains to have around 250 games by 2020.

Xbox and Playstation have the very interesting trends amongst all others. As we can see, Xbox is first released in 2001 and stopped to have games by 2006, similarly to other series and Playstation series that started at some point, stayed for a while and just lost count of games after a couple years. We do not know for sure the reason behind this, but we can conclude from the chart that once one series end, another new model came out and started gaining popularity for game developers to create game on and the cycle continues. 

We can't conclude what happens in the rise and the drops of gaming platforms just by the chart. But we can tell for sure that the gaming industry was and still is very popular. With the advancing of technology, people are more eager to try on new different platforms that might offer better services than the others, such as better gaming experience.

### Summary

