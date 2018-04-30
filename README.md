Lab 12: Using a Third Party App (Geopy)
====

### Today's lab concerns how we can integrate a third party application/library in a web application.

### Topics:
* Geopy (http://geopy.readthedocs.io/en/stable/): a python library/api for accessing and querying geographic information.
* Django: custom (non object related) forms using `generic.FormView`
* Django: overriding a `get_context_data` method


# A. Let's Play With `geopy`
1. Create (and activate) a virtual environment named `lab12demo_env`
2. Install geopy: `pip install geopy`
- geopy as a request api to many different GIS data stores. We will use the **Nominatim** data store to query for various addresses.
3. Try it out in a python shell:

`from geopy.geocoders import Nominatim`

**connect to the gis service**

`geolocator = Nominatim()`

**create a query string**

`q = '1009 diamond, las vegas, nm'`

**perform query against gis service. should return a Location object if anything.**

`loc = geolocator.geocode(q)`

**Check out what you can do with a location object**

`help(loc)`

**Try:**

`print loc.address`

`print loc.latitude`

`print loc.longitude`

**Can we compute distance between to geographic locations (using geodisic measurement)? Sure!**

`from geopy.distance import distance`

** Location A **

`q = '1314 chavez st, las vegas, nm'`

`a = geolocator.geocode(q)`

** Location B**

`q = '1009 diamond, las vegas, nm'`

`b = geolocator.geocode(q)`

`aloc = (a.latitude, a.longitude)`

`bloc = (b.latitude, b.longitude)`

`d = distance(aloc, bloc).miles`

`print 'distance', d`


# B. Get Started With a Simple Django App
1. __fork__ this repository to your GitHub account (use the fork button at the top)
2. __clone__ your forked repo to your local working directory
3. cd to repository/project root
... you know the drill...
4. Use virtual environment that you created above for this project
5. Run: `pip install -r requirements.txt`
6. Setup the django app: `python manage.py migrate`
7. Run the test server: `python manage.py runserver`
8. In a browser, the home page for this lab should be displayed. 

E.g., `http://localhost:8000`

TODO: geoquery App
----
### 1. Hook up the url located on the home page to go to the `lookup` url using the url template filter. 

#### a. Edit geoquery/templates/geoquery/index.html

### 2. Try out the form. No results? Let's use geopy to perform a lookup when a query is submitted through the form.

#### a. Open geoquery/views.py
#### b. Add a geopy lookup to the `get_context_data` override.
#### c. Add a template variable to show the result of the query.
#### d. Test your query in the form to see results.

### 3. Add a new page to the app to measure distance from highlands university to a location input into the query form. The official address of NMHU is '1009 diamond, las vegas, nm'.  
#### a. Create a new view for processing the form. You can start with a copy of the LookupView.
#### b. Reference the form class in the new view.
#### c. Create a new template for the view (start with a copy of lookup.html)
#### d. In your new view in geoquery/views.py, modify the get_context_data override, implement the distance calculation and write to a new template variable.
#### e. Add a route to the geoquery/urls.py file to your new view.
#### f. Modify the new template to display the distance calculation.
#### g. Test.

### Done.