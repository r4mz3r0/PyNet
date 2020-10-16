def create_bucket(bucket): 
    print(bucket) 
    XML = ET.Element('CreateBucketConfiguration') 
    XML.attrib['xmlns'] = ns 
    location = ET.SubElement(XML, 'LocationConstraint') 
    location.text = auth.region 
    data = ET.tostring(XML, encoding='utf-8') 
    url = 'http://{}.{}'.format(bucket, endpoint) 
    xml_pprint(data) 
    response = requests.put(url, data=data, auth=auth) 
    print(response) 
    if(response.ok): 
        print('Created bucket {} OK'.format(bucket)) 
    else: 
        xml_pprint(response.text) 

