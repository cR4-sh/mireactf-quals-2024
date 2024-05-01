import os
import re

from flask import Flask, render_template, request
from lxml import etree

app = Flask(__name__, template_folder="templates", static_folder="img")
XML_FILE_PATH = os.path.join(os.path.dirname(__file__), 'books.xml')

def get_books_from_xml(xml_data):
    title = xml_data.find('title').text
    author = xml_data.find('author').text
    year = xml_data.find('year').text
    book = (title, author, year)
    return book

def is_valid_xpath(query):
    forbidden_patterns = [
        r"/{2,}",          
        r"\[not\(",        
        r"\[contains\(",      
    ]

    if query == '/books/book':
        return False
    
    else:
        for pattern in forbidden_patterns:
            if re.search(pattern, query):
                return False
        
    return True

@app.route("/", methods=['GET', 'POST'])
def index():
    books = []
    message = ""
    if request.method == 'POST':
        query = request.form.get('query')
        if not is_valid_xpath(query):
            message = "Your XPath query is forbidden.  Please enter a valid XPath query."
        elif query.startswith('/'):
            try:
                xml_tree = etree.parse(XML_FILE_PATH)
                xml_books = xml_tree.xpath(query)
                books = [get_books_from_xml(xml) for xml in xml_books]
            except Exception as e:
                message = "An error occurred while processing your request."
        else:
            xml_tree = etree.parse(XML_FILE_PATH)
            filter_query = ".//book[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{}')]".format(query.lower())
            xml_books = xml_tree.xpath(filter_query)
            books = [get_books_from_xml(xml) for xml in xml_books if not xml.findtext('title').startswith("mireactf")]
    return render_template('index.html', books=books, message=message)

@app.route("/books")
def books():
    xml_tree = etree.parse(XML_FILE_PATH)
    xml_books = xml_tree.findall('.//book')
    filtered_books = [get_books_from_xml(xml) for xml in xml_books if not xml.findtext('title').startswith("mireactf")]
    return render_template('books.html', books=filtered_books)

@app.route("/secret")
def secret():
    xml_example = """
    <books>
        <book>
            <title>Structure</title>
            <author>of</author>
            <year>xml</year>
        </book>
    </books>
    """
    return render_template('secret.html', xml_example=xml_example)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
