import xml.etree.ElementTree as ET

def parse_log(asked_xml):
    root = ET.fromstring(asked_xml)
    el = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')
    func = None
    func_tag = None
    for funcTag in el:
        #print(f'<----{funcTag.tag}---->')
        func = funcTag.tag.split('WMLS_')[-1]
        func_tag = funcTag
    if func == "GetFromStore":
        type_in = func_tag.find("WMLtypeIn").text
        query_in = func_tag.find("QueryIn").text
        options_in = func_tag.find("OptionsIn").text
        return {
            "type_in":type_in,
            "query_in":query_in,
            "options_in": options_in
            }