#! /usr/bin/env python

import os, sys, re
import owlready2 as owlr


### Load the ontologies by IRI:

iao = owlr.get_ontology("http://purl.obolibrary.org/obo/iao.owl").load()
bco = owlr.get_ontology("http://purl.obolibrary.org/obo/bco.owl").load()

### Set namespaces, if they differ (like for OBO purls) from IRI

obo = owlr.get_namespace("http://purl.obolibrary.org/obo/")

#We get http://purl.org/dc/terms/modified from bco! 
dc = owlr.get_namespace("http://purl.org/dc/terms/")
dwc = owlr.get_namespace("http://rs.tdwg.org/dwc/terms/")
ods = "http://github.com/hardistyar/openDS/ods-ontology/terms/"

# open empty ods_ont
ods_ont = owlr.get_ontology(ods)

### import ontologies if necessary?
#ods.imported_ontologies.append(iao)


#### create DigitalSpecimen entity and properties

with ods_ont:
    class DigitalSpecimen(obo.IAO_0000030) : pass
    #class Test(owlr.Thing) : pass

    class modified(dc.modified) :
        domain = [DigitalSpecimen]
        range = [dc.date]

    class name(dwc.scientificName, owlr.DataProperty):
        domain = [DigitalSpecimen]
        range = [str]

    class midsLevel(owlr.DataProperty, owlr.FunctionalProperty):
        domain = [DigitalSpecimen]
        range = [int]

    class physicalSpecimenId(owlr.DataProperty, owlr.FunctionalProperty):
        domain = [DigitalSpecimen]
        range = [str]

    class materialType(owlr.DataProperty):
        domain = [DigitalSpecimen]
        range = [str]

    class institution(owlr.ObjectProperty):
        domain = [DigitalSpecimen]

        
if __name__ == "__main__":
    ods_ont.save("ods.owl", format="ntriples")

