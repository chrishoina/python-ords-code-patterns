# python-ords-code-patterns
Various small code snippets that use python to interact with Oracle REST Database Services

Current open ORDS endpoints: 
Annual Characteristics of New Housing | Single-Family Sold | New Single-Family Houses sold x Finance Type
All tables would include: 
-Year 
-Total units sold (this is an aggregate of both attached and detached homes)
-Total units sold using convential loans
- Total units sold using FHA-insured loans
- Total units sold using VA-guaranteed loans

The original dataset was retrived from: https://www.census.gov/construction/chars/ 
But it has been transformed slightly so I could create various tables. The URIs are all open/unauthenticaed, and are meant to be used as examples for related python code snippets. 

- U.S Midwest
  - https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_mwest/

https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_neast/
https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_rse_se/
https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_south/
https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_us/
https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/homefin_west/
