# nwsl-fantasy-helper
A repository of utilities for NWSL fantasy

## Current State of the Project (8/17/2022)
I wanted to move away from scraping after the debacle with CSS tags changings names on FBref last week. We also wanted to move the project towards using Fotmob, since it has more available data than FBref. There is an unofficial Fotmob API with javascript and python wrappers (on npm and pypi). However, neither of these are working as expected at the moment (and for context, the latest release of the npm package was 3/2021). 

So it's back to web scraping, trying to scrape Fotmob in a way that doesn't make me hate football, and maybe using Rust just for fun. 
