jasper-movies
=============

Jasper Movies Plugin

## Installation Steps

1. Install dependencies
```
sudo pip install imdbpy
```
2. Place the movies/ folder in your jasper_directory/plugins/speechhandler/ folder
3. Restart Jasper

## Usage
```
YOU: movies
JASPER: What movie?
YOU: iron man
JASPER: Searching top five results for.  iron man
JASPER: Did you mean Iron Man (2008)?
YOU: no
JASPER: Did you mean Iron Man (1994)?
YOU: no
JASPER: Did you mean Iron Man (2010)?
YOU: no
JASPER: Did you mean Iron Man 3 (2013)?
YOU: yes
JASPER: Iron Man 3 (2013).  Rating.  7.3 out of 10.  Runtime.  130 minutes.  Genres.  Action.  Adventure.  Sci-Fi.  Plot.  When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.  Directors.  Shane Black.  .  Producers.  Victoria Alonso.  Mitchell Bell.  Stephen Broussard.  Louis D'Esposito.  Jon Favreau.  .  Cast.  Robert Downey Jr..  Gwyneth Paltrow.  Don Cheadle.  Guy Pearce.  Rebecca Hall.
```
