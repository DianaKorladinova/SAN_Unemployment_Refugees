# Dataset Description
The file `team_A_dataset.csv` is a CSV file (values separated by`,`) containing the dataset for the SAN Final Assignment of team A 2023/2024.

## 📆 Timespan
The data were collected in December 2023 from public resources, mainly from the Czech government agencies. Due to the data availability, we were forced to work only with data from **January 2009** to **September 2023**.

## Columns
TODO add units and really used links

- **month** - ordinal numbers for months 1..12
- **year** - year as number
- **kraj** - code of NUTS3 in the Czech Republic (see ČSÚ reference - https://www.czso.cz/documents/10180/20536384/13-72390704.pdf)
- **avg_month_salary** - average salaries per quarter for every region w.r.t to the number of employed people ("https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt-parametry&pvo=MZD01-C&z=T&f=TABULKA&sp=A&skupId=855&filtr=G~F_M~F_Z~F_R~T_P~_S~_null_null_&katalog=30852&pvo=MZD01-C&evo=v208_!_MZD-Q-ABS-od2011_1&u=v159__VUZEMI__100__3018")
- **general_thefts** - number of general thefts in given timespan ("https://www.policie.cz/clanek/statisticke-prehledy-kriminality-za-rok-2023.aspx")
- **break_in_thefts** - number of break in thefts in the Czech Republic in the given timespan("https://www.policie.cz/clanek/statisticke-prehledy-kriminality-za-rok-2023.aspx")
- **celkem** - number of Ukrainian refugees that come in the month to the kraj (additionally **celkem_w?** are distributed lags for window sizes from 2 to 19 = meaning how many refugees came in the last **?** months) ("https://www.mvcr.cz/clanek/statistika-v-souvislosti-s-valkou-na-ukrajine-archiv.aspx?q=Y2hudW09NA%3d%3d")
- **m_do_65** - number of men Ukrainian refugees between 18 and 65 years (additionally **m_do_65_w?** are distributed lags for window sizes from 2 to 19 = meaning how many men refugees came in the last **?** months) ("https://www.mvcr.cz/clanek/statistika-v-souvislosti-s-valkou-na-ukrajine-archiv.aspx?q=Y2hudW09NA%3d%3d")
- **z_do_65** - number of women Ukrainian refugees between 18 and 65 years (additionally **z_do_65_w?** are distributed lags for window sizes from 2 to 19 = meaning how many women refugees came in the last **?** months) ("https://www.mvcr.cz/clanek/statistika-v-souvislosti-s-valkou-na-ukrajine-archiv.aspx?q=Y2hudW09NA%3d%3d")
- **monthly_min_wage** - minimum wage in Kč ("https://www.mpsv.cz/web/cz/prehled-o-vyvoji-castek-minimalni-mzdy")
- **monthly_inflation_rate_wrt_last_year** - inflation as defined by ČSÚ ("https://www.czso.cz/csu/czso/mira_inflace")
- **reer** - Real effective exchange rate (ČNB definition - https://www.cnb.cz/docs/ARADY/MET_LIST/reer_cs.pdf") ("http://www.cnb.cz/arad/#/cs/display_link/single__SREERQ205_")
- **bilance** - the balance of import and export in the Czech Republic ("https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt-parametry&z=T&f=TABULKA&sp=A&skupId=2848&katalog=32935&pvo=VZO011-NP-D")
- **avg_energy_price** - average price of electricity
- **avg_gasoline_price** - average price of gasoline
- **avg_natural_gas_price** - average price of natural gas
- **uchazeciOZamestnaniUoZ** - the total number of job applicants by the end of the month ("https://data.mpsv.cz/web/data/otevrena-data16")
- **noveHlaseniUchazeci** - new job applicants in the month ("https://data.mpsv.cz/web/data/otevrena-data16")
- **noveHlasenaAUvolnenaVPM** - new jobs in the month ("https://data.mpsv.cz/web/data/otevrena-data16")
- **obsazenaAZrusenaVPM** - canceled job places ("https://data.mpsv.cz/web/data/otevrena-data16")
- **absolventiSkolAMladistvi** - applicants from schools ("https://data.mpsv.cz/web/data/otevrena-data16")

## License & Mentions
- ČSÚ data - license link (https://www.czso.cz/csu/czso/podminky_pro_vyuzivani_a_dalsi_zverejnovani_statistickych_udaju_csu)
- ČNB ARAD (https://www.cnb.cz/arad/#/cs/documentation:~:text=je%20dostupn%C3%BD%20zde.-,Jak%C3%A1%20jsou%20pravidla%20pro,%C3%BA%C4%8Det%20m%C5%AF%C5%BEe%20b%C3%BDt%20uzam%C4%8Den.,-Jak%20uv%C3%A1d%C4%9Bt%20ARAD)
- MPSV, MVČR data are publicly available without license
