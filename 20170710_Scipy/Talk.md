Title: MyShake - Building a global smartphone seismic network


**Abstract**    
MyShake is a global smartphone seismic network that harnesses the power of crowdsourcing. It has two component: an android application running on the personal smartphones monitoring the sensors inside to detect earthquake-like motion, and a network detection algorithm to aggregate results from multiple smartphones to detect earthquakes. The MyShake application was released to the public on Feb 12th 2016. Within the first year, there are more than 250,000 earthquakes recorded by the smartphones all over the world. In this presentation, I will show how did we build the artificial neural network approach to distinguish earthquake-motions from daily human activities and the whole infrastructure of the whole system to collect and analyze large amount of data. Currently, we are collecting 30 GB time-series data each day, I will also show how do we extract earthquake signal from the data. 

**Extended Abstract (Should be no more than 2 pages, and address the following: Do you intend to present a demo? Does the work make any new contributions to open-source software? Which existing open-source tools does it use? What science fields are impacted by the work? How does it work fit into the Scientific Python community?)**   

Do you intend to present a demo?  
There will be no demo in this presentation. But this talk will be a case to show how we built the whole system using a lot of the open-source tools. 

Does the work make any new contributions to open-source software?  
Currently, due to privacy policy we have with the users, we can not share the data to the public. But the tools and the architecture of the whole system will provide useful insights to similar type of effort in large-scale sensor arrays to the community. We also want to use this chance to raise discussion from the audience and explore more directions for data acquisition, data analysis, and the architecture of the computing platform.   

Which existing open-source tools does it use?   
In the project, we used many open-source tools including, numpy, scipy, matplotlib, sklearn, folium, tensorflow, datashader, h5py, pymongo, pyspark, etc. 

What science fields are impacted by the work?  
The science fields are impacted by the work is the hazards migration, earth science, especially geosciences. The system we built will help to detect earthquakes and issue an early warning to the public in the future. Especially at places where they don't have good seismic networks, this type of network will help a lot to reduce the earthquake risk. 

How does it work fit into the Scientific Python community?   
This presentation will be a case of building a whole crowdsourcing system by utilizing a lot of the packages from Python community. I hope it will be a motivation for people to learn more and apply Python to different areas to solve real world problems. 



