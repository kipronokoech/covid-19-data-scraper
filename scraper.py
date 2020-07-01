import requests
import lxml.html as lh
import pandas as pd
import numpy as np
def aims(url):
    page = requests.get(url)  # Store the contents of the website under doc
    doc = lh.fromstring(page.content)  # Parse data that are stored between <tr>..</tr> of HTML
    # Lets go through the columns
    tr_elements = doc.xpath('//tr')  # Create empty list
    col = []
    i = 0  # For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        col.append((name, []))

    # Since out first row is the header, data is stored on the second row onwards
    for j in range(1, len(tr_elements)):
        # T is our j'th row
        T = tr_elements[j]

        # If row is not of size 10, the //tr data is not from our table
        if len(T) != 19:
            break

        # i is the index of our column
        i = 0

        # Iterate through each element of the row
        for t in T.iterchildren():
            data = t.text_content()
            # Check if row is empty
            if i > 0:
                # Convert any numerical value to integers
                try:
                    data = int(data)
                except:
                    pass
            # Append the data to the empty list of the i'th column
            col[i][1].append(data)
            # Increment i for the next column
            i += 1

    Dict = {title: column for (title, column) in col}
    df = pd.DataFrame(Dict)
    data = df[df["#"] != ""].reset_index(drop=True)
    data = data.drop_duplicates(subset=["Country,Other"])

    cols = ['#',
            'Tot\xa0Cases/1M pop',
            'Deaths/1M pop',
            'Tests/\n1M pop\n',
            'Population',
            'Continent',
            '1 Caseevery X ppl',
            '1 Deathevery X ppl',
            '1 Testevery X ppl']

    data_final = data.drop(cols, axis=1)
    c = ["South Africa", "Rwanda", "Senegal", "Ghana", "Cameroon"]
    data = data_final[data_final["Country,Other"].isin(c)].reset_index(drop=True)
    #['Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths',
    # 'TotalRecovered', 'NewRecovered', 'ActiveCases', 'Serious,Critical', 'TotalTests']
    col_al =  list(data.columns)
    col_al.remove('Country,Other')
    data[col_al] = data[col_al].astype(str)

    def recode_empty_cells(dataframe, list_of_columns):

        for column in list_of_columns:
            dataframe[column] = dataframe[column].map(lambda x: x.replace(",",""))
            dataframe[column] = dataframe[column].map(lambda x: x.replace("+", ""))
            dataframe[column] = dataframe[column].replace('', np.nan, regex=True)
            dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')
            #dataframe[column] = dataframe[column].astype("int64")


        return dataframe
    data = recode_empty_cells(data,col_al)

    #data['TotalCases'] = data['TotalCases'].astype("int64")
    # data["NewCases"].astype("int64")
    # data["TotalDeaths"].astype("int64")
    return data.set_index("Country,Other")

def world(url):
    page = requests.get(url)  # Store the contents of the website under doc
    doc = lh.fromstring(page.content)  # Parse data that are stored between <tr>..</tr> of HTML
    # Lets go through the columns
    tr_elements = doc.xpath('//tr')  # Create empty list
    col = []
    i = 0  # For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        col.append((name, []))

    # Since out first row is the header, data is stored on the second row onwards
    for j in range(1, len(tr_elements)):
        # T is our j'th row
        T = tr_elements[j]

        # If row is not of size 10, the //tr data is not from our table
        if len(T) != 19:
            break

        # i is the index of our column
        i = 0

        # Iterate through each element of the row
        for t in T.iterchildren():
            data = t.text_content()
            # Check if row is empty
            if i > 0:
                # Convert any numerical value to integers
                try:
                    data = int(data)
                except:
                    pass
            # Append the data to the empty list of the i'th column
            col[i][1].append(data)
            # Increment i for the next column
            i += 1

    Dict = {title: column for (title, column) in col}
    df = pd.DataFrame(Dict)
    data = df[df["#"] != ""].reset_index(drop=True)
    data = data.drop_duplicates(subset=["Country,Other"])

    cols = ['#',
            'Tot\xa0Cases/1M pop',
            'Deaths/1M pop',
            'Tests/\n1M pop\n',
            'Population',
            'Continent',
            '1 Caseevery X ppl',
            '1 Deathevery X ppl',
            '1 Testevery X ppl']

    data_final = data.drop(cols, axis=1)
    data_final = data_final[data_final["Country,Other"] != "Country,Other"]
    col_al = list(data_final.columns)
    col_al.remove('Country,Other')
    data_final[col_al] = data_final[col_al].astype(str)

    def recode_empty_cells(dataframe, list_of_columns):

        for column in list_of_columns:
            dataframe[column] = dataframe[column].map(lambda x: x.replace(",", ""))
            dataframe[column] = dataframe[column].map(lambda x: x.replace("+", ""))
            dataframe[column] = dataframe[column].replace('', np.nan, regex=True)
            dataframe[column] = pd.to_numeric(dataframe[column], errors='coerce')
            # dataframe[column] = dataframe[column].astype("int64")

        return dataframe

    data_ = recode_empty_cells(data_final, col_al)
    return data_.set_index("Country,Other")
if __name__ == "__main__":

    url = "https://www.worldometers.info/coronavirus/"
    page = requests.get(url)#Store the contents of the website under doc
    doc = lh.fromstring(page.content)#Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')

    print(len(list(tr_elements)))

    #Lets go through the columns
    tr_elements = doc.xpath('//tr')#Create empty list
    col=[]
    i=0#For each row, store each first element (header) and an empty list
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
        print('%d:"%s"'%(i,name))
        col.append((name,[]))

    # Since out first row is the header, data is stored on the second row onwards
    for j in range(1, len(tr_elements)):
        # T is our j'th row
        T = tr_elements[j]

        # If row is not of size 10, the //tr data is not from our table
        if len(T) != 19:
            break

        # i is the index of our column
        i = 0

        # Iterate through each element of the row
        for t in T.iterchildren():
            data = t.text_content()
            # Check if row is empty
            if i > 0:
                # Convert any numerical value to integers
                try:
                    data = int(data)
                except:
                    pass
            # Append the data to the empty list of the i'th column
            col[i][1].append(data)
            # Increment i for the next column
            i += 1

    #ideally all columns must have the same number of rows
    print([len(C) for (title,C) in col])

    Dict = {title:column for (title,column) in col}
    df = pd.DataFrame(Dict)
    data = df[df["#"]!=""].reset_index(drop=True)
    data = data.drop_duplicates(subset = ["Country,Other"])

    cols = ['#',
     'Tot\xa0Cases/1M pop',
     'Deaths/1M pop',
     'Tests/\n1M pop\n',
     'Population',
     'Continent',
     '1 Caseevery X ppl',
     '1 Deathevery X ppl',
     '1 Testevery X ppl']

    data_final = data.drop(cols,axis=1)
    c = ["South Africa" , "Rwanda","Senegal","Ghana","Cameroon"]
    data = data_final[data_final["Country,Other"].isin(c)].reset_index(drop=True)
    print(data.columns)