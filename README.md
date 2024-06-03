# Linda Data Project
## by Nathan Goodroe

This is a project from multiple csv all the way through to final findings.

## Social Security Data

https://www.ssa.gov/oact/babynames/limits.html

Access to Baby names from the past 100+ years with any name that recieved >4 uses each year.
Each download comes as a single year csv in a large folder with hundreds of csvs.

## Python

The first file is the combine.py which is where I took the multiple csv from the Social security administration and was able to put them into one file so that I could then load them into my SQL (Postgres) server and be able to do work on it.

*Some later py files were from taking data after the SQL step and creating animations in MatPlotLib. These were successful but not ultimately used in the Youtube video.

## SQL

Once in Postgres I ran a number of different commands to try and find some interesting things, look for a story in the data and pull out any kind of details that might be of note.

I settled on the name Linda and the story around it.

Those were then exported into their own csvs and subsequently loaded into Tableua for visualizations.

## Tableau

Graphs were made in Tableau and put on a final graphic found at https://public.tableau.com/views/TheHistoryoftheNameLinda/LindaDashboard?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link

## Youtube

Then I took the visualizations and explained the foundings at https://youtu.be/tGr4HzKR_co?si=H_qkPSomJ32GtzFc

