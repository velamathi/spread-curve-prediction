import numpy as np 
import pandas as pd
from numpy import random
import xml.etree.ElementTree as et



x = pd.DataFrame(np.random.random((10,16)), 
                 columns=['a','b','c', 'd', 
                          'gradeDetail',
                            'gradeRecordId',
                            'loanId',
                            'facilityId',
                            'defaultGrade',
                            'effectiveDate',
                            'facilityGrade',
                            'facilityId',
                            'graderecordId',
                            'loanId',
                            'lossGivenDefault',
                            'factorDetails',
                         ])

def factor_xml_builder(df, root):
    # fetching tags from the dataframe 
    tags = df.columns.tolist() 

    # iteratinga over datas in the dataframe
    factor = et.SubElement(root, 'factor')
    df_dict = df.to_dict()
    for tag in tags:
            val = et.SubElement(factor, str(tag))
            val.text = str((df_dict.get(tag,None)).get(0) )
    
    
    return root

def builder(x, root):
    for model in x.itertuples():
        gradeDetail = et.SubElement(root,'gradeDetail')
        gradeRecordId = et.SubElement(gradeDetail,'gradeRecordId')
        gradeRecordId.text = str(model.gradeRecordId)
        loanId = et.SubElement(gradeDetail,'loanId')
        loanId.text = str(model.loanId)
        facilityId = et.SubElement(gradeDetail,'facilityId')
        facilityId.text = str(model.facilityId)
        defaultGrade = et.SubElement(gradeDetail,'defaultGrade')
        defaultGrade.text = str(model.defaultGrade)
        effectiveDate = et.SubElement(gradeDetail,'effectiveDate')
        effectiveDate.text = str(model.effectiveDate)
        facilityGrade = et.SubElement(gradeDetail,'facilityGrade')
        facilityGrade.text = str(model.facilityGrade)
        facilityId = et.SubElement(gradeDetail,'facilityId')
        facilityId.text = str(model.facilityId)
        loanId = et.SubElement(gradeDetail,'loanId')
        loanId.text = str(model.loanId)
        lossGivenDefault = et.SubElement(gradeDetail,'lossGivenDefault')
        lossGivenDefault.text = str(model.lossGivenDefault)
        factorDetails = et.SubElement(gradeDetail,'factorDetails')
        factor_columns = ['a','b','c']
        factorDetails = factor_xml_builder(pd.DataFrame.from_records([model[1:5]], 
                                                                     columns=list('abcd')),
                                           factorDetails
                                          )
    return root


pdmodelRes = et.Element('pdmodelRes')
gradeDetails = et.SubElement(pdmodelRes,'gradeDetails')
gradeDetails = builder(x, gradeDetails)
et.dump(pdmodelRes)
