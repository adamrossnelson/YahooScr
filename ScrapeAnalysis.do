// Open excel file created by ScrapeBuild.jpynb
import excel "all_asca_messages.xlsx", sheet("Sheet1") firstrow clear

// Import text file messages from ASCA
gen strL msgBody = fileread("msgs.asca.apr192018/asca_" + string(msgId) + "_post.txt")

// Save the dta file
save all_asca_messages.dta, replace

// Generate new variables
gen year = substr(Date,1,4)
gen month = substr(Date,6,2)
gen day = substr(Date,9,2)

destring year, replace
destring month, replace
destring day, replace

// Correct bad date in message number 1071
replace year = 2002 if msgId == 1071

// Make some histograms
histogram month if ///
inlist(year, 2008, 2009, 2010, 2011, 2012, 2013, 2014), ///
discrete frequency xlabel(1(1)12, labsize(small)) by(year) name(months)

histogram year, discrete frequency xlabel(2000(1)2018, labsize(small)) name(years)
