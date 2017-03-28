Please provide a brief summary of your work?

I am currently working on MyShake, a project to build a global smartphone seismic network by turning users' smartphones into portable seismometers. I am mainly working on machine learning algorithms and building the whole infrastructue. We released the smartphone application last year and got 250,000 downloads globally. We are now collecting about 30 Gb time series sensor data each day. You can find more info of the project here - http://myshake.berkeley.edu/. 

Tell us a little about your computing experience?

I mainly use Python/Fortran in my reserach (mostly Python, only use Fortran to speed things up). I had experience of writing android applications and using Spark/Hadoop to analyze large amount of data by training machine learning algorithms. I only used mpi4py instead of MPI or OpenMP. But I do used Spark (by using pyspark and scala) and pig/hive to deal with distributed computing to analyze TB of data. I am comfortable working in a Linux environment. I seldom use standard 3rd party software. 

Briefly describe your problems to be solved and your computational needs. 

Currently, we collected more than 10 TB time-series sensor data in total last year, how to store and analyze the data is my high priority needs. I will try to build a deep learning model and train it using the data I collected. 

Briefly, what are your data management and analysis needs and with how much data do you typically work (MB, GB, TB, PB)?

We built our own servers to manage the data right now, it built on AWS using database like mysql/mongo. The data size is about 10 TB and it continuously increasing at a speed of 30 GB/day. Currently, we only do some simple analyze of the data, for example, cross-correlation of the waveforms. But I also want to build some machine learning models using all the waveform data. 