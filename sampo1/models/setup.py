def setup(dbh):
    dbh.EK.bulk_update(ek_initlist, dbsession=dbh.session())


# add additional initial data here


ek_initlist = [     # TODO: not yet
    ('@SYSNAME', 'System names',
     [
         ('sampo'.upper(), 'sampo'),
     ]
     ),
    # ('@POSTTYPE', 'Post types',
    #  [
    #      ('Article', 'article'),
    #      ('News', 'news')
    #  ]
    #  ),
]
