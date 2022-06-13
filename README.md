# python-ords-code-patterns
Various small code snippets that use python to interact with Oracle REST Database Services (ORDS)

Current open ORDS endpoints: 

## Annual Characteristics of New Housing | Single-Family Sold | New Single-Family Houses sold x Finance Type

All tables would include: 
- Year 
- Total units sold (this is an aggregate of both attached and detached homes)
- Total units sold using convential loans
- Total units sold using FHA-insured loans
- Total units sold using VA-guaranteed loans
- Total units sold using Cash 

The original dataset was retrived from: https://www.census.gov/construction/chars/ 
But it has been transformed slightly so I could create various tables. The URIs are all open/unauthenticaed, and are meant to be used as examples for the related python + ORDS enabled table code snippets. 

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
- U.S. RSE/SE 
-   This quantifies **R.S.E** Relative Standard Error (in percent), **S.E.** Standard Error (in percentage points). It shows Region by Total, Conventional, FHA, or VA, or Cash loan. 
  - https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_rse_se/
