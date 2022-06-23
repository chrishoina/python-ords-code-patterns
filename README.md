# python-ords-code-patterns
## Intended Audience
I'm a python developer who is comfortable with python libraries but less so with databases and database schemas. I want to learn how python, it's popular libraries and ORDS APIs can work together to achieve my development goals. 

### Purpose
Various small code snippets that use python to interact with Oracle REST Database Services (ORDS)

## Current open ORDS endpoints: 

### Annual Characteristics of New Housing
*The original dataset was retrived from: https://www.census.gov/construction/chars/; it has been transformed slightly so I could create various tables. The URIs are all open/unauthenticaed and are meant to be used as examples for their related python + ORDS enabled table code snippets.*

#### All tables (excluding the U.S. RSE/RS table) include: 
*These are all New U.S. single-family houses sold xfinance type used; depending on the table the years will range from 1978-2021*

#### Data included:

- Year 
- Total units sold (this is an aggregate of both attached and detached homes)
- Total units sold using convential loans
- Total units sold using FHA-insured loans
- Total units sold using VA-guaranteed loans
- Total units sold using Cash 

#### Tables:
- U.S Midwest
  - https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_mwest/
- U.S. Northeast
  - https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_neast/
- U.S. South
  - https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_south/
- U.S. Total
  - https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_us/
- U.S West
  -  https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_west/

### RSE/RS Table includes: 
*This table shows R.S.E Relative Standard Error (in percent) / S.E. Standard Error (in percentage points).* 

#### Data included:

- Region and:
  - RSE/RS for Total units sold (this is an aggregate of both attached and detached homes)
  - RSE/RS for Total units sold using convential loans
  - RSE/RS for Total units sold using FHA-insured loans
  - RSE/RS for Total units sold using VA-guaranteed loans
  - RSE/RS for Total units sold using Cash 

#### Table
- U.S. RSE/SE 
  - https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_rse_se/
