a=$(locate /home/*.mozilla/*/places.sqlite)
sqlite3 $a "select url,visit_count from moz_places" > history

# select url from moz_places 