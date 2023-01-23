# Introduction
Package for analysising and viewing transport events occuring in microfluidic devices. 

This package was created throughout my Mini MRes project while a student at the NanoDTC, Cavendish Laboratories, Cambridge. 

# Installation and Requirements

# Documentation

## 1. Loading Dataset

To begin an analysis of the events that occured throughout a measurement, we use the `Nanopore()` class, whose argument is the path of the events.hdf file we wish to analysis. 

An example if given below; 

```js
Events = Nanpore(insert_file_name)
```

After importing in the events file, we can obtain information from the class, including number of events and the list of event names. 

```js
Events.n_events #prints out number of events 
Events.events_list #prints out the list of names of the events
```

## 2. Noise Processing 

To analysis our data, we first apply a filter to our events, to disregard any events given by a noise threshold. This can be applied by using the `.filter()` function, which creates a list of events above a certain noise threshold. 

```js
Events.filter()
```

The default threshold is initiall set to `level = 0.04'` however, this can be adjusted by passing in the the level as an argument, as shown below; 

```js
Events.filter(level=0.02)
```

After filtering the data, we can obtain a list of events that were below the noise threshold; 

```js
Events.events_list_ln
```

3. Plotting a Single Event 

To plot a single event, we use the `.plot_one_event()` function, where the event name is passed as an argument. 

Optional arguemnts can also be included, including determining and plotting the position of the peaks: This method involves the use of scipy's `find_peaks()` function, of which the inputs are given below. 
- height: 
- threshold: 
- distance:
- widths:
- wl:

Default values are given above for the Nanopore class. To change the parameters of these parameters, one use pass the value into the `Nanopore()` class, as given below




