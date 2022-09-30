# -*- coding: utf-8 -*-
import logging
from src.data.multiple_files_to_single_excel_file import SingleExcelFile
import numpy as np
import pandas as pd

log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)


class SalesETL:
    def __init__(self):
        self._logger = logging.getLogger('Sales ETL')

    def ETL(self, input_filepath):
        """
            Following piece of code converts different Excel files into one file with different sheets
            using multiple_files_to_single_excel_file.py. This is extraction part
            of ETL pipeline.

            :param input_filepath: directory path where source files exist
            :return: none

        """

        self._logger.info('Starting ETL process....')

        self._logger.info('Converting excel files into one excel file....')
        sales_etl = SingleExcelFile()
        sales_etl.multiple_to_single_xlsx_file(input_filepath)
        self._logger.info('sales_data.xlsx has been saved.')
        self._logger.info('All xlsx files added to data/interim/sales_data.xlsx')

        """
            Following piece of code converts those Excel sheets into different dataframes on which
            later transformations such as imputing missing values, dropping
            unnecessary columns, making new columns etc are applied. This is transformation
            part of ETL.

        """
        self._logger.info('Reading sales_data.xlsx')
        sales_data = 'data/interim/sales_data.xlsx'
        self._logger.info('Converting each sheet into separate pandas dataframe...')
        cust_add_df = pd.read_excel(sales_data, "CUSTOMERADDRESS")
        cust_df = pd.read_excel(sales_data, "CUSTOMERS")
        div_df = pd.read_excel(sales_data, "DIVISION")
        region_df = pd.read_excel(sales_data, "REGION")
        sales_data_df = pd.read_excel(sales_data, "SALESDATA")
        self._logger.info("Conversion finished")
        self._logger.info('Starting transformation..')
        self._logger.info('Removing unnecessary columns..  ')
        sales_data_df.drop('Unnamed: 20', axis=1, inplace=True)
        sales_data_df.drop('Unnamed: 21', axis=1, inplace=True)
        self._logger.info('Imputing missing values..')
        sales_data_df['Discount Amount'].fillna(sales_data_df['Discount Amount'].mean(), inplace=True)
        sales_data_df['Sales Price'].fillna(sales_data_df['Sales Price'].mean(), inplace=True)
        sales_data.replace(r'^\s*$', "0")
        sales_data_df['Item Class'].fillna("0", inplace=True)
        sales_data_df['Item Number'].fillna("0", inplace=True)
        cust_df.replace(r'^\s*$', "0", regex=True, inplace=True)
        cust_add_df.replace(r'^\s*$', "", regex=True, inplace=True)
        cust_add_df['State'].replace(np.NaN, "", inplace=True)
        self._logger.info('Finalizing Transformations..')
        cust_add_df['Full Address'] = cust_add_df['Customer Address 1'].astype('str') + ' ' + cust_add_df[
            'Customer Address 2'].astype('str') + \
                                      ' ' + cust_add_df['Customer Address 3'].astype('str') + ' ' + cust_add_df[
                                          'Customer Address 4'].astype('str') + \
                                      ' ' + cust_add_df['Zip Code'].astype('str') + ' ' + cust_add_df['City'].astype(
            'str') + ' ' + cust_add_df['State'].astype('str') + \
                                      ' ' + cust_add_df['Country'].astype('str')
        cust_add_df['Full Address'] = cust_add_df['Full Address'].str.strip()
        cust_add_df.replace(r'^\s*$', "0", regex=True, inplace=True)
        self._logger.info('Transformation Completed. Waiting for loading process to start..')

        """
            The processed dataframes are converted to Excel sheets back and saved in to data/processed/
            processed_data.xlsx. The final processed file is ready to be used for analysis. This is
            loading part of ETL.
        """

        self._logger.info('Starting loading Process..')
        with pd.ExcelWriter('data/processed/processed_data.xlsx', date_format='MM-DD-YYYY') as writer:
            sales_data_df.to_excel(writer, sheet_name='Sales_Data', index=False)
            region_df.to_excel(writer, sheet_name='Region', index=False)
            div_df.to_excel(writer, sheet_name='Division', index=False)
            cust_add_df.to_excel(writer, sheet_name='Customers_Address', index=False)
            cust_df.to_excel(writer, sheet_name='Customers', index=False)
        self._logger.info('Dataframes converted to Excel file and loaded in data/processed/processed_data.xlsx')


if __name__ == '__main__':
    pass
