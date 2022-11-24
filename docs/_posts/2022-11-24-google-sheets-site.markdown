---
layout: post
title:  "Generate Proposals with Google Sheets, App Script, Vue, & Vuetify"
categories: 
excerpt: Yeah, I'm a full stack developer 😎
---

[Link to the Project README](https://github.com/radiosketch/edu/tree/master/Software%20Engineering/Websites/google_sheets_site)

&emsp;In an effort to help streamline customer interactions, I've been tasked with making a webapp for generating proposals which can be sent directly to clients of my employer.   

&emsp;The initial project was a proof of concept containing basic forms for getting and setting fields contained within the database (in this case, a Google Sheet). To prevent the user from changing the datatype of a cell entirely, the edit form, shown in yellow, checks the datatype of the cell selected for editing. The form will not let a request go through until the input matches a regex that corresponds to the cell data format.  

![Image of Site](https://cdn.discordapp.com/attachments/513555424247676929/1035358405788971098/sheets_site_10_27_2022.PNG)

&emsp;Later versions will make it easier to select and edit the cells related to each line item. Rather than typing the index of the cell in the database in order to edit it, the user should be able to select items from a dropdown and be able to edit the available fields.  

## Intuitive Estimates with Blueprints  

&emsp;When inspecting a crawlspace, measurements need to be taken to calculate material costs and estimate the amount of labor required to complete the job. I propose a method of making simple blueprints since making the calculations by hand is slow and unintuitive to perform in the field. Shown below is a current view of the demo for this idea.

![Image of Crawlspace Calculator Demo](https://cdn.discordapp.com/attachments/513555424247676929/1045225340882141214/image.png)  

&emsp;Eventually the user will be able to add measurements to the line segments they draw onscreen. The program can then calculate Perimeter and Area on its own, and send the values to the spreadsheet which calculates material usage and estimates billable hours.


