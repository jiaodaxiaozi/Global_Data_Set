import osm2gmns as og

net = og.getNetFromOSMFile('map.osm', network_type=('railway', 'auto', 'walk', 'bike'), POIs=True, default_lanes=True,default_speed=True)
# osm2gmns supports five different network types, including auto, bike, walk, railway, aeroway. 'auto' is set as default.

og.connectPOIWithNet(net)

og.generateNodeActivityInfo(net)

og.outputNetToCSV(net)