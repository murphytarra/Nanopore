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

## 3. Plotting a Single Event 

To plot a single event, we use the `.plot_one_event()` function, where the event name is passed as an argument. 

```js
Events.plot_one_event('event_name')
```
 
A further option in plotting these events marking each of the peaks in the event. This can be acheived by setting `peaks=True`.

```js
Events.plot_one_event('event_name', peaks=True)
```

Optional arguemnts can also be included, including determining and plotting the position of the peaks: This method involves the use of scipy's `find_peaks()` function, of which the inputs are given below. 
- height: Required height of peaks. Default value is set to 0.1
- threshold: Required threshold of peaks, the vertical distance to its neighboring samples. Default value is set to 0.015
- distance: Required minimal horizontal distance (>= 1) in samples between neighbouring peaks. Default value is set to 25
- widths: Required width of peaks in samples. Default value is set to 1
- wl: Used for calculation of the peaks prominences, thus it is only used if one of the arguments prominence or width is given. Default value is set to 10

Default values are given above for the Nanopore class. To change the parameters of these parameters, one use pass the value into the `Nanopore()` class, as given below

```js
Events.h = 0.05
Events.wl = 15
```

These changes must be completed before `.plot_one_event()` is called. 

To plot all the events in a file, one can pass the function 

```js
Events.plot_events()
```

In order to plot the events about a given noise threshold, one can pass the argument `ln = True`; 

```js
Events.plot_events(ln = True)
```

## Further things to upload

Things I'll upload this week: 
- Plotting Values of heights, distances from one another, position
- Plotting heights of peaks relative to baseline
- Creating list of events with at least a specific number of events
- Compensating for saturation in voltage. 



