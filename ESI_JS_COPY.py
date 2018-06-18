import pandas as pd
import numpy
import bs4 as bs
import urllib.request
import re
from selenium import webdriver
def fetching_ESI_JS_FROM_PAGE():
    data=pd.read_csv(r"C:\URLs.csv")
    dim_data=pd.read_csv(r"C:\cm_dim_data.csv")

    cm_dimension_id = []
    for cm_dim in dim_data['cm_dimension_id']:
        cm_dimension_id.append(cm_dim)


    dim_names = []
    for dim_nm in dim_data['dim_name']:
        dim_names.append(dim_nm)

    template_type = []
    for temp_item in dim_data['template_item_type']:
        template_type.append(temp_item)

    cm_dim_name = zip(cm_dimension_id, dim_names)
    cm_dim_name_dict = dict(cm_dim_name)
    #print(cm_dim_name_dict)

    cm_dim_temp = zip(cm_dimension_id, template_type)
    cm_dim_temp_dict = dict(cm_dim_temp)
    #print(cm_dim_temp_dict)

    for url_name in data['URL']:
        browser = webdriver.Firefox(executable_path="C:\\Users\\ankit.vashishth\\Downloads\\geckodriver.exe")
        browser.get(url_name)
        soup = bs.BeautifulSoup(browser.page_source, "html.parser")
        ESI_ad_unit = re.findall(r"<!-- \d{6}", str(soup))
        JS_ad_unit = re.findall(r"data-slot=\"\d{6}", str(soup))

        for esi_ad_unit_id in ESI_ad_unit:
            esi_ad_unit_id=esi_ad_unit_id.strip('<!-')
            esi_ad_unit=esi_ad_unit_id.strip()

            if (int(esi_ad_unit)) in cm_dim_name_dict.keys():
                print('URL is {} || ESI ad-unit id is {} || Dimension name is {}  & Item Type is {}'.format(url_name,esi_ad_unit,cm_dim_name_dict[int(esi_ad_unit)],cm_dim_temp_dict[int(esi_ad_unit)]))


        for js_ad_unit_id in JS_ad_unit:
            js_ad_unit_id=js_ad_unit_id.strip('data-slot= " "')
            js_ad_unit=js_ad_unit_id.strip()

            if (int(js_ad_unit)) in cm_dim_name_dict.keys():
                print('URL is {} || JS ad-unit {}|| Dimension name is {} & Item Type is {}'.format(url_name,js_ad_unit,cm_dim_name_dict[int(js_ad_unit)],cm_dim_temp_dict[int(js_ad_unit)]))


fetching_ESI_JS_FROM_PAGE()
