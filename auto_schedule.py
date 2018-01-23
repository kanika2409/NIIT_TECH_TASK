from itertools import zip_longest
import xlrd
import requests
import os
import pandas as pd

def automateType1(url):
    r = requests.get(url)
    with open("bcb_input_10.xlsx", "wb") as code:
        code.write(r.content)
    rb2 = xlrd.open_workbook('bcb_input_1.xlsx') ##### old xls file in current path
    rb1 = xlrd.open_workbook('bcb_input_20.xlsx') #### new file dowloaded from the url
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
        os.rename('bcb_input_20.xlsx','bcb_input_2 .xlsx')
            
        return dumy_out_2
            
   
if __name__=="__main__":       
        output1=automateType1('http://www.bcb.gov.br/pec/Indeco/Ingl/ie5-24i.xlsx')
        output2=automateType2('http://www.bcb.gov.br/pec/Indeco/Ingl/ie5-26i.xlsx')
        file1=pd.read_csv('bcb_output_1.csv')
        file1.loc[len(file1)]=['1/'+str(int(output1[0]))+'/2018',output1[1],output1[2],output1[3],output1[4],output1[5],output1[6],output1[7],output1[8],output1[9],output1[10]] ### final output save with date
        os.remove('bcb_output_1.csv')
        file1.to_csv('bcb_output_1.csv')
        ###### For 2nd output arrangement
        file2=pd.read_csv("bcb_output_2.csv")
        
        if output2[0] == 'Jan':
            file2.loc[len(file2)] = ['01/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Feb':
            file2.loc[len(file2)] = ['02/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Mar':
            file2.loc[len(file2)] = ['03/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Apr':
            file2.loc[len(file2)] = ['04/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'May':
            file2.loc[len(file2)] = ['05/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Jun':
            file2.loc[len(file2)] = ['06/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Jul':
            file2.loc[len(file2)] = ['07/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Aug':
            file2.loc[len(file2)] = ['08/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Sep':
            file2.loc[len(file2)] = ['09/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Oct':
            file2.loc[len(file2)] = ['10/'+'01'+'/2018',output2[1]]
        elif output2[0] == 'Nov':
            file2.loc[len(file2)] = ['11/'+'01'+'/2018',output2[1]]
        else:
            file2.loc[len(file2)] = ['12/'+'01'+'/2018',output2[1]]
        
        os.remove('bcb_output_2.csv')
        file2.to_csv('bcb_output_2.csv')
            
        


