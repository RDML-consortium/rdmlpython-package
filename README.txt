==========
rdmlpython
==========

The Real-time PCR Data Markup Language (RDML) is a structured and 
universal data standard for exchanging quantitative PCR (qPCR) 
data. The rdmlpython package allows to load, view, modify and 
save RDML files. 

Typical usage may looks like this::

    #!/usr/bin/env python

    from rdmlpython as rdml

    dat = rdml.Rdml('sample.rdml')

    sam = dat.samples()

    for sample in sam:
        print(sample["id"] + " - " + sample["type"])


