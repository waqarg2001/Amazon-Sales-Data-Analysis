<p align='center'>
<img src='https://github.com/waqarg2001/Amazon-Sales-Data-Analysis/blob/master/src/Sales%20Data.png' width=600 height=170 >
</p>

---

<h4 align='center'> Application of ETL process on raw <a href='https://www.amazon.com/' target='_blank'>Aamazon</a> sales data along with its analysis using <a href='jupyter.org' target='_blank'>Jupyter</a> Notebook and <a href='tableau.com' target='_blank'>Tableau</a> for a dashboard. </h4>

<p align='center'>
<img src="https://i.ibb.co/KxfMMsP/built-with-love.png" alt="built-with-love" border="0">
<img src="https://i.ibb.co/MBDK1Pk/powered-by-coffee.png" alt="powered-by-coffee" border="0">
<img src="https://i.ibb.co/CtGqhQH/cc-nc-sa.png" alt="cc-nc-sa" border="0">
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#demo">Demo</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>


## Overview

<p><a href='Amazon.com' target='_blank'>Amazon</a> is the world's largest eCommerce website. It was originally launched as a book-selling website and sold its first book in 1995.</p>

This project involves Extract Transform Load(ETL) process on fictious raw sales data of Amazon. Exploratory Data Analysis(EDA) is done on it using Jupyter Notebook to extract key insights about the sales and later on a executive's sales dashbaord is produced using Tableau.

The repository directory structure is as follows:

├── LICENSE
├── README.md          <- The top-level README for developers using this project.
|
├── run.py             <- Python script to start ETL process.
|
├── data
│   ├── interim        <- Intermediate data that has been transformed using ETL process.
│   ├── processed      <- The final, canonical data set for analysis.
│   └── raw            <- The original, immutable data dump.
│
│
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-mwg-initial-data-exploration`.
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
|
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to perform ETL
│       ├── make_dataset.py
|       └── multiple_files_to_single_excel_file.py
|
|
├── dashboard          <- Dashboard created using transformed data.
|   └── Sales Dashboard.twbx 
|
├── resources          <- Resources for this readme file.
