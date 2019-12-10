# web_map
Wanna Create a Web map using python, it is the right coise.

# requirements
* Python 3 required.
* any text editting software should be there(recommended : VsCode), pycharm could also be used.
* any csv file editor like Excel required.

# installation
* Install the following pyton modules:-
``` 
pip install pandas
pip install folium
pip install branca 
```
* pandas, folium, branca are only required, most probably branca will be automatically install when you install folium

* Get the Source code via git
``` git clone https://github.com/pranayteaches/web_map/ ```
# Details and usage
The data.csv file in this repo. is a web extracted database of OSGeo members.
the Extracter.py extracts the necessary data out of it, and saves it to main.csv.
But this while needs to be editted to be able to use it as a datafile for our project.
Some of the datasets needs to be deleted and editted.
now the main.py file executes the whole program and takes main.csv as a datafile.

# Highlights
* Has the tooltip to view details when the curser is placed above the marker.
* Has the custom logo. To modify it one can replace the icon.png file or can provide the marker's location.
* The data is imported from the csv file so one can either create a csv file with the same headings.
* One can edit the circle marker and can t=mark the circle to the place you want. this is helpful when you want to select a larger reigon or don't know the exact location.
* One can also edit the initial place from where the map would be displayed by editing the ``` folium.map() ```

Further details are provided in the files itself.

To know the hardwork beside it one must view the personal_readme.txt




