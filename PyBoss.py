
import os
import csv
import re
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
input_file = os.path.join('raw_data', 'employee_data.csv')
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []
#read the csv and convert it into a list of dictionaries
with open(input_file,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        #append informations
        for row in reader:
        # Get all data in employee data row
            emp_id.append(row['Emp ID'])
            first_name.append(row['Name'].split(" ")[0])
            last_name.append(row['Name'].split(" ")[1])
            dob.append(row['DOB'].split('-')[1] + '/' + row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
            ssn.append('***-**-' + row['SSN'].split('-')[2])
            state.append(us_state_abbrev[row['State']])
                    
#zip all together
new_data = zip(emp_id, first_name, last_name, dob, ssn, state)           

#output file
output_file = os.path.join('raw_data', 'new_employee_data.csv')
#open and write to csv file
with open(output_file,'w') as csvwrite:
    outputfile = csv.writer(csvwrite,delimiter =',')
    outputfile.writerow(['Emp ID','First Name', 'Last Name', 'DOB','SSN', 'State'])
    outputfile.writerows(new_data)