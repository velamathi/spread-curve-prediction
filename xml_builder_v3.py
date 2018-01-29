import numpy as np
import pandas as pd
import xml.etree.ElementTree as et

#Global Model Version Coeffecient
model_version_coeff = {
                        'Client UCN':                           '0.5451',
                        'Grading FICO Y/N':                     '1.54541',
                        'Client FICO':                          '4.52152',
                        'Client FICO Substitute Indicator':     '7.265',
                      }

factor_columns =  ['Client UCN',
                   'Grading FICO Y/N',
                   'Client FICO',
                   'Client FICO Substitute Indicator',
                   'Aggregate Loan Balance',
                   'Property Count',
                   'Estimated Aggregate Property Value',
                   'Estimated Aggregate LTV',
                   'Estimated Aggregate NOI',
                   'Estimated Aggregate DCR',
                   'House Price Appreciation',
                   'Months Since 30+ Delinquent',
                   'Negative Amortization Balance',
                   'MONTHS ON BOOK',
                   'REMAINING MATURITY TERM',
                   'MODEL VERSION',
                   'PD MODEL SCORE',
                   'INTERCEPT',
                   'NEAR CORE MARKET',
                   'NON CORE MARKET',
                   'CLIENT FICO (NORMALIZED)',
                   'INDICATOR FOR CLIENT FICO IS MISSING',
                   'ESTIMATED CONCURRENT LTV (NORMALIZED)',
                   'ESTIMATED CONCURRENT DCR (NORMALIZED)',
                   'ESTIMATED CONCURRENT DCR BELOW THRESHOLD',
                   'MONTHS SINCE 30+ DELINQUENT (NORMALIZED)',
                   'INDICATOR FOR MONTHS SINCE DELINQUENT',
                   'REMAINING MATURITY TERM 1 (TRANSFORMED)',
                   'REMAINING MATURITY TERM 2 (TRANSFORMED)',
                   'NEGAM TO LOAN BALANCE',
                   'HOUSE PRICE APPRECIATION (NORMALIZED)',
                   'NOI CHANGE (NORMALIZED)',
                   'INDICATOR FOR MULTIFAMLIY PROPERTY',
                   'SEASONING CURVE 1',
                   'SEASONING CURVE 2',
                   'INDICATOR FOR 2+PPD',
                   ]


x = pd.DataFrame(np.random.random((10, 48)),
                 columns=['Client UCN',
                           'Grading FICO Y/N',
                           'Client FICO',
                           'Client FICO Substitute Indicator',
                           'Aggregate Loan Balance',
                           'Property Count',
                           'Estimated Aggregate Property Value',
                           'Estimated Aggregate LTV',
                           'Estimated Aggregate NOI',
                           'Estimated Aggregate DCR',
                           'House Price Appreciation',
                           'Months Since 30+ Delinquent',
                           'Negative Amortization Balance',
                           'MONTHS ON BOOK',
                           'REMAINING MATURITY TERM',
                           'MODEL VERSION',
                           'PD MODEL SCORE',
                           'INTERCEPT',
                           'NEAR CORE MARKET',
                           'NON CORE MARKET',
                           'CLIENT FICO (NORMALIZED)',
                           'INDICATOR FOR CLIENT FICO IS MISSING',
                           'ESTIMATED CONCURRENT LTV (NORMALIZED)',
                           'ESTIMATED CONCURRENT DCR (NORMALIZED)',
                           'ESTIMATED CONCURRENT DCR BELOW THRESHOLD',
                           'MONTHS SINCE 30+ DELINQUENT (NORMALIZED)',
                           'INDICATOR FOR MONTHS SINCE DELINQUENT',
                           'REMAINING MATURITY TERM 1 (TRANSFORMED)',
                           'REMAINING MATURITY TERM 2 (TRANSFORMED)',
                           'NEGAM TO LOAN BALANCE',
                           'HOUSE PRICE APPRECIATION (NORMALIZED)',
                           'NOI CHANGE (NORMALIZED)',
                           'INDICATOR FOR MULTIFAMLIY PROPERTY',
                           'SEASONING CURVE 1',
                           'SEASONING CURVE 2',
                           'INDICATOR FOR 2+PPD',
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


def factor_xml_builder(data_tuple, tag_names, root_node):
    """Building SubElement XML from the Tuples"""
    sortorder           = 0
    for value, tag in zip(list(data_tuple), tag_names):
        factor          = et.SubElement(root_node, 'factor')
        sortorder       += 1
        tag_name        = et.SubElement(factor, 'name')
        tag_name.text   = str(tag)
        tag_value       = et.SubElement(factor, 'value')
        tag_value.text  = str(value)
        tag_coeff       = et.SubElement(factor, 'coeff')
        tag_coeff.text  = str(model_version_coeff.get(tag,''))
        sorder          = et.SubElement(factor, 'sortOrder')
        sorder.text     = str(sortorder)

    return root_node


def builder(x, root):
    """Building feed XML from the Output DataFrame"""
    for model in x.itertuples():
        gradeDetail             = et.SubElement(root, 'gradeDetail')
        gradeRecordId           = et.SubElement(gradeDetail, 'gradeRecordId')
        gradeRecordId.text      = str(model.gradeRecordId)
        loanId                  = et.SubElement(gradeDetail, 'loanId')
        loanId.text             = str(model.loanId)
        facilityId              = et.SubElement(gradeDetail, 'facilityId')
        facilityId.text         = str(model.facilityId)
        defaultGrade            = et.SubElement(gradeDetail, 'defaultGrade')
        defaultGrade.text       = str(model.defaultGrade)
        effectiveDate           = et.SubElement(gradeDetail, 'effectiveDate')
        effectiveDate.text      = str(model.effectiveDate)
        facilityGrade           = et.SubElement(gradeDetail, 'facilityGrade')
        facilityGrade.text      = str(model.facilityGrade)
        facilityId              = et.SubElement(gradeDetail, 'facilityId')
        facilityId.text         = str(model.facilityId)
        loanId                  = et.SubElement(gradeDetail, 'loanId')
        loanId.text             = str(model.loanId)
        lossGivenDefault        = et.SubElement(gradeDetail, 'lossGivenDefault')
        lossGivenDefault.text   = str(model.lossGivenDefault)
        factorDetails           = et.SubElement(gradeDetail, 'factorDetails')
        factorDetails           = factor_xml_builder(data_tuple = model[1:37],
                                                     tag_names  = factor_columns,
                                                     root_node  = factorDetails)
    return root


pdmodelRes = et.Element('pdmodelRes')
gradeDetails = et.SubElement(pdmodelRes, 'gradeDetails')
gradeDetails = builder(x, gradeDetails)
et.dump(pdmodelRes)