import xml.etree.ElementTree as ET 
root = ET.Element('root') 
ET.dump(root) 
book = ET.Element('book') 
root.append(book) 
ET.dump(root)
name = ET.SubElement(book, 'name') 
name.text  = 'Book1'  
ET.dump(root) 
