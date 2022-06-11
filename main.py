from bs4 import BeautifulSoup
html = ''' 
<html>
<head>
<style>
.myDiv {
  border: 5px outset red;
  background-color: lightblue;
  text-align: center;
}
</style>
</head>
<body>
<div id="first">
    <h3 data-example="yes">hi</h3> 
</div>
<div class="myDiv">
  <h2>This is a heading in a div element...Javed</h2>
  <p>This is some text in a div element....Javed</p>
</div>
<ol>
    <li class ="special"> This list item is special. </li>
    <li> This list item is not special. </li>
    <li class ="special"> This list item is special. </li>
</ol>
<div class="myDiv">
  <h3>This is a heading in a div element...Sajid</h3>
  <p>This is some text in a div element....Sajid</p>
</div>
<div data-example="yes">bye</div>

<h1 id="myHeader">Hello World!...Javed</h1>
<button onclick="displayResult()">Change text</button>

<h2 id="myHeader">Hello World!...Sajid</h2>
<button onclick="displayResult()">Rename text</button>

</body>
</html> 
'''
soup = BeautifulSoup(html, "html.parser")

# find & find_all & select :

div_single = soup.find("div")   #Will find ony 1st element since used find method
print(div_single)

div_all = soup.find_all("div")   #Will find all elements since used find_all method
print(div_all)

# Find using CSS Tag Name :

css_tag = soup.select("div")    # Imp : select Will always find all elements unless specified index as below
print(css_tag)

css_tag_first_element = soup.select("div")[0]   #This will give only 1st element
print(css_tag_first_element)

css_tag_second_element = soup.select("div")[1]  #This will give only 2nd element
print(css_tag_second_element)

# Find using ID :

id_single = soup.find(id="myHeader")  #Will find ony 1st element since used find method
print(id_single)

id_all = soup.find_all(id="myHeader")#Will find all elements since used find_all method
print(id_all)

# Find using CSS ID :

css_id = soup.select("#myHeader")  # Imp : select Will always find all elements unless specified index as below
print(css_id)

css_id_first_element = soup.select("#myHeader")[0]  #This will give only 1st element
print(css_id_first_element)

css_id_second_element = soup.select("#myHeader")[1]  #This will give only 2nd element
print(css_id_second_element)

# Find using Class :

class_single = soup.find(class_="myDiv")  #Will find ony 1st element since used find method
print(class_single)

class_all = soup.find_all(class_="myDiv") #Will find all elements since used find_all method
print(class_all)

# Find using CSS Class :

css_class = soup.select(".myDiv")    # Imp : select Will always find all elements unless specified index as below
print(css_class)

css_class_first_element = soup.select(".myDiv")[0]  #This will give only 1st element
print(css_class_first_element)

css_class_second_element = soup.select(".myDiv")[1]  #This will give only 2nd element
print(css_class_second_element)

# Find using a specific attribute :

atrribute_find_single = soup.find(attrs={"onclick":"displayResult()"})
#Will find only 1st elements since  used find method

print(atrribute_find_single)

atrribute_find_all = soup.find_all(attrs={"onclick":"displayResult()"})
#Will find all elements since used find_all method

print(atrribute_find_all)

# Find using CSS Attribute :

css_attr = soup.select("[onclick]")  # Imp : select Will always find all elements unless specified index as below  ..Need to give in form of list
print(css_attr)

css_attr_first_element = soup.select("[onclick]")[0]   #This will give only 1st element..Need to give in form of list
print(css_attr_first_element)

css_attr_second_element = soup.select("[onclick]")[1]   #This will give only 2nd element..Need to give in form of list
print(css_attr_second_element)

# Accessing Data in Elements:

# get_text --> Access the inner text in an element

# css_id_text = soup.select("#myHeader").get_text()     #Does Not Works # Imp : select Will always find all elements unless specified index as below
# print(css_id_text)      #Here, instead of printing text, it will throw an error bcoz it is required to pass index to get text

css_id_first_element_text = soup.select("#myHeader")[0].get_text()  #This will give only 1st element
print(css_id_first_element_text)

css_id_second_element_text = soup.select("#myHeader")[1].get_text()  #This will give only 2nd element
print(css_id_second_element_text)

# name --> Tag Name

# css_class_name = soup.select(".myDiv").name    #Does Not Works # Imp : select Will always find all elements unless specified index as below
# print(css_class_name)   #Here, instead of printing name i.e.,tag, it will throw an error bcoz it is required to pass index to get tag


css_class_first_element_name = soup.select(".myDiv")[0].name  #This will give only 1st element
print(css_class_first_element_name)

css_class_second_element_name = soup.select(".myDiv")[1].name  #This will give only 2nd element
print(css_class_second_element_name)

# attrs --> Dictionary of Attributes  --> Dictionary containing Key-Value pairs for the attributes on each item.

attrs = soup.find("button").attrs   #Cannot use find_all method, only find method works here.
print(attrs)     #This Method will return a Dictionary of Key-Value Pairs
# O/P --> {'onclick': 'displayResult()'}

# You can also access Attributes values using Brackets as shown below!!

attrs = soup.find("button")["onclick"]   #onclick --> Key Here
print(attrs)    #In this method, we specify key using Square Brackets and it will return Value
# O/P --> displayResult() ---> Value Returned

#Navigating with BeautifulSoup

# print(soup.body)
# print(soup.body.div)

# using contents keyword:

# print(soup.body.contents)  #soup.body.contents will print all content inside the body
data1 = soup.body.contents[1] #soup.body.contents[1] will print 1st content inside the body
print(data1)

data2 = soup.body.contents[1].contents #soup.body.contents[1].contents will print next content
print(data2)

# using next_sibling keyword:   #ignore this, better method available down in find_next_sibling()

data3 = soup.body.contents[1].next_sibling.next_sibling  #soup.body.contents[1].next_sibling.next_sibling will print next to next sibling
# We have used .next_sibling 2 times since on 1st .next_sibling it is having a new line, so ideally nothing is being printed, so using one more time .next_sibling to get next sibling data.
print(data3)

# using parent keyword:

data4 = soup.find(class_="myDiv").parent   #will give entire data of that particular class
print(data4)

data5 = soup.find(class_="myDiv").parent.parent   #will give entire body of that particular class
print(data5)

parent_data = soup.find(id="first").find_parent()  #will search until it finds the parent with id="first" and return that data to us.
print(parent_data)

# find_next_sibling() keyword:

data6 = soup.find(id="myHeader").find_next_sibling()  #find_next_sibling() will ignore new line as above problem existed and give entire element for the defined.
print(data6)

data7 = soup.find(id="myHeader").find_next_sibling().find_next_sibling()  #Next 2 siblings
print(data7)

data8 = soup.find(id="myHeader").find_next_sibling().find_next_sibling().find_next_sibling()  #Next 3 siblings
print(data8)

# find_next_sibling() keyword with a defined term:

data9 = soup.find(class_="special")  #...Since used Find will only get 1 result.
print(data9)   #O/P -->   <li class="special"> This list item is special. </li>

data10 = soup.find(class_="special").find_next_sibling()      #Finding Next Sibling.
print(data10)   #O/P -->    <li> This list item is not special. </li>

data11 = soup.find(class_="special").find_next_sibling(class_="special")  #Finding Next Sibling with the class of "special"
print(data11)  #O/P -->   <li class="special"> This list item is special. </li>

data12 = soup.select("[onclick]")[0]
print(data12)  # O/P -->   <button onclick="displayResult()">Change text</button>

data13 = soup.select("[onclick]")[0].find_next_sibling().find_next_sibling()
print(data13)    # O/P -->  <button onclick="displayResult()">Rename text</button>

# find_previous_sibling() keyword:

data14 = soup.select("#myHeader")[1].find_previous_sibling()  #This will find one sibling back to defined.
print(data14)

data15 = soup.select("[onclick]")[1]
print(data15)   # O/P -->  <button onclick="displayResult()">Rename text</button>

data16 = soup.select("[onclick]")[1].find_previous_sibling().find_previous_sibling()
print(data16)   # O/P -->  <button onclick="displayResult()">Change text</button>

