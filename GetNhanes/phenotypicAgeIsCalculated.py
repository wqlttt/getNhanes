# #Demographic
# DEMO <- nhanes_load_data(c("DEMO","DEMO_B","DEMO_C","DEMO_D","DEMO_E","DEMO_F","DEMO_G","DEMO_H","DEMO_I","DEMO_J"),
#                          c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Activities of daily livings
# PFQ <- nhanes_load_data(c("PFQ","PFQ_B","PFQ_C","PFQ_D","PFQ_E","PFQ_F","PFQ_G","PFQ_H","PFQ_I","PFQ_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #BMI
# BMI <- nhanes_load_data(c("BMX","BMX_B","BMX_C","BMX_D","BMX_E","BMX_F","BMX_G","BMX_H","BMX_I","BMX_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Body Fat
# BIX <- nhanes_load_data(c("BIX","BIX_B","BIX_C"),
#                         c("1999-2000","2001-2002","2003-2004"))
# #FEV1
# SPX <- nhanes_load_data(c("SPX_E","SPX_F","SPX_G"),
#                         c("2007-2008","2009-2010","2011-2012"))
# #Grip strength
# MGX <- nhanes_load_data(c("MGX_G","MGX_H"),
#                         c("2011-2012","2013-2014"))
# #Self-rated health
# HSQ <- nhanes_load_data(c("HSQ_B","HSQ_C","HSQ_D","HSQ_E","HSQ_F","HSQ_G","HSQ_H","HSQ_I","HSQ_J"),
#                         c("2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Walk speed
# MSX <- nhanes_load_data(c("MSX","MSX_B"),
#                         c("1999-2000","2001-2002"))
# #VO2 max
# CVX <- nhanes_load_data(c("CVX","CVX_B","CVX_C"),
#                         c("1999-2000","2001-2002","2003-2004"))
# #Albumin
# SGL <- nhanes_load_data(c("LAB18","L40_B","L40_C","BIOPRO_D","BIOPRO_E","BIOPRO_F","BIOPRO_G","BIOPRO_H","BIOPRO_I","BIOPRO_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #BAP
# BAP <- nhanes_load_data(c("LAB11","L11_B","L11_C"),
#                         c("1999-2000","2001-2002","2003-2004"))
# #Basophils
# WBC <- nhanes_load_data(c("LAB25","L25_B","L25_C","CBC_D","CBC_E","CBC_F","CBC_G","CBC_H","CBC_I","CBC_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Cadmium
# CAD <- nhanes_load_data(c("LAB06","L06_B","L06BMT_C","PbCd_D","PbCd_E","PbCd_F","PbCd_G","PBCD_H","PBCD_I"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016"))
# #CRP
# CRP <- nhanes_load_data(c("LAB11","L11_B","L11_C","CRP_D","CRP_E","CRP_F","HSCRP_I","HSCRP_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2015-2016","2017-2018"))
# #Cystatin C
# CYS <- nhanes_load_data(c("SSCYST_A","SSCYST_B"),
#                         c("1999-2000","2001-2002"))
# #Blood pressure
# BPX <- nhanes_load_data(c("BPX","BPX_B","BPX_C","BPX_D","BPX_E","BPX_F","BPX_G","BPX_H","BPX_I","BPX_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Gamma glutamyl transferase
# GGT <- nhanes_load_data(c("L40_2_B","L40_C","BIOPRO_D","BIOPRO_E","BIOPRO_F","BIOPRO_G","BIOPRO_H","BIOPRO_I","BIOPRO_J"),
#                         c("2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Plasma fasting glucose
# GLU <- nhanes_load_data(c("LAB10AM","L10AM_B","L10AM_C","GLU_D","GLU_E","GLU_F","GLU_G","GLU_H","INS_H","GLU_I","INS_I"),
#                          c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2013-2014","2015-2016","2015-2016"))
# #Fasting
# PHH <- nhanes_load_data(c("PH","PH_B","PH_C","FASTQX_D","FASTQX_E","FASTQX_F","FASTQX_G","FASTQX_H","FASTQX_I","FASTQX_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Hba1c
# HBA <- nhanes_load_data(c("LAB10","L10_B","L10_C","GHB_D","GHB_E","GHB_F","GHB_G","GHB_H","GHB_I","GHB_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #HDL
# HDLchol <- nhanes_load_data(c("LAB13","L13_B","L13_C","HDL_D","HDL_E","HDL_F","HDL_G","HDL_H","HDL_I","HDL_J"),
#                             c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #LDL
# TRI <- nhanes_load_data(c("LAB13AM","L13AM_B","L13AM_C","TRIGLY_D","TRIGLY_E","TRIGLY_F","TRIGLY_G","TRIGLY_H","TRIGLY_I"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016"))
# #Total cholesterol
# CHL <- nhanes_load_data(c("Lab13","l13_b","l13_c","TCHOL_D","TCHOL_E","TCHOL_F","TCHOL_G","TCHOL_H","TCHOL_I","TCHOL_J"),
#                         c("1999-2000","2001-2002","2003-2004","2005-2006","2007-2008","2009-2010","2011-2012","2013-2014","2015-2016","2017-2018"))
# #Vitamin A
# VITA <- nhanes_load_data(c("LAB06","L06VIT_B","L45VIT_C","VITAEC_D"),
#                          c("1999-2000","2001-2002","2003-2004","2005-2006"))
# #Vitamin B
# VITAB <- nhanes_load_data(c("LAB06","L06_B","L06NB_C","B12_D","VITB12_G","VITB12_H"),
#                           c("1999-2000","2001-2002","2003-2004","2005-2006","2011-2012","2013-2014"))
# #Vitamin C
# VITAC <- nhanes_load_data(c("L06VIT_C","VIC_D"),
#                           c("2003-2004","2005-2006"))