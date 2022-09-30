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

"""
├── LICENSE <br>
├── README.md          <- The top-level README for developers using this project. <br>
| <br>
├── run.py             <- Python script to start ETL process. <br>
| <br>
├── data
│   ├── interim        <- Intermediate data that has been transformed using ETL process. <br>
│   ├── processed      <- The final, canonical data set for analysis. <br>
│   └── raw            <- The original, immutable data dump. <br>
│ <br>
│ <br>
│ <br>
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),<br>
│                         the creator's initials, and a short `-` delimited description, e.g.<br>
│                         `1.0-mwg-initial-data-exploration`. <br>
│ <br>
│ <br>
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.<br>
│                         generated with `pip freeze > requirements.txt` <br>
| <br>
│ <br>
├── src                <- Source code for use in this project. <br>
│   ├── __init__.py    <- Makes src a Python module. <br>
│   │ <br>
│   ├── data           <- Scripts to perform ETL. <br>
│       ├── make_dataset.py <br>
|       └── multiple_files_to_single_excel_file.py <br>
| <br>
| <br>
├── dashboard          <- Dashboard created using transformed data. <br>
|   └── Sales Dashboard.twbx <br>
| <br>
├── resources          <- Resources for this readme file. <br>
"""
