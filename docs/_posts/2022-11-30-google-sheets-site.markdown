---
layout: post
title:  "Generate Proposals with Google Sheets, App Script, Vue, & Vuetify"
categories: 
excerpt: Yeah, I'm a full stack developer 😎
---

[Link to the Project README](https://github.com/radiosketch/edu/tree/master/Software%20Engineering/Websites/google_sheets_site)

&emsp;In an effort to help streamline customer interactions, I've been tasked with making a webapp for generating proposals which can be sent directly to clients of my employer.   

&emsp;The initial project was a proof of concept containing basic forms for getting and setting fields contained within the Sheet database. To prevent the user from changing the datatype of a cell entirely, the edit form, shown in yellow, checks the datatype of the cell selected for editing. The form will not let a request go through until the input matches a regex that corresponds to the cell data format.  

&emsp;The app as it exists today contains a dropdown menu which allows the user to search for a product or service in the database and edit its related fields. Formulaic fields are not shown in the dropdown and thus are not editable.  

![Image of Site](https://cdn.discordapp.com/attachments/513555424247676929/1047719161020825630/image.png)

&emsp;In the future, these products and their respective fields will be edited during the process of making an inspection. Answering basic questions about the job site, and more interactive methods will be used to draw conclusions about which materials and services are required for a particular job.

## Intuitive Estimates with Blueprints  

&emsp;When inspecting a crawlspace, measurements need to be taken to calculate material costs and estimate the amount of labor required to complete the job. I propose a method of making simple blueprints since making the calculations by hand is slow and unintuitive to perform in the field. Shown below is a current view of the demo for this idea.

![Image of Crawlspace Calculator Demo](https://cdn.discordapp.com/attachments/513555424247676929/1047718048741728306/image.png)  

&emsp;Eventually the user will be able to add measurements to the line segments they draw onscreen. The program can then calculate Perimeter and Area on its own, and send the values to the spreadsheet which calculates material usage and estimates billable hours.


