#from itertools import zip_longest
from itertools import izip_longest as zip_longest
import xlrd
import requests
import os

def automateType1(url):
    r = requests.get(url)
    with open("bcb_input_10.xlsx", "wb") as code:
        code.write(r.content)
    rb2 = xlrd.open_workbook('bcb_input_1.xlsx') ##### old xls file in current path
    rb1 = xlrd.open_workbook('bcb_input_10.xlsx') #### new file dowloaded from the url
    dumy_out=[]
    sheet1 = rb1.sheet_by_index(0)
    sheet2 = rb2.sheet_by_index(0)

    for rownum in range(max(sheet1.nrows, sheet2.nrows)):
        if rownum < sheet1.nrows:
            row_rb1 = sheet1.row_values(rownum)
            row_rb2 = sheet2.row_values(rownum)

            for colnum, (c1, c2) in enumerate(zip_longest(row_rb1, row_rb2)):
                if c1 != c2:
                    print (rownum)
                    print (c2)
                    dumy_out.append(c2) #### 
                #print("Row {} Col {} - {} != {}".format(rownum+1, colnum+1, c1, c2))
                
        else:
            print("Row {} missing".format(rownum+1))
            
    os.remove('bcb_input_1.xlsx')
    os.rename('bcb_input_10.xlsx','bcb_input_1.xlsx')
            
    return dumy_out ##### returning the change between two files

def automateType2(url):
        r = requests.get(url)
        with open("test1.xlsx", "wb") as code:
            code.write(r.content)
        rb2 = xlrd.open_workbook('bcb_input_2.xlsx')##### old xls file in current path
        rb1 = xlrd.open_workbook('bcb_input_20.xlsx')#### new file dowloaded from the url
        dumy_out_2=[]
        sheet1 = rb1.sheet_by_index(0)
        sheet2 = rb2.sheet_by_index(0)

        for rownum in range(max(sheet1.nrows, sheet2.nrows)):
            if rownum < sheet1.nrows:
                row_rb1 = sheet1.row_values(rownum)
                row_rb2 = sheet2.row_values(rownum)

                for colnum, (c1, c2) in enumerate(zip_longest(row_rb1, row_rb2)):
                    if c1 != c2:
                        dumy_out_2.append(c2)
                #print("Row {} Col {} - {} != {}".format(rownum+1, colnum+1, c1, c2))
                
            else:
                print("Row {} missing".format(rownum+1))
                
        os.remove('bcb_input_2.xlsx')
        os.rename('bcb_input_20.xlsx','bcb_input_2.xlsx')
            
        return dumy_out_2
            
   
if __name__=="__main__":
        try:     
            output1=automateType1('http://www.bcb.gov.br/pec/Indeco/Ingl/ie5-24i.xlsx')
            output2=automateType2('http://www.bcb.gov.br/pec/Indeco/Ingl/ie5-26i.xlsx')
        except:
            print("file execution done")


