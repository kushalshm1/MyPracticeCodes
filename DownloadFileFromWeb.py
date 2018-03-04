from urllib import request #different way to import

drive_url = 'http://www.sample-videos.com/csv/Sample-Spreadsheet-1000-rows.csv'

def download_pdf_file(file_url):
    #Connect
    response = request.urlopen(file_url)
    file = response.read()
    #Save as a string
    file_str = str(file)
    lines = file_str.split("\\n")
    #Make a file
    dest_url = r'goog.csv'
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")

download_pdf_file(drive_url)
