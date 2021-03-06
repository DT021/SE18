def getSP500():
    sp500 = (['A',
        'AAL',
        'AAP',
        'AAPL',
        'ABBV',
        'ABC',
        'ABT',
        'ACN',
        'ADBE',
        'ADI',
        'ADM',
        'ADP',
        'ADS',
        'ADSK',
        'AEE',
        'AEP',
        'AES',
        'AET',
        'AFL',
        'AGN',
        'AIG',
        'AIV',
        'AIZ',
        'AJG',
        'AKAM',
        'ALB',
        'ALGN',
        'ALK',
        'ALL',
        'ALLE',
        'ALXN',
        'AMAT',
        'AMD',
        'AME',
        'AMG',
        'AMGN',
        'AMP',
        'AMT',
        'AMZN',
        'ANDV',
        'ANSS',
        'ANTM',
        'AON',
        'AOS',
        'APA',
        'APC',
        'APD',
        'APH',
        'APTV',
        'ARE',
        'ARNC',
        'ATVI',
        'AVB',
        'AVGO',
        'AVY',
        'AWK',
        'AXP',
        'AYI',
        'AZO',
        'BA',
        'BAC',
        'BAX',
        'BBT',
        'BBY',
        'BDX',
        'BEN',
        'BF.B',
        'BHF',
        'BHGE',
        'BIIB',
        'BK',
        'BKNG',
        'BLK',
        'BLL',
        'BMY',
        'BRK.B',
        'BSX',
        'BWA',
        'BXP',
        'C',
        'CA',
        'CAG',
        'CAH',
        'CAT',
        'CB',
        'CBOE',
        'CBRE',
        'CBS',
        'CCI',
        'CCL',
        'CDNS',
        'CELG',
        'CERN',
        'CF',
        'CFG',
        'CHD',
        'CHRW',
        'CHTR',
        'CI',
        'CINF',
        'CL',
        'CLX',
        'CMA',
        'CMCSA',
        'CME',
        'CMG',
        'CMI',
        'CMS',
        'CNC',
        'CNP',
        'COF',
        'COG',
        'COL',
        'COO',
        'COP',
        'COST',
        'COTY',
        'CPB',
        'CRM',
        'CSCO',
        'CSX',
        'CTAS',
        'CTL',
        'CTSH',
        'CTXS',
        'CVS',
        'CVX',
        'CXO',
        'D',
        'DAL',
        'DE',
        'DFS',
        'DG',
        'DGX',
        'DHI',
        'DHR',
        'DIS',
        'DISCA',
        'DISCK',
        'DISH',
        'DLR',
        'DLTR',
        'DOV',
        'DPS',
        'DRE',
        'DRI',
        'DTE',
        'DUK',
        'DVA',
        'DVN',
        'DWDP',
        'DXC',
        'EA',
        'EBAY',
        'ECL',
        'ED',
        'EFX',
        'EIX',
        'EL',
        'EMN',
        'EMR',
        'EOG',
        'EQIX',
        'EQR',
        'EQT',
        'ES',
        'ESRX',
        'ESS',
        'ETFC',
        'ETN',
        'ETR',
        'EVHC',
        'EW',
        'EXC',
        'EXPD',
        'EXPE',
        'EXR',
        'F',
        'FAST',
        'FB',
        'FBHS',
        'FCX',
        'FDX',
        'FE',
        'FFIV',
        'FIS',
        'FISV',
        'FITB',
        'FL',
        'FLIR',
        'FLR',
        'FLS',
        'FMC',
        'FOX',
        'FOXA',
        'FRT',
        'FTI',
        'FTV',
        'GD',
        'GE',
        'GGP',
        'GILD',
        'GIS',
        'GLW',
        'GM',
        'GOOG',
        'GOOGL',
        'GPC',
        'GPN',
        'GPS',
        'GRMN',
        'GS',
        'GT',
        'GWW',
        'HAL',
        'HAS',
        'HBAN',
        'HBI',
        'HCA',
        'HCP',
        'HD',
        'HES',
        'HIG',
        'HII',
        'HLT',
        'HOG',
        'HOLX',
        'HON',
        'HP',
        'HPE',
        'HPQ',
        'HRB',
        'HRL',
        'HRS',
        'HSIC',
        'HST',
        'HSY',
        'HUM',
        'IBM',
        'ICE',
        'IDXX',
        'IFF',
        'ILMN',
        'INCY',
        'INFO',
        'INTC',
        'INTU',
        'IP',
        'IPG',
        'IPGP',
        'IQV',
        'IR',
        'IRM',
        'ISRG',
        'IT',
        'ITW',
        'IVZ',
        'JBHT',
        'JCI',
        'JEC',
        'JNJ',
        'JNPR',
        'JPM',
        'JWN',
        'K',
        'KEY',
        'KHC',
        'KIM',
        'KLAC',
        'KMB',
        'KMI',
        'KMX',
        'KO',
        'KORS',
        'KR',
        'KSS',
        'KSU',
        'L',
        'LB',
        'LEG',
        'LEN',
        'LH',
        'LKQ',
        'LLL',
        'LLY',
        'LMT',
        'LNC',
        'LNT',
        'LOW',
        'LRCX',
        'LUK',
        'LUV',
        'LYB',
        'M',
        'MA',
        'MAA',
        'MAC',
        'MAR',
        'MAS',
        'MAT',
        'MCD',
        'MCHP',
        'MCK',
        'MCO',
        'MDLZ',
        'MDT',
        'MET',
        'MGM',
        'MHK',
        'MKC',
        'MLM',
        'MMC',
        'MMM',
        'MNST',
        'MO',
        'MON',
        'MOS',
        'MPC',
        'MRK',
        'MRO',
        'MS',
        'MSCI',
        'MSFT',
        'MSI',
        'MTB',
        'MTD',
        'MU',
        'MYL',
        'NAVI',
        'NBL',
        'NCLH',
        'NDAQ',
        'NEE',
        'NEM',
        'NFLX',
        'NFX',
        'NI',
        'NKE',
        'NKTR',
        'NLSN',
        'NOC',
        'NOV',
        'NRG',
        'NSC',
        'NTAP',
        'NTRS',
        'NUE',
        'NVDA',
        'NWL',
        'NWS',
        'NWSA',
        'O',
        'OKE',
        'OMC',
        'ORCL',
        'ORLY',
        'OXY',
        'PAYX',
        'PBCT',
        'PCAR',
        'PCG',
        'PEG',
        'PEP',
        'PFE',
        'PFG',
        'PG',
        'PGR',
        'PH',
        'PHM',
        'PKG',
        'PKI',
        'PLD',
        'PM',
        'PNC',
        'PNR',
        'PNW',
        'PPG',
        'PPL',
        'PRGO',
        'PRU',
        'PSA',
        'PSX',
        'PVH',
        'PWR',
        'PX',
        'PXD',
        'PYPL',
        'QCOM',
        'QRVO',
        'RCL',
        'RE',
        'REG',
        'REGN',
        'RF',
        'RHI',
        'RHT',
        'RJF',
        'RL',
        'RMD',
        'ROK',
        'ROP',
        'ROST',
        'RRC',
        'RSG',
        'RTN',
        'SBAC',
        'SBUX',
        'SCG',
        'SCHW',
        'SEE',
        'SHW',
        'SIVB',
        'SJM',
        'SLB',
        'SLG',
        'SNA',
        'SNPS',
        'SO',
        'SPG',
        'SPGI',
        'SRCL',
        'SRE',
        'STI',
        'STT',
        'STX',
        'STZ',
        'SWK',
        'SWKS',
        'SYF',
        'SYK',
        'SYMC',
        'SYY',
        'T',
        'TAP',
        'TDG',
        'TEL',
        'TGT',
        'TIF',
        'TJX',
        'TMK',
        'TMO',
        'TPR',
        'TRIP',
        'TROW',
        'TRV',
        'TSCO',
        'TSN',
        'TSS',
        'TTWO',
        'TWX',
        'TXN',
        'TXT',
        'UA',
        'UAA',
        'UAL',
        'UDR',
        'UHS',
        'ULTA',
        'UNH',
        'UNM',
        'UNP',
        'UPS',
        'URI',
        'USB',
        'UTX',
        'V',
        'VAR',
        'VFC',
        'VIAB',
        'VLO',
        'VMC',
        'VNO',
        'VRSK',
        'VRSN',
        'VRTX',
        'VTR',
        'VZ',
        'WAT',
        'WBA',
        'WDC',
        'WEC',
        'WELL',
        'WFC',
        'WHR',
        'WLTW',
        'WM',
        'WMB',
        'WMT',
        'WRK',
        'WU',
        'WY',
        'WYN',
        'WYNN',
        'XEC',
        'XEL',
        'XL',
        'XLNX',
        'XOM',
        'XRAY',
        'XRX',
        'XYL',
        'YUM',
        'ZBH',
        'ZION',
        'ZTS'])
    return sp500

def getCryptoList():
    cryptos = (['1ST',
	'2GIVE',
	'808',
	'AC',
	'ACT',
	'ADA',
	'ADT',
	'ADX',
	'AE',
	'AEON',
	'AGI',
	'AGRS',
	'AI',
	'AION',
	'AIR',
	'AKY',
	'ALIS',
	'AMBER',
	'AMP',
	'ANC',
	'ANT',
	'APPC',
	'APX',
	'ARDR',
	'ARK',
	'AST',
	'ATB',
	'ATM',
	'ATS',
	'AUR',
	'AVT',
	'B3',
	'BAT',
	'BAY',
	'BBR',
	'BCAP',
	'BCC',
	'BCD',
	'BCH',
	'BCN',
	'BCX',
	'BCY',
	'BDL',
	'BELA',
	'BET',
	'BIS',
	'BITB',
	'BITBTC',
	'BITCNY',
	'BITEUR',
	'BITGOLD',
	'BITSILVER',
	'BITUSD',
	'BIX',
	'BLITZ',
	'BLK',
	'BLN',
	'BLOCK',
	'BMC',
	'BNB',
	'BNT',
	'BNTY',
	'BOST',
	'BOT',
	'BQ',
	'BRD',
	'BTA',
	'BTC',
	'BTCD',
	'BTG',
	'BTM',
	'BTS',
	'BTSR',
	'BTX',
	'BURST',
	'BUZZ',
	'BYC',
	'BYTOM',
	'CANN',
	'CAT',
	'CCRB',
	'CDT',
	'CFI',
	'CHIPS',
	'CLAM',
	'CLOAK',
	'CMP',
	'CMT',
	'CND',
	'CNX',
	'COFI',
	'COSS',
	'COVAL',
	'CRBIT',
	'CREA',
	'CREDO',
	'CRW',
	'CSNO',
	'CTR',
	'CURE',
	'CVC',
	'DAR',
	'DASH',
	'DATA',
	'DAY',
	'DBC',
	'DCN',
	'DCR',
	'DCT',
	'DDF',
	'DENT',
	'DFS',
	'DGB',
	'DGC',
	'DGD',
	'DICE',
	'DLT',
	'DNT',
	'DOGE',
	'DOPE',
	'DRGN',
	'DTB',
	'DYN',
	'EAC',
	'EBST',
	'EBTC',
	'ECC',
	'ECN',
	'EDG',
	'EDO',
	'ELA',
	'ELF',
	'ELIX',
	'EMB',
	'EMC',
	'EMC2',
	'ENG',
	'ENJ',
	'EOS',
	'EOT',
	'EQT',
	'ETC',
	'ETH',
	'ETHD',
	'ETHOS',
	'ETN',
	'ETP',
	'ETT',
	'EVE',
	'EVX',
	'EXP',
	'FCT',
	'FLDC',
	'FLO',
	'FLT',
	'FRST',
	'FTC',
	'FUEL',
	'FUN',
	'GAM',
	'GAME',
	'GAS',
	'GBG',
	'GBYTE',
	'GCR',
	'GLD',
	'GNO',
	'GNT',
	'GOLOS',
	'GRC',
	'GRWI',
	'GTO',
	'GUP',
	'GVT',
	'GXS',
	'HBN',
	'HEAT',
	'HMQ',
	'HPB',
	'HSR',
	'HUSH',
	'HVN',
	'ICN',
	'ICX',
	'IFC',
	'IFT',
	'IGNIS',
	'INCNT',
	'IND',
	'INF',
	'INK',
	'INS',
	'INXT',
	'IOC',
	'ION',
	'IOP',
	'IOST',
	'IOTA',
	'IQT',
	'ITC',
	'IXC',
	'IXT',
	'JNT',
	'KCS',
	'KICK',
	'KIN',
	'KMD',
	'KNC',
	'KORE',
	'LBC',
	'LCC',
	'LEND',
	'LEV',
	'LGD',
	'LINDA',
	'LINK',
	'LKK',
	'LMC',
	'LOCI',
	'LRC',
	'LSK',
	'LTC',
	'LUN',
	'MAID',
	'MANA',
	'MAX',
	'MBRS',
	'MCAP',
	'MCO',
	'MDA',
	'MEC',
	'MED',
	'MEME',
	'MER',
	'MGC',
	'MGO',
	'MINEX',
	'MINT',
	'MKR',
	'MLN',
	'MNE',
	'MNX',
	'MONA',
	'MRT',
	'MSP',
	'MTH',
	'MTN',
	'MUE',
	'MUSIC',
	'MYB',
	'MYST',
	'MZC',
	'NAMO',
	'NAS',
	'NAV',
	'NBT',
	'NDC',
	'NEBL',
	'NEO',
	'NEOS',
	'NET',
	'NLC2',
	'NLG',
	'NMC',
	'NMR',
	'NOBL',
	'NOTE',
	'NSR',
	'NTO',
	'NULS',
	'NVC',
	'NXC',
	'NXS',
	'NXT',
	'OAX',
	'OBITS',
	'OCL',
	'OCN',
	'ODN',
	'OF',
	'OK',
	'OMG',
	'OMNI',
	'ONION',
	'OPT',
	'OST',
	'PART',
	'PASC',
	'PAY',
	'PBL',
	'PBT',
	'PFR',
	'PING',
	'PINK',
	'PIVX',
	'PIX',
	'PLBT',
	'PLR',
	'PLU',
	'POE',
	'POLY',
	'POSW',
	'POT',
	'POWR',
	'PPC',
	'PPT',
	'PPY',
	'PRG',
	'PRL',
	'PRO',
	'PST',
	'PTC',
	'PTOY',
	'PURA',
	'QASH',
	'QAU',
	'QRK',
	'QRL',
	'QSP',
	'QTL',
	'QTUM',
	'QWARK',
	'R',
	'RADS',
	'RAIN',
	'RBIES',
	'RBX',
	'RBY',
	'RCN',
	'RDD',
	'RDN',
	'REC',
	'RED',
	'REP',
	'REQ',
	'RHOC',
	'RIC',
	'RISE',
	'RLC',
	'RLT',
	'RRT',
	'RUP',
	'RVT',
	'SAFEX',
	'SALT',
	'SAN',
	'SBD',
	'SBTC',
	'SC',
	'SEQ',
	'SHIFT',
	'SIGMA',
	'SIGT',
	'SJCX',
	'SKIN',
	'SKY',
	'SLS',
	'SMART',
	'SMT',
	'SNC',
	'SNGLS',
	'SNM',
	'SNRG',
	'SNT',
	'SPANK',
	'SPR',
	'SRN',
	'START',
	'STEEM',
	'STK',
	'STORJ',
	'STRAT',
	'STX',
	'SUB',
	'SWT',
	'SYS',
	'TAAS',
	'TAU',
	'TCC',
	'TFL',
	'THC',
	'TIME',
	'TIX',
	'TKN',
	'TKR',
	'TKS',
	'TNB',
	'TNT',
	'TOA',
	'TRC',
	'TRCT',
	'TRIG',
	'TRST',
	'TRX',
	'UBQ',
	'UKG',
	'ULA',
	'UNITY',
	'UNO',
	'UNY',
	'URO',
	'USDT',
	'UTK',
	'VEE',
	'VEN',
	'VERI',
	'VIA',
	'VIB',
	'VIVO',
	'VOISE',
	'VOX',
	'VPN',
	'VRC',
	'VRM',
	'VRS',
	'VSL',
	'VTC',
	'VTR',
	'WABI',
	'WAVES',
	'WAX',
	'WCT',
	'WDC',
	'WGO',
	'WGR',
	'WINGS',
	'WTC',
	'WTT',
	'XAS',
	'XAUR',
	'XBC',
	'XBY',
	'XCN',
	'XCP',
	'XDN',
	'XEL',
	'XEM',
	'XID',
	'XLM',
	'XMR',
	'XMT',
	'XMY',
	'XPM',
	'XRB',
	'XRL',
	'XRP',
	'XSPEC',
	'XST',
	'XTZ',
	'XUC',
	'XVC',
	'XVG',
	'XWC',
	'XZC',
	'XZR',
	'YOYOW',
	'ZCC',
	'ZCL',
	'ZEC',
	'ZEN',
	'ZET',
	'ZRX'])
    return cryptos
def getDow():
    dow = (['MMM',
	'AXP',
	'AAPL',
	'BA',
	'CAT',
	'CVX',
	'CSCO',
	'KO',
	'DIS',
	'DWDP',
	'XOM',
	'GE',
	'GS',
	'HD',
	'IBM',
	'INTC',
	'JNJ',
	'JPM',
	'MCD',
	'MRK',
	'MSFT',
	'NKE',
	'PFE',
	'PG',
	'TRV',
	'UTX',
	'UNH',
	'VZ',
	'V',
	'WMT'])
    return dow