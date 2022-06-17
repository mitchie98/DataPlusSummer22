import pandas as pd

# data
df = pd.read_csv(r'C:\Users\hessi\PycharmProjects\App\Universal Health Coverage Policies.csv', encoding = 'utf-16', sep='\t')
# Maybe make automatic update. Still need to make UTF-8 encoded out of MonQcle, automate CSV downloads

# removing unnecessary columns (caution checks, etc.)
for col in df.columns:
    if col[0:1] == '_':
        df.drop(col, axis=1, inplace=True)

# refactors 1/0 to T/F, for readability in graphics
df = df.replace(1, True)
df = df.replace(0, False)
df = df.fillna('No Data')

# cleans up the strings in the csv (removes [=,(), ""])
def clean_str(row):
    return row.strip('=()"')
cols=['disadvantagedgroups_schemes','needs_schemes','healthoutcomes_schemes', 'userfeesexemptions_schemes','priorityservicesprocess_schemes','selectionprocess_populations_schemes', 'completed']
for col in cols:
    df[col] = df[col].apply(lambda row: clean_str(row))

# adds code column, necessary to generate map, must figure out how to automate on new data input.
codes = {
    "Afghanistan": "AFG",
    "Albania": "ALB",
    "Algeria": "DZA",
    "American Samoa": "ASM",
    "Andorra": "AND",
    "Angola": "AGO",
    "Anguilla": "AIA",
    "Antarctica": "ATA",
    "Antigua and Barbuda": "ATG",
    "Argentina": "ARG",
    "Armenia": "ARM",
    "Aruba": "ABW",
    "Australia": "AUS",
    "Austria": "AUT",
    "Azerbaijan": "AZE",
    "Bahamas": "BHS",
    "Bahrain": "BHR",
    "Bangladesh": "BGD",
    "Barbados": "BRB",
    "Belarus": "BLR",
    "Belgium": "BEL",
    "Belize": "BLZ",
    "Benin": "BEN",
    "Bermuda": "BMU",
    "Bhutan": "BTN",
    "Bolivia, Plurinational State of": "BOL",
    "Bolivia": "BOL",
    "Bosnia and Herzegovina": "BIH",
    "Botswana": "BWA",
    "Bouvet Island": "BVT",
    "Brazil": "BRA",
    "British Indian Ocean Territory": "IOT",
    "Brunei Darussalam": "BRN",
    "Brunei": "BRN",
    "Bulgaria": "BGR",
    "Burkina Faso": "BFA",
    "Burundi": "BDI",
    "Cambodia": "KHM",
    "Cameroon": "CMR",
    "Canada": "CAN",
    "Cape Verde": "CPV",
    "Cayman Islands": "CYM",
    "Central African Republic": "CAF",
    "Chad": "TCD",
    "Chile": "CHL",
    "China": "CHN",
    "Christmas Island": "CXR",
    "Cocos (Keeling) Islands": "CCK",
    "Colombia": "COL",
    "Comoros": "COM",
    "Congo": "COG",
    "Congo, the Democratic Republic of the": "COD",
    "Cook Islands": "COK",
    "Costa Rica": "CRI",
    "CÃ´te d'Ivoire": "CIV",
    "Ivory Coast": "CIV",
    "Croatia": "HRV",
    "Cuba": "CUB",
    "Cyprus": "CYP",
    "Czech Republic": "CZE",
    "Denmark": "DNK",
    "Djibouti": "DJI",
    "Dominica": "DMA",
    "Dominican Republic": "DOM",
    "Ecuador": "ECU",
    "Egypt": "EGY",
    "El Salvador": "SLV",
    "Equatorial Guinea": "GNQ",
    "Eritrea": "ERI",
    "Estonia": "EST",
    "Ethiopia": "ETH",
    "Falkland Islands (Malvinas)": "FLK",
    "Faroe Islands": "FRO",
    "Fiji": "FJI",
    "Finland": "FIN",
    "France": "FRA",
    "French Guiana": "GUF",
    "French Polynesia": "PYF",
    "French Southern Territories": "ATF",
    "Gabon": "GAB",
    "Gambia": "GMB",
    "Georgia": "GEO",
    "Germany": "DEU",
    "Ghana": "GHA",
    "Gibraltar": "GIB",
    "Greece": "GRC",
    "Greenland": "GRL",
    "Grenada": "GRD",
    "Guadeloupe": "GLP",
    "Guam": "GUM",
    "Guatemala": "GTM",
    "Guernsey": "GGY",
    "Guinea": "GIN",
    "Guinea-Bissau": "GNB",
    "Guyana": "GUY",
    "Haiti": "HTI",
    "Heard Island and McDonald Islands": "HMD",
    "Holy See (Vatican City State)": "VAT",
    "Honduras": "HND",
    "Hong Kong": "HKG",
    "Hungary": "HUN",
    "Iceland": "ISL",
    "India": "IND",
    "Indonesia": "IDN",
    "Iran, Islamic Republic of": "IRN",
    "Iraq": "IRQ",
    "Ireland": "IRL",
    "Isle of Man": "IMN",
    "Israel": "ISR",
    "Italy": "ITA",
    "Jamaica": "JAM",
    "Japan": "JPN",
    "Jersey": "JEY",
    "Jordan": "JOR",
    "Kazakhstan": "KAZ",
    "Kenya": "KEN",
    "Kiribati": "KIR",
    "Korea, Democratic People's Republic of": "PRK",
    "Korea, Republic of": "KOR",
    "South Korea": "KOR",
    "Kuwait": "KWT",
    "Kyrgyzstan": "KGZ",
    "Lao People's Democratic Republic": "LAO",
    "Latvia": "LVA",
    "Lebanon": "LBN",
    "Lesotho": "LSO",
    "Liberia": "LBR",
    "Libyan Arab Jamahiriya": "LBY",
    "Libya": "LBY",
    "Liechtenstein": "LIE",
    "Lithuania": "LTU",
    "Luxembourg": "LUX",
    "Macao": "MAC",
    "Macedonia, the former Yugoslav Republic of": "MKD",
    "Madagascar": "MDG",
    "Malawi": "MWI",
    "Malaysia": "MYS",
    "Maldives": "MDV",
    "Mali": "MLI",
    "Malta": "MLT",
    "Marshall Islands": "MHL",
    "Martinique": "MTQ",
    "Mauritania": "MRT",
    "Mauritius": "MUS",
    "Mayotte": "MYT",
    "Mexico": "MEX",
    "Micronesia, Federated States of": "FSM",
    "Moldova, Republic of": "MDA",
    "Monaco": "MCO",
    "Mongolia": "MNG",
    "Montenegro": "MNE",
    "Montserrat": "MSR",
    "Morocco": "MAR",
    "Mozambique": "MOZ",
    "Myanmar": "MMR",
    "Burma": "MMR",
    "Namibia": "NAM",
    "Nauru": "NRU",
    "Nepal": "NPL",
    "Netherlands": "NLD",
    "Netherlands Antilles": "ANT",
    "New Caledonia": "NCL",
    "New Zealand": "NZL",
    "Nicaragua": "NIC",
    "Niger": "NER",
    "Nigeria": "NGA",
    "Niue": "NIU",
    "Norfolk Island": "NFK",
    "Northern Mariana Islands": "MNP",
    "Norway": "NOR",
    "Oman": "OMN",
    "Pakistan": "PAK",
    "Palau": "PLW",
    "Palestinian Territory, Occupied": "PSE",
    "Panama": "PAN",
    "Papua New Guinea": "PNG",
    "Paraguay": "PRY",
    "Peru": "PER",
    "Philippines": "PHL",
    "Pitcairn": "PCN",
    "Poland": "POL",
    "Portugal": "PRT",
    "Puerto Rico": "PRI",
    "Qatar": "QAT",
    "RÃ©union": "REU",
    "Romania": "ROU",
    "Russian Federation": "RUS",
    "Russia": "RUS",
    "Rwanda": "RWA",
    "Saint Helena, Ascension and Tristan da Cunha": "SHN",
    "Saint Kitts and Nevis": "KNA",
    "Saint Lucia": "LCA",
    "Saint Pierre and Miquelon": "SPM",
    "Saint Vincent and the Grenadines": "VCT",
    "Saint Vincent & the Grenadines": "VCT",
    "St. Vincent and the Grenadines": "VCT",
    "Samoa": "WSM",
    "San Marino": "SMR",
    "Sao Tome and Principe": "STP",
    "Saudi Arabia": "SAU",
    "Senegal": "SEN",
    "Serbia": "SRB",
    "Seychelles": "SYC",
    "Sierra Leone": "SLE",
    "Singapore": "SGP",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "Solomon Islands": "SLB",
    "Somalia": "SOM",
    "South Africa": "ZAF",
    "South Georgia and the South Sandwich Islands": "SGS",
    "South Sudan": "SSD",
    "Spain": "ESP",
    "Sri Lanka": "LKA",
    "Sudan": "SDN",
    "Suriname": "SUR",
    "Svalbard and Jan Mayen": "SJM",
    "Swaziland": "SWZ",
    "Sweden": "SWE",
    "Switzerland": "CHE",
    "Syrian Arab Republic": "SYR",
    "Taiwan, Province of China": "TWN",
    "Taiwan": "TWN",
    "Tajikistan": "TJK",
    "Tanzania, United Republic of": "TZA",
    "Thailand": "THA",
    "Timor-Leste": "TLS",
    "Togo": "TGO",
    "Tokelau": "TKL",
    "Tonga": "TON",
    "Trinidad and Tobago": "TTO",
    "Tunisia": "TUN",
    "Turkey": "TUR",
    "Turkmenistan": "TKM",
    "Turks and Caicos Islands": "TCA",
    "Tuvalu": "TUV",
    "Uganda": "UGA",
    "Ukraine": "UKR",
    "United Arab Emirates": "ARE",
    "United Kingdom": "GBR",
    "United States": "USA",
    "United States Minor Outlying Islands": "UMI",
    "Uruguay": "URY",
    "Uzbekistan": "UZB",
    "Vanuatu": "VUT",
    "Venezuela, Bolivarian Republic of": "VEN",
    "Venezuela": "VEN",
    "Viet Nam": "VNM",
    "Vietnam": "VNM",
    "Virgin Islands, British": "VGB",
    "Virgin Islands, U.S.": "VIR",
    "Wallis and Futuna": "WLF",
    "Western Sahara": "ESH",
    "Yemen": "YEM",
    "Zambia": "ZMB",
    "Zimbabwe": "ZWE"
}

def findcode(row, dict):
    if row in dict:
        return dict[row]
    else:
        return ''


df['Code'] = df['Name'].apply(lambda row: findcode(row, codes))

# counts number of policies implemented from the 9 main policies defined in the codebook


def pol_implemented(row):
    c = 0
    if row['national_policy_threshold ']:
        c = c + 1
    if row['prepaid_services']:
        c = c + 1
    if row['redistribution_pooling']:
        c = c + 1
    if row['fragmentation_pooling']:
        c = c + 1
    if row['payments_linked']:
        c = c + 1
    if row['purchasing_separate']:
        c = c + 1
    if row['specifying_benefits']:
        c = c + 1
    if row['specifying_benefits']:
        c = c + 1
    if row['pointofcare_exemptions']:
        c = c + 1
    return c


df['policies_implemented'] = df.apply(lambda row: pol_implemented(row), axis=1)

# proportion of 9 core policies implemented
df['policy_prop'] = df['policies_implemented'] / 9


# categorizes the proportions into 1 of 5 bins, I think this will go on the map
def bin_prob(row):
    if row['policy_prop'] <= .2:
        return 1
    if .2 < row['policy_prop'] <= .4:
        return 2
    if .4 < row['policy_prop'] <= .6:
        return 3
    if .6 < row['policy_prop'] <= .8:
        return 4
    else:
        return 5


df['prop_binned'] = df.apply(lambda row: bin_prob(row), axis=1)

# rename columns
df = df.rename(columns={"national_policy_threshold ": "National Policy",
                   "prepaid_services": "Prepayment Mechanisms",
                   "redistribution_pooling": "Fund Distribution Btwn Schemes",
                   "fragmentation_pooling": "Fragmentation Prevention",
                   "payments_linked": "Linked Payments",
                   "purchasing_separate": "Purchaser-Provider Separation",
                   "specifying_benefits": "Specific Benefits Package",
                   "pointofcare_exemptions": "Point of Car Exemptions"})


df.to_csv('processed_UHC_data.csv')