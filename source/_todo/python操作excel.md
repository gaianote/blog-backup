```python
import os  
import xlrd  
from datetime import date,datetime  
  
#打开Excel文件  
workbook = xlrd.open_workbook('09-10.11-38-12-HTTP-GOOD-1-Lte1sDataStat_Charts.xlsx')  
  
#输出Excel文件中所有sheet的名字  
print workbook.sheet_names()  
  
#根据sheet索引或者名称获取sheet内容  
Data_sheet    = workbook.sheets()[0]  
CdfData_sheet = workbook.sheet_by_index(1)  
Charts_sheet  = workbook.sheet_by_name(u'Charts')  
  
#获取sheet名称、行数和列数  
print (Data_sheet.name,    Data_sheet.nrows,    Data_sheet.ncols)
  
#获取整行和整列的值（列表）      
rows = Data_sheet.row_values(0) #获取第一行内容  
cols = Data_sheet.col_values(1) #获取第二列内容  
#print rows  
#print cols  
  
#获取单元格内容  
cell_A1 = Data_sheet.cell(0,0).value  
cell_C1 = Data_sheet.cell(0,2).value  
cell_B1 = Data_sheet.row(0)[1].value  
cell_D2 = Data_sheet.col(3)[1].value  
print cell_A1, cell_B1, cell_C1, cell_D2  
  
#获取单元格内容的数据类型  
#ctype:0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error  
print 'cell(0,0)数据类型:', Data_sheet.cell(0,0).ctype  
print 'cell(1,0)数据类型:', Data_sheet.cell(1,0).ctype  
print 'cell(1,1)数据类型:', Data_sheet.cell(1,1).ctype  
print 'cell(1,2)数据类型:', Data_sheet.cell(1,2).ctype  
  
#获取单元格内容为日期的数据  
date_value = xlrd.xldate_as_tuple(Data_sheet.cell_value(1,0),workbook.datemode)  
print date_value  
print '%d:%d:%d' %(date_value[3:])  
  
d = {'11:25:59':[1, 2, 3], '11:26:00':[2, 3, 4], '11:26:01':[3, 4, 5]}  
print d['11:25:59']  
print d['11:26:00']  
print d['11:26:01']  
  
print d['11:25:59'][0]  
print d['11:26:00'][0]  
print d['11:26:01'][0]  

```